#!/usr/bin/python

import CurzbdWindow

class ConfigWindow(CurzbdWindow.CurzbdWindow):

    def __init__(self, stdscr):
        self.selected_item = 0
        self.headings = ["Filename", "Size", "Percent", "Status"]
        self.stdscr = stdscr

        self.construct_window()

    def update(self):
        q = fetch_queue()
    
    def construct_window(self):
        self.window = self.stdscr.derwin(2, 0)
        
    def fetch_queue(self):
        pass

    def display(self):
        self.window.erase()
        self.window.addstr(0, 0, "This")
        self.window.refresh()
