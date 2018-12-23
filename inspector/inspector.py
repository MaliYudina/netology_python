import requests
import json
import logging
from config import TOKEN, ID_INPUT

# from progressbar import ProgressBar


VERSION = '5.92'
URL_USER = 'https://api.vk.com/method/users.get'
URL_FRIENDS = 'https://api.vk.com/method/friends.get'
URL_GROUPS = 'https://api.vk.com/method/groups.get'
URL_MEMBERS = 'https://api.vk.com/method/groups.getMembers'
URL_GROUP_ID = 'https://api.vk.com/method/groups.getById'
ERROR_MANY_REQ = 6
USER_ID = ID_INPUT

print('\nStep 1 is being started...\n')
progress = []


class TooManyRequestsError:
    """
    class for error with many requests
    """

    def __init__(self, name):
        self.name = name


# def progress_bar(fn):
#     try:
#         '' % fn()
#     except:
#         fn
#
#     def wrapped():
#         try:
#             sys.stdout.write('')
#             fn()
#             sys.stdout.write('')
#         except KeyboardInterrupt:
#             sys.stdout.write('')
#
#     progress.append(wrapped)
#     return wrapped
#
#
# def current_bar():
#     pbar = ProgressBar(maxval=50)
#     for i in pbar((i for i in range(50))):
#         time.sleep(0.01)

def params_vk(url, id):
    params = {'access_token': TOKEN, 'v': VERSION, 'fields': 'screen_name'}
    if url == URL_FRIENDS:
        params['user_id'] = id
        if not str(id).isdigit():
            params['nickname'] = id  # TODO: check why not ok
            print(id)
    else:
        params['group_id'] = id

    if (url == URL_GROUPS) or (url == URL_GROUP_ID):
        params['fields'] = 'members_count'
        # try:
        #     for bar in progress: bar()
        # except KeyboardInterrupt:
        #     sys.stdout('')
    return params


def errors_logged(fn):
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as err:
            logging.error('{}(*{}, **{}) failed {}'.format(
                function.__name__, repr(args), repr(kwargs), repr(err)))
            raise
    return wrapped


@errors_logged
def do_request(url, id):
    while True:
        message = requests.get(url, params_vk(url, id)).json()
        if 'error' in message.keys():
            if message['error']['error_code'] != ERROR_MANY_REQ:
                raise Exception('Retry error')  # Class instance, not class itself
        else:
            return message


def find_secret(user_id):
    """
    search all friends list,
    determine the groups list
    and check if friends are in this groups
    """
    # Get target user friends list
    friends_list_raw = do_request(URL_FRIENDS, user_id)['response']['items']
    # Get target user groups list
    group_names_list = do_request(URL_GROUPS, user_id)['response']['items']
    groups_list_qty = len(group_names_list)

    friends = set()
    for friend in friends_list_raw:
        friends.add(friend['id'])

    secret_groups = []
    for num, group_id in enumerate(group_names_list):
        print('Checking {} of {}'.format(num + 1, groups_list_qty))
        # current_bar()
        group_members_raw = do_request(URL_MEMBERS, group_id)['response']['items']
        members = set()
        for member in group_members_raw:
            members.add(member['id'])

        print('Friends that are also in this group:', friends & members)

        # Кажется, это должно работать, но не работает
        if not (friends & members):
            secret_groups.append(group_id)

        print(secret_groups)

    # Writing result
    filename = 'groups_answer.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(secret_groups, sort_keys=False))

    print('\nStep 1 is finished.\n\nStarting step 2...\n')

    group_names_list = []
    num = 1
    secret_group_list_qty = len(secret_groups)
    for num, secret_group in enumerate(secret_groups, num):
        print('Checking {} of {}'.format(num, secret_group_list_qty))
        # current_bar()
        num += 1

        group = do_request(URL_GROUP_ID, secret_group)['response'][0]
        group_dict = {
            'name': group['name'],
            'gid': group['id'],
            'members_count': group['members_count'],
        }
        group_names_list.append(group_dict)

    filename = 'groups_answer.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(group_names_list, sort_keys=False,
                           indent=4, ensure_ascii=False, separators=(',', ': ')))
    print('Search results are written down - ', filename)
    print('Total were found', groups_list_qty, 'groups')


if __name__ == '__main__':
    find_secret(USER_ID)
