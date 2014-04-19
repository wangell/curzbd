#!/usr/bin/python

import curses
import CurzbdWindow

class Navbar(CurzbdWindow.CurzbdWindow):

    def __init__(self, stdscr):
        self.window = stdscr.derwin(1, 80, 0, 0)
        self.links = ["1: Queue", "2: History", "3: Config", "4: Help"]
        self.spacing = 5

    def update(self, active_window):
        total = 0
        for x in range(0, len(self.links)):
            if active_window == (x+1):
                self.window.addstr(0, total, self.links[x], curses.color_pair(2))
            else:
                self.window.addstr(0, total, self.links[x], curses.color_pair(1))
            for y in range(0, self.spacing):
                self.window.addstr(" ")
            total += self.spacing + len(self.links[x])
        
    def fetch_queue(self):
        pass

    def display(self, active_window):
        self.update(active_window)
        #self.window.touchwin()
        self.window.noutrefresh()
