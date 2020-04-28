#! /usr/bin/python

import curses

def main(stdscr):
    stdscr.clear()

    # Code goes here
    new_window = curses.newwin(10, 20, 7, 20)
    new_window.addstr(5, 5, 'Hello, world')
    new_window.refresh()
    new_window.getkey()

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
