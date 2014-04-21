#!/usr/bin/python

import curses
import CurzbdWindow

class QueueWindow(CurzbdWindow.CurzbdWindow):

    def __init__(self, stdscr, sab):
        self.sabnzbd = sab
        self.padding = 5
        self.selected = 0
        self.stdscr = stdscr

        self.construct_window()

    def update(self):
        self.print_row(["Status", "Filename", "Size", "Progress", "Timeleft"], 0)

        q = self.fetch_queue()
        for s in range(0, min(len(q), self.maxY -1)):
            if s == self.selected:
                self.print_row(q[s], s+1, curses.color_pair(3))
            else:
                self.print_row(q[s], s+1)

    def construct_window(self):
        self.window = self.stdscr.derwin(2, 0)
        self.columns = [("Status",.05), ("Filename",.45), ("Size",.1), ("Progress",.1), ("Timeleft", .2)]
        self.maxY,self.maxX = self.window.getmaxyx()
        self.maxX -= (self.padding * len(self.columns))

    def fetch_queue(self):
        queue = self.sabnzbd.queue_output([])

        queue_filtered = []
        if "queue" in queue:
            for q in queue["queue"]["slots"]:
                temp_r = []
                temp_r.append(q["status"])
                temp_r.append(q["filename"])
                temp_r.append(q["size"])
                temp_r.append(q["percentage"] + "%")
                temp_r.append(q["timeleft"])
                queue_filtered.append(temp_r)

        return queue_filtered

    def print_row(self, row, y, attr=0):
        self.columns_size = map(lambda x: round(x[1]*self.maxX), self.columns)
        q = zip(row, self.columns_size)
        curX = 0
        for (row_element, size) in q:
            self.window.addstr(y, curX, row_element[:size], attr)
            curX += size + self.padding

    def display(self):
        self.window.erase()
        self.update()
        self.window.noutrefresh()

    def process_key(self, key):
        if key == 'KEY_DOWN':
            if self.selected < self.maxY - 1:
                self.selected += 1
            else:
                self.selected = 0
        if key == 'KEY_UP':
            if self.selected > 0:
                self.selected -= 1
            else:
                self.selected = self.maxY - 1
