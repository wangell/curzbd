#!/usr/bin/python

import curses
import CurzbdWindow

class QueueWindow(CurzbdWindow.CurzbdWindow):

    def __init__(self, stdscr, sab):
        self.sabnzbd = sab
        self.window = stdscr.derwin(2, 0)
        self.selected_index = 0
        self.headings = ["Status", "Filename", "Size", "Percent"]
        self.sizes = [15, 30, 15, 10]

        #Heading percentages

    def update(self):
        (maxY,maxX) = self.window.getmaxyx()

        self.window.addstr(0, 0, "S")
        self.window.addstr(0, 3, "Filename")
        self.window.addstr(0, 48, "Size")
        self.window.addstr(0, 57, "Progess")
        self.window.addstr(0, 70, "Timeleft")

        self.queued = []
        
        sabout = self.sabnzbd.queue_output([])
        if "queue" in sabout:
            queue = sabout["queue"]
            self.queued = queue["slots"]

        x = 1
        index = 0
        for q in self.queued:
            if self.selected_index == index:
                self.window.addstr(x, 0, q["status"][:1], curses.color_pair(3))
                self.window.addstr(x, 3, q["filename"][:40], curses.color_pair(3))
                self.window.addstr(x, 48, q["size"], curses.color_pair(3))
                self.window.addstr(x, 57, q["percentage"] + "%", curses.color_pair(3))
                self.window.addstr(x, 70, q["timeleft"], curses.color_pair(3))
            else:
                self.window.addstr(x, 0, q["status"][:1])
                self.window.addstr(x, 3, q["filename"][:40])
                self.window.addstr(x, 48, q["size"])
                self.window.addstr(x, 57, q["percentage"] + "%")
                self.window.addstr(x, 70, q["timeleft"])
            x += 1
            index += 1

    def fetch_queue(self):
        pass

    def display(self):
        self.window.erase()
        self.update()
        #self.window.touchwin()
        self.window.noutrefresh()

    def process_key(self, key):
        if key == 'KEY_DOWN':
            if self.selected_index < len(self.queued) - 1:
                self.selected_index += 1
            else:
                self.selected_index = 0
        if key == 'KEY_UP':
            if self.selected_index > 0:
                self.selected_index -= 1
            else:
                self.selected_index = len(self.queued) - 1
