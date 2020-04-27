#! /usr/bin/python

import curses

def main(stdscr):
    stdscr.clear()

    # Code goes here
    new_window = curses.newwin(10, 25, 7, 20)
    new_window.addstr(1, 1, 'Hello, world')
    stdscr.refresh()

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
