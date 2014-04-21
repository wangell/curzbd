#!/usr/bin/python

import CurzbdWindow

class HelpWindow(CurzbdWindow.CurzbdWindow):

    def __init__(self, stdscr):
        self.window = stdscr.derwin(2, 0)
        self.selected_item = 0
        self.headings = ["Filename", "Size", "Percent", "Status"]

    def update(self):
        q = fetch_queue()
        
    def fetch_queue(self):
        pass

    def display(self):

        maxy,maxx = self.window.getmaxyx()

        self.window.erase()
        self.window.addstr(round(maxy/2), round(maxx/2), "X {} Y {}".format(round(maxx/2),round(maxy/2)))
        self.window.noutrefresh()
