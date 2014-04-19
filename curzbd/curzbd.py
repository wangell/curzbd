#!/usr/bin/python

import sys
import configparser
import os.path
from CurzbdInterface import CurzbdInterface

def main():
    config = configparser.ConfigParser()

    config_path = os.path.expanduser("~/.curzbd.conf")

    print(config_path)

    if os.path.isfile(config_path):
        try:
            config.read(config_path)
        except:
            print("Can't read config file")
            exit()
    else:
        create_default_config(config)

    app = CurzbdInterface(config)
    app.run()

def create_default_config(config):

    config['General'] = {}
    config['General']['RefreshRate'] = '15'

    config['Colors'] = {}
    config['Colors']['ColorPair1'] = '7,0'
    config['Colors']['ColorPair2'] = '6,0'
    config['Colors']['ColorPair3'] = '1,0'
    config['Colors']['ColorPair4'] = '0,1'
    config['Colors']['ColorPair5'] = '0,1'
    config['Colors']['ColorPair6'] = '0,1'

    config['Sabnzbd'] = {}
    config['Sabnzbd']['Host'] = 'localhost'
    config['Sabnzbd']['Port'] = '8080'
    config['Sabnzbd']['ApiKey'] = 'xxxxxxxxxxxxx'
    config['Sabnzbd']['HttpMethod'] = 'http'

    with open(os.path.expanduser('~/.curzbd.conf'), 'w') as conf:
            config.write(conf)

if __name__ == "__main__":
    main()
