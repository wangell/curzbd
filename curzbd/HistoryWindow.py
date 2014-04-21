#!/usr/bin/python

import curses
import math
import CurzbdWindow

class HistoryWindow(CurzbdWindow.CurzbdWindow):

    def __init__(self, stdscr, sab):
        self.sabnzbd = sab
        self.selected = 0
        self.padding = 5
        self.stdscr = stdscr

        self.construct_window()

    def construct_window(self):
        self.window = self.stdscr.derwin(2, 0)
        self.maxY,self.maxX = self.window.getmaxyx()
        self.columns = [("Status",.2),("Filename",.6),("Size",.2)]
        self.maxX -= (self.padding * len(self.columns))

    def update(self):
        self.print_row(["Status", "Filename", "Size"], 0)

        q = self.fetch_queue()
        for s in range(0, min(len(q),self.maxY - 1)):
            if s == self.selected:
                self.print_row(q[s], s+1, curses.color_pair(3))
            else:
                self.print_row(q[s], s+1)

    def print_row(self, row, y, attr=0):
        self.columns_size = map(lambda x: round(x[1]*self.maxX), self.columns)
        q = zip(row, self.columns_size)
        curX = 0
        for (row_element, size) in q:
            self.window.addstr(y, curX, row_element[:size], attr)
            curX += size + self.padding

    def fetch_queue(self):
        history = self.sabnzbd.history_output([])["history"]

        history_filtered = []
        for s in history["slots"]:
            temp_r = []
            temp_r.append(s['status'])
            temp_r.append(s['name'])
            temp_r.append(s['size'])
            history_filtered.append(temp_r)

        return history_filtered

    def display(self):
        self.window.erase()
        self.update()
        self.window.noutrefresh()

    def process_key(self, key):
        if key == "KEY_DOWN":
            if self.selected < self.maxY - 1:
                self.selected += 1
            else:
                self.selected = 0
        if key == "KEY_UP":
            if self.selected > 0:
                self.selected -= 1
            else:
                self.selected = self.maxY

