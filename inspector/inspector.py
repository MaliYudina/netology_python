import requests
import json
import logging
import time
from config import TOKEN, ID_INPUT


from progressbar import ProgressBar


VERSION = '5.92'
URL_USER = 'https://api.vk.com/method/users.get'
URL_FRIENDS = 'https://api.vk.com/method/friends.get'

# Возвращает список сообществ указанного пользователя.
URL_GROUPS = 'https://api.vk.com/method/groups.get'

URL_ARE_MEMBERS = 'https://api.vk.com/method/groups.isMember'
URL_GROUP_ID = 'https://api.vk.com/method/groups.getById'
ERROR_MANY_REQ = 6
USER_ID = ID_INPUT

print('\nStep 1 is being started...\n')
progress = []


class TooManyRequestsError(Exception):
    """
    class for error with many requests
    """

    def __init__(self, name):
        self.name = name


def params_vk(**kwargs):
    params = {
        'access_token': TOKEN,
        'v': VERSION,
        'fields': 'screen_name',
        **kwargs,
    }
    return params


def resolve_uid(user_id):
    if user_id.isnumeric():
        return user_id
    return do_request(URL_USER, nickname=user_id)[0]['id']


def errors_logged(fn):
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as err:
            logging.error('{}(*{}, **{}) failed {}'.format(
                fn.__name__, repr(args), repr(kwargs), repr(err)))
            raise
    return wrapped


@errors_logged
def do_request(url, **kwargs):
    while True:
        message = requests.get(url, params_vk(**kwargs)).json()
        if 'error' in message.keys():
            logging.error('API error: %s', message['error'])
            if message['error']['error_code'] == ERROR_MANY_REQ:
                raise TooManyRequestsError('Cannot retry anymore')
            time.sleep(1)
        else:
            return message['response']


def group_is_private(membership_obj_list):
    """
    iterating through the given list, look for '1':
      return False if found,
        and return True otherwise
    """
    # E.g.: [{'member': 0, 'user_id': 1646659}, {'member': 0, 'user_id': 214895},  ... ]
    for member in membership_obj_list:
        if member['member']:
            return False
    return True


def find_secret(identifier):
    """
    find source user's groups
    find his friends
    check if each friend is a member of the above mentioned groups
    for each group given:
      call groups.isMember using friends' UIDs
      get 1/0 response
      call group_is_private function with the above response as a single parameter:
        iterating through the given list, look for '1':
          return False if found,
        and return True otherwise

    """
    user_id = resolve_uid(identifier)

    # Get target user friends list
    friends_obj_list = do_request(URL_FRIENDS, user_id=user_id)['items']
    # Get target user groups list
    group_obj_list = do_request(
        URL_GROUPS,
        user_id=user_id,
        fields='members_count',
    )['items']

    friends = set()
    for friend in friends_obj_list:
        friends.add(str(friend['id']))

    secret_groups = []
    prog = ProgressBar(maxval=len(group_obj_list), poll=0, left_justify=False).start()
    for num, group_id in enumerate(group_obj_list):
        prog.update(num + 1)
        # print('Checking {}'.format(num + 1))
        membership_obj_list = do_request(
            URL_ARE_MEMBERS,
            group_id=group_id,
            user_ids=','.join(friends)
        )
        if group_is_private(membership_obj_list):
            secret_groups.append(group_id)
        time.sleep(0.5)

        # print(secret_groups)
    prog.finish()

    # Writing result
    filename = 'groups_answer.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(secret_groups, sort_keys=False))

    print('\nStep 1 is finished.\n\nStarting step 2...\n')

    group_obj_list = []
    prog = ProgressBar(maxval=len(secret_groups), poll=0, left_justify=False).start()
    for num, secret_group in enumerate(secret_groups):
        # print('Checking {} of {}'.format(num + 1, len(secret_groups)))
        prog.update(num + 1)
        group = do_request(
            URL_GROUP_ID,
            group_id=secret_group,
            fields='members_count',
        )[0]
        group_dict = {
            'name': group['name'],
            'gid': group['id'],
            'members_count': group['members_count'],
        }
        group_obj_list.append(group_dict)
        time.sleep(0.5)
    prog.finish()

    filename = 'groups_answer.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(group_obj_list, sort_keys=False,
                           indent=4, ensure_ascii=False, separators=(',', ': ')))

    print('Search results are written down - ', filename)
    print('Total were found', len(secret_groups), 'groups')


if __name__ == '__main__':
    find_secret(USER_ID)
