#!/usr/bin/python

import curses
import CurzbdWindow

class HistoryWindow(CurzbdWindow.CurzbdWindow):

    def __init__(self, stdscr, sab):
        self.sabnzbd = sab
        self.window = stdscr.derwin(2, 0)
        self.selected_index = 0
        self.headings = ["Status", "Filename", "Size", "Percent"]

    def update(self):
        (maxY,maxX) = self.window.getmaxyx()

        history = self.sabnzbd.history_output([])["history"]
        self.queued = history["slots"]

        self.window.addstr(0, 0, "Status")
        self.window.addstr(0, 15, "Filename")
        self.window.addstr(0, 65, "Size")

        x = 1
        index = 0
        for q in history["slots"][:24]:
            if self.selected_index == index:
                self.window.addstr(x, 0, q["status"], curses.color_pair(3))
                self.window.addstr(x, 15, q["name"][:40], curses.color_pair(3))
                self.window.addstr(x, 65, q["size"], curses.color_pair(3))
            else:
                self.window.addstr(x, 0, q["status"])
                self.window.addstr(x, 15, q["name"][:40])
                self.window.addstr(x, 65, q["size"])
            x += 1
            index += 1

    def fetch_queue(self):
        pass

    def display(self):
        self.window.erase()
        self.update()
        self.window.noutrefresh()

    def process_key(self, key):
        if key == "KEY_DOWN":
            if self.selected_index < len(self.queued) - 1:
                self.selected_index += 1
            else:
                self.selected_index = 0
        if key == "KEY_UP":
            if self.selected_index > 0:
                self.selected_index -= 1
            else:
                self.selected_index = len(self.queued) - 1
