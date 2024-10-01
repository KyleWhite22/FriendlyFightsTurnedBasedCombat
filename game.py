import curses
window = curses.initscr() # Initialize the library. Returns a WindowObject which represents the whole screen.
window.keypad(True) # Escape sequences generated by some keys (keypad, function keys) will be interpreted by curses.
curses.cbreak() # Keys are read one by one. Also safer than curses.raw() because you can still interrupt a running script with hotkeys.
curses.noecho() # Prevent getch() keys from being visible when pressed. Echoing of input characters is turned off.

# Initialize colors.
curses.start_color() # Must be called if the programmer wants to use colors.
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
black = curses.color_pair(1)
white = curses.color_pair(2)

def display_menu(window):
    selectedIndex = 0

    while True:
        window.clear()
        window.addstr('Pick an option:\n', curses.A_UNDERLINE)

        for i in range(len(MENU_OPTIONS)):
            # Uncolored line number.
            window.addstr('{}. '.format(i + 1))
            # Colored menu option.
            window.addstr(MENU_OPTIONS[i] + '\n', black if i == selectedIndex else white)

        c = window.getch()

        if c == curses.KEY_UP or c == curses.KEY_LEFT:
            # Loop around backwards.
            selectedIndex = (selectedIndex - 1 + len(MENU_OPTIONS)) % len(MENU_OPTIONS)

        elif c == curses.KEY_DOWN or c == curses.KEY_RIGHT:
            # Loop around forwards.
            selectedIndex = (selectedIndex + 1) % len(MENU_OPTIONS)

        # If curses.nonl() is called, Enter key = \r else \n.
        elif c == curses.KEY_ENTER or chr(c) in '\r\n':
            # If the last option, exit, is selected.
            if selectedIndex == len(MENU_OPTIONS) - 1:
                curses.endwin() # De-initialize the library, and return terminal to normal status.    <-- Works without this on Windows, however in Linux you can't type in the terminal after exiting without this :P
                break

            window.addstr('\nYou choose {}\n'.format(MENU_OPTIONS[selectedIndex]))
            window.getch()

        else:
            window.addstr("\nThe pressed key '{}' {} is not associated with a menu function.\n".format(chr(c), c))
            window.getch()

MENU_OPTIONS = [
    '',
    '',
    '',
    '',
]

def startMenu(window):
    window.addstr("                           \n")
    window.addstr("                           \n")
    window.addstr("                           \n")
    window.addstr("                           Cream Fights\n")
    window.addstr("                           \n")





if __name__ == '__main__':
    startMenu(window)