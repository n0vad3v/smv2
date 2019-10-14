#!/usr/bin/env python3
import requests
import sys
import os
import json
import configparser
from terminaltables import SingleTable

smms_endpoint = "https://sm.ms/api/v2/upload/"
smms_profile_endpoint = "https://sm.ms/api/v2/profile/"
smms_upload_history_endpoint = "https://sm.ms/api/v2/upload_history/"

"""
Upload image to sm.ms with/out token.
"""
def upload(image_path, smms_api_token=None):
    image_filename = os.path.basename(image_path)
    multipart_form_data = {
        'smfile': (image_filename, open(image_path, 'rb')),
    }
    if smms_api_token is None:
        print("Upload without Token.")
        r = requests.post(smms_endpoint, files=multipart_form_data)
    else:
        print("Upload with Token:" + smms_api_token)
        headers = {
            'Authorization': smms_api_token
        }
        r = requests.post(smms_endpoint, files=multipart_form_data, headers=headers)
    json_content = json.loads(r.text)
    if json_content['success']:
        return draw_upload_status_table(json_content)
    else:
        return "Something went wrong, info as follows: " + json_content['message']

"""
Get user profile.
"""
def get_profile(smms_api_token):
    headers = {
        'Authorization': smms_api_token
    }
    r = requests.post(smms_profile_endpoint, headers=headers)
    json_content = json.loads(r.text)
    return draw_profile_table(json_content)

"""
Visualize the user history JSON response by SM.MS.
"""
def draw_profile_table(json_response):
    j = json_response
    data = [
        ['username', j['data']['username']],
        ['Role', j['data']['role']],
        ['Group Expire Time', j['data']['group_expire']],
        ['Disk Usage', j['data']['disk_usage']],
        ['Disk Limit', j['data']['disk_limit']],
    ]
    table_instance = SingleTable(data, 'SM.MS User Profile')
    table_instance.inner_row_border = True
    return table_instance.table


"""
Get user upload history.
"""
def get_upload_history(smms_api_token):
    headers = {
        'Authorization': smms_api_token
    }
    r = requests.get(smms_upload_history_endpoint, headers=headers)
    json_content = json.loads(r.text)
    return draw_user_history_table(json_content)

"""
Visualize the user history JSON response by SM.MS.
"""
def draw_user_history_table(json_response):
    j = json_response
    data = []
    title_line = ['Image URL','Delete URL']
    data.append(title_line)
    for item in j['data']:
        picture_item = []
        picture_item.append(item['url'])
        picture_item.append(item['delete'])
        data.append(picture_item)
    table_instance = SingleTable(data, 'SM.MS User History')
    table_instance.inner_row_border = True
    return table_instance.table


"""
Visualize the upload JSON response by SM.MS.

Example:

{'success': True,
'code': 'success',
'message': 'Upload success.',
'data': {'file_id': 0,
        'width': 1350,
        'height': 449,
        'filename': 'ccc.jpg',
        'storename': 'hHt4IcpxNXo5TdS.jpg',
        'size': 141115,
        'path': '/2019/08/03/hHt4IcpxNXo5TdS.jpg',
        'hash': 'u3dpSRFMslx7PAZNGTCQjYL4r6',
        'url': 'https://i.loli.net/2019/08/03/hHt4IcpxNXo5TdS.jpg',
        'delete': 'https://sm.ms/delete/u3dpSRFMslx7PAZNGTCQjYL4r6',
        'page': 'https://sm.ms/image/hHt4IcpxNXo5TdS'},
'RequestId': 'FD6277E3-F2AB-4762-A575-21A7600D5BEA'}
"""
def draw_upload_status_table(json_response):
    j = json_response
    data = [
        ['Image URL', j['data']['url']],
        ['Deletion URL', j['data']['delete']],
    ]
    table_instance = SingleTable(data, 'SM.MS Upload Status')
    table_instance.inner_row_border = True
    return table_instance.table


def exe_main():
    if len(sys.argv) < 2:
        sys.exit("Missing argument, you should run with 'smv2 /path/to/image' to upload images and 'smv2 history' to show image history when API Token is supplied.")

    config_path = os.path.expanduser('~') + '/.smms'
    config = configparser.ConfigParser()
    """
    In case of looking up upload history.
    """
    if sys.argv[1] == "history":
        try:
            config.read(config_path)
            smms_api_token = config['sm.ms']['api_token']
            t = get_upload_history(smms_api_token)
            print(t)
        except:
            sys.exit("Missing API Token in '~/.smms'")
    elif sys.argv[1] == "profile":
        try:
            config.read(config_path)
            smms_api_token = config['sm.ms']['api_token']
            t = get_profile(smms_api_token)
            print(t)
        except:
            sys.exit("Missing API Token in '~/.smms'")
    else:
        send_file = sys.argv[1]
        try:
            config.read(config_path)
            smms_api_token = config['sm.ms']['api_token']
            j = upload(send_file, smms_api_token)
        except:
            j = upload(send_file)
        print(j)


if __name__ == '__main__':
    exe_main()
