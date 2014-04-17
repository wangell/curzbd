#!/usr/bin/python

import sys
import configparser
from CurzbdInterface import CurzbdInterface

def main():
    config = configparser.ConfigParser()
    config.read("curzbd.conf")

    app = CurzbdInterface(config)
    app.run()

if __name__ == "__main__":
    main()
