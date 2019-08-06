#!/usr/bin/env python3
import requests
import sys
import os
import json
import configparser
from terminaltables import SingleTable

smms_endpoint = "https://sm.ms/api/v2/upload/"


def upload(image_path, smms_api_token=None):
    """
    Upload image to sm.ms with/out token.
    """
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
        return draw_status_table(json_content)
    else:
        return "Something went wrong, info as follows: " + json_content['message']


def draw_status_table(json_response):
    """
    Visualize the JSON response by SM.MS.
    
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
    j = json_response
    data = [
        ['Status', j['success']],
        ['Image URL', j['data']['url']],
        ['Deletion URL', j['data']['delete']],
    ]
    table_instance = SingleTable(data, 'SM.MS Upload Status')
    table_instance.inner_row_border = True
    return table_instance.table


def exe_main():
    if len(sys.argv) < 2:
        sys.exit("Missing file path, you should run with 'smv2 /path/to/image'.")
    else:
        send_file = sys.argv[1]
    config_path = os.path.expanduser('~') + '/.smms'
    config = configparser.ConfigParser()
    try:
        config.read(config_path)
        smms_api_token = config['sm.ms']['api_token']
        j = upload(send_file, smms_api_token)
    except:
        j = upload(send_file)
    print(j)


if __name__ == '__main__':
    exe_main()
