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
        #self.window.clear()
        self.window.erase()
        self.window.addstr(0, 0, "Check")
        self.window.noutrefresh()
