import json
import time
import requests

from datetime import datetime

__author__ = 'NjProVk'
__version__ = '0.0.1'


def Start(auth_key, world_file, time_sleep):
    list_world = []
    with open(world_file) as f:
        for add_in_list in f.read().split('\n'):
            if add_in_list:
                list_world.append(add_in_list)

    print(f'Load: {len(list_world)} world!')

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
               'origin': 'https://discord.com',
               'referer': 'https://discord.com/channels/@me',
               'content-type': 'application/json',
               'authorization': auth_key}

    while 1:
        for message_text in list_world:
            time.sleep(float(time_sleep))
            r = requests.patch('https://discord.com/api/v9/users/@me/settings',
                               json={"custom_status": {"text": message_text}},
                               headers=headers)


if __name__ == '__main__':
    print(f"Start: {datetime.now().strftime('%T')}\n\tGitHub: https://github.com/NjProVk")
    with open('./config.json') as config:
        config_data = json.load(config)

    Start(config_data['authorization'], config_data['World-file'], config_data['Time-sleep'])
