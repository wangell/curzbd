#!/usr/bin/python

import curses
import QueueWindow, HistoryWindow, ConfigWindow, HelpWindow, Navbar
from SabnzbdApi import SabnzbdApi

class CurzbdInterface:
    
    def __init__(self, config_dic):
        self.config = config_dic
        self.sabnzbd = SabnzbdApi(self.config['Sabnzbd'])
        self.activeChanged = False

    def run(self):
        curses.wrapper(self.__setup)

    def __setup(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.nodelay(1)
        curses.init_color(curses.COLOR_WHITE, 1000, 1000, 1000)

        #Initialize colors
        for c in range(1, len(self.config['Colors'])):
            (c1,c2) = self.config['Colors']['ColorPair' + str(c)].split(',')
            curses.init_pair(c, int(c1), int(c2))

        #Hide cursor
        curses.curs_set(0)

        #Setup class members
        self.global_keys = { 
                '1' : self.activate_window,
                '2' : self.activate_window,
                '3' : self.activate_window,
                '4' : self.activate_window,
                'q' : self.quit_sequence
        }

        #Initialize windows
        self.construct_windows()
        self.activeWindow = 1

        self.__loop()

    def construct_windows(self):
        nav = Navbar.Navbar(self.stdscr)
        queueWindow = QueueWindow.QueueWindow(self.stdscr, self.sabnzbd)
        historyWindow = HistoryWindow.HistoryWindow(self.stdscr, self.sabnzbd)
        configWindow = ConfigWindow.ConfigWindow(self.stdscr)
        helpWindow = HelpWindow.HelpWindow(self.stdscr)

        self.windows = { 1 : queueWindow, 2 : historyWindow, 3 : configWindow, 4 : helpWindow }
        self.navbar = nav

    def __loop(self):

        while True:
            #Display
            self.windows[self.activeWindow].display()
            self.navbar.display(self.activeWindow)

            curses.doupdate()

            #Input
            try:
                key = self.stdscr.getkey()
            except:
                continue
            
            self.__process_input(key)

    def __process_input(self, key):
        if key in self.global_keys:
            self.global_keys[key](key)
        elif key == "KEY_RESIZE":
            self.construct_windows()
        else:
            self.windows[self.activeWindow].process_key(key)

    #Global Key functions
    def activate_window(self, key):
        if self.activeWindow != int(key):
            self.activeWindow = int(key)

    def quit_sequence(self, key):
        quit()
