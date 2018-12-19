import requests
import sys
import time
import json
import logging
from progressbar import ProgressBar

TOKEN = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'
VERSION = '5.92'
URL_FRIENDS = 'https://api.vk.com/method/friends.get'
URL_GROUPS = 'https://api.vk.com/method/groups.get'
URL_MEMBERS = 'https://api.vk.com/method/groups.getMembers'
URL_GROUP_ID = 'https://api.vk.com/method/groups.getById'
ERROR_MANY_REQ = 6

print('\nStep 1 is being started...\n')
progress = []


def progress_bar(fn):
    try:
        '' % fn()
    except:
        fn

    def wrapped():
        try:
            sys.stdout.write('')
            fn()
            sys.stdout.write('')
        except KeyboardInterrupt:
            sys.stdout.write('')

    progress.append(wrapped)
    return wrapped


@progress_bar
def current_bar():
    pbar = ProgressBar(maxval=50)
    for i in pbar((i for i in range(50))):
        time.sleep(0.01)


def params_vk(url, id):
    params = {'access_token': TOKEN, 'v': VERSION, 'fields': 'screen_name'}
    if url == URL_FRIENDS:
        params['user_id'] = id
        if not str(id).isdigit():
            params['screen_name'] = id
    else:
        params['group_id'] = id

    if (url == URL_GROUPS) or (url == URL_GROUP_ID):
        params['fields'] = 'members_count'
        try:
            for bar in progress: bar()
        except KeyboardInterrupt:
            sys.stdout('')
    return params


def error_check(fn):
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as err:
            logging.error('{}(*{}, **{}) failed {}'.format(
                function.__name__, repr(args), repr(kwargs), repr(err)))

    return wrapped


@error_check
def req_error(url, id):
    while True:
        message = requests.get(url, params_vk(url, id)).json()
        if 'error' in message.keys():
            if message['error']['error_code'] != ERROR_MANY_REQ:
                print('An unexpected error occurred: ', message['error']['error_msg'])
                break
        else:
            break
    return message


def find_secret():
    friends_list = req_error(URL_FRIENDS, user_id)['response']['items']
    group_names_list = req_error(URL_GROUPS, user_id)['response']['items']
    groups_list_qty = len(group_names_list)

    secret_result_list = []
    num = 0

    for i, group_id in enumerate(group_names_list):
        print('Checking {} of {}'.format(num, groups_list_qty))
        current_bar()
        num += 1
        friends_common_list = req_error(URL_MEMBERS, group_id)['response']['items']
        secret_group_flag = True
        for friend in friends_list:
            if friend in friends_common_list:
                secret_group_flag = False
                break
        if secret_group_flag:
            secret_result_list.append(group_id)

    print('\nStep 1 is successfully finished.\n\nStep 2 is being started...\n')

    group_names_list = []
    secret_group_list_qty = len(secret_result_list)
    num = 0
    for num, secret_group in enumerate(secret_result_list):
        print('Checking {} of {}'.format(num, secret_group_list_qty))
        num += 1
        group_dict = {}
        group = req_error(URL_GROUP_ID, secret_group)['response'][0]
        group_dict['name'] = group['name']
        group_dict['gid'] = group['id']
        group_dict['members_count'] = group['members_count']
        group_names_list.append(group_dict)

    filename = 'groups_answer.json'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(group_names_list, sort_keys=False,
                           indent=4, ensure_ascii=False, separators=(',', ': ')))
    print('Search results are written down - ', filename)
    print('Total were found', groups_list_qty, 'groups.')


if __name__ == '__main__':
    user_id = 171691064
    find_secret()
