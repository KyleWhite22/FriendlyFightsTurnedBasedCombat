#!/usr/bin/env python3
from brendanBattle import *
from MathiasBattle import *
from characterPrints import playerPrint, enemyPrint
from moves import moveList
import curses
import pygame
from pygame.locals import *


window = curses.initscr() # Initialize the library. Returns a WindowObject which represents the whole screen.
window.keypad(True) # Escape sequences generated by some keys (keypad, function keys) will be interpreted by curses.
curses.cbreak() # Keys are read one by one. Also safer than curses.raw() because you can still interrupt a running script with hotkeys.
curses.noecho() # Prevent getch() keys from being visible when pressed. Echoing of input characters is turned off.

# Initialize colors.
curses.start_color() # Must be called if the programmer wants to use colors.
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)

black = curses.color_pair(1)
white = curses.color_pair(2)
green = curses.color_pair(3)
yellow = curses.color_pair(4)
red = curses.color_pair(5)

curses.curs_set(0)
def printMystery(window):
    window.addstr("\n")
    window.addstr("\n")
    window.addstr("\n")
    window.addstr("                    ???\n")
    window.addstr("          <        ?????        >\n")
    window.addstr("                    ???\n")
    window.addstr("\n")
    window.addstr("                    ???\n")

def printMax(window):
    window.addstr("\n")
    window.addstr("\n")
    window.addstr("\n")
    window.addstr("                     o\n")
    window.addstr("                    /O\\        >\n")
    window.addstr("                    / \\\n")
    window.addstr("\n")
    window.addstr("                    MAX\n")

def printBrendan(window):
    window.addstr("\n")
    window.addstr("\n")
    window.addstr("                     o\n")
    window.addstr("                   _/O\\_\n")
    window.addstr("          <         / \\        >\n")
    window.addstr("                   /   \\\n")
    window.addstr("\n")
    window.addstr("                  BRENDAN\n")

def printMathias(window):
    window.addstr("\n")
    window.addstr("\n")
    window.addstr("                     o\n")
    window.addstr("                   _/O\\_\n")
    window.addstr("          <         / \\        >\n")
    window.addstr("                   /   \\\n")
    window.addstr("\n")
    window.addstr("                   Mathias\n")



MAX = {
    'baseHP': 120,
    'currentHP': 120,
    'move1' : 'MeatBall Sub Slam',
    'move1Base' : 15,
    "move1Count" : 15,
    'move2': 'Genshin Blast',
    'move2Base': 3, 
    'move2Count' :3,
    'move3': 'Gax Tax',
    "move3Base" : 20,
    "move3Count" : 20,
    'move4': 'GrubHub',
    'move4Base' : 25,
    'move4Count' : 25,
    'damaged': False,
    'cashBase': 60,
    'cashCurrent' : 30,
    'defense': .90,
    'speed': 10,
    'strength' : 1.08,
    'defenseBase': .90,
    'speedBase': 10,
    'strengthBase' : 1.08,
    'grubHubChoice' : 0,
    'unlocked' : True,
}

GRUHUBNAMES = [
    "Wendys",
    "Savvy",
    "ShakeShack",
    "AppleBees"
]
GRUBHUB = {
    "WendyPrice" : 10,
    "WendyHP": 5,
    "SavvyPrice": 20,
    "SavvyHP": 15,
    "ShakeShackPrice": 40,
    "ShakeShackHP": 35,
    "AppleBeesPrice":  60,
    "AppleBeesHP": 100
}
BRENDAN = {
    'baseHP': 100,
    'currentHP': 100,
    'move1' : '800m Dash',
    'move1Base' : 15,
    "move1Count" : 15,
    'move2': 'CEO of Blue',
    'move2Base': 5, 
    'move2Count' :5,
    'move3': 'Chirp',
    "move3Base" : 15,
    "move3Count" : 15,
    'move4': 'Brooks Ghost',
    'move4Base': 1, 
    'move4Count' :1,
    'damaged': False,
    'defense': .98,
    'speed': 99,
    'strength' : 1.03,
    'defenseBase': .98,
    'speedBase': 99,
    'strengthBase' : 1.03,
    'ghost': False,
    'unlocked' : False,
}
BRENDANENEMY = {
    'baseHP': 100,
    'currentHP': 100,
    'move1' : '800m Dash',
    'move1Base' : 15,
    "move1Count" : 15,
    'move2': 'CEO of Blue',
    'move2Base': 5, 
    'move2Count' :5,
    'move3': 'Chirp',
    "move3Base" : 15,
    "move3Count" : 15,
    'move4': 'Brooks Ghost',
    'move4Base': 1, 
    'move4Count' :1,
    'damaged': False,
    'defense': .98,
    'speed': 99,
    'strength' : 1.03,
    'defenseBase': .98,
    'speedBase': 99,
    'strengthBase' : 1.03,
    'ghost': False,
}
MATHIAS = {
    'baseHP': 110,
    'currentHP': 110,
    'move1' : 'Debug',
    'move1Base' : 15,
    "move1Count" : 15,
    'move2': 'New Cut',
    'move2Base': 10, 
    'move2Count' :10,
    'move3': 'Aptivate Potential',
    "move3Base" : 20,
    "move3Count" : 20,
    'move4': 'Now You See Me 2',
    'move4Base': 15, 
    'move4Count': 15,
    'damaged': False,
    'defense': .90,
    'speed': 20,
    'strength' : 1.08,
    'defenseBase': .90,
    'speedBase': 20,
    'strengthBase' : 1.08,
    'unlocked' : False,
}
JUSTIN = {
    'baseHP': 110,
    'currentHP': 110,
    'move1' : 'Mario Kart Connoisseur ',
    'move1Base' : 10,
    "move1Count" : 10,
    'move2': 'Red Ball Throw',
    'move2Base': 15, 
    'move2Count' :15,
    'move3': 'Jersey Man',
    "move3Base" : 5,
    "move3Count" : 5,
    'move4': 'Peanut Butter',
    'move4Base': 10, 
    'move4Count' :10,
    'damaged': False,
    'defense': 1,
    'speed': 60,
    'strength' : 1.03,
    'defenseBase': .8,
    'speedBase': 60,
    'strengthBase' : 1.03,
    'jerseyMan' : False,
    'unlocked' : False,
}


def display_menu(window):
    selectedIndex = 0

    while True:
        window.refresh()
        window.clear()
        window.addstr('Pick an option:\n', curses.A_UNDERLINE)

        for i in range(len(MENU_OPTIONS)):
            # Uncolored line number.
            window.addstr('{}. '.format(i + 1))
            # Colored menu option.
            window.addstr(MENU_OPTIONS[i] + '\n', black if i == selectedIndex else white)
        flush_input()
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
            flush_input()
            window.getch()

        else:
            window.addstr("\nThe pressed key '{}' {} is not associated with a menu function.\n".format(chr(c), c))
            flush_input()
            window.getch()

MENU_OPTIONS = [
    'Option 1',
    'Option 2',
    'Option 3',
    'Exit',
]
MAP_OPTIONS = [
    'Bolz Hall',
    '???',
    '???',
    '???',
    '???',
    '???', 
]

def chooseChar(window):
    selectIndex = 0
    numChars = 6
    while True:
        window.refresh()
        window.clear()
        window.addstr("\n")     
        window.addstr("\n")            
        window.addstr("\n")             
        window.addstr("\n")             
        window.addstr("\n")
        if selectIndex == 0:
            printMax(window)
        elif selectIndex == 1:
            if BRENDAN['unlocked']== True:
                printBrendan(window)
            else:
                printMystery(window)
        elif selectIndex == 2:
            printMystery(window)
        elif selectIndex == 3:
            printMystery(window)
        elif selectIndex == 4:
            printMystery(window)
        elif selectIndex == 5:
            printMystery(window)
        elif selectIndex == 6:
            printMystery(window)
        window.addstr("\n")                               
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        flush_input()
        c = window.getch()
        if c == curses.KEY_RIGHT and selectIndex < numChars: 
            selectIndex = selectIndex + 1
        elif c == curses.KEY_LEFT and selectIndex !=0:
            selectIndex = selectIndex - 1
        elif c == curses.KEY_ENTER or chr(c) in '\r\n':
            if(selectIndex == 0):
                playerChar = 'Max'
            elif(selectIndex == 1):
                playerChar = 'Brendan'
            break
    map(window, playerChar)

def map(window, playerChar):
    selectedIndex = 0
    while True:
        window.refresh()
        window.clear()
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        if BRENDAN["unlocked"] == True:
            MAP_OPTIONS[1] = "Aptiv Tower"
        for i in range(len(MAP_OPTIONS)):
            # Uncolored line number.
            window.addstr('{}. '.format(i + 1))
            # Colored menu option.
            window.addstr(MAP_OPTIONS[i] + '\n', black if i == selectedIndex else white)
        flush_input()
        c = window.getch()

        if c == curses.KEY_UP or c == curses.KEY_LEFT:
            # Loop around backwards.
            selectedIndex = (selectedIndex - 1 + len(MAP_OPTIONS)) % len(MAP_OPTIONS)

        elif c == curses.KEY_DOWN or c == curses.KEY_RIGHT:
            # Loop around forwards.
            selectedIndex = (selectedIndex + 1) % len(MAP_OPTIONS)

        # If curses.nonl() is called, Enter key = \r else \n.
        elif c == curses.KEY_ENTER or chr(c) in '\r\n':
            # If the last option, exit, is selected.
            if selectedIndex == len(MAP_OPTIONS) - 1:
                curses.endwin() # De-initialize the library, and return terminal to normal status.    <-- Works without this on Windows, however in Linux you can't type in the terminal after exiting without this :P
                break
            if selectedIndex == 0:
                battle(window, playerChar, 'Brendan')
                break
            elif selectedIndex == 1 and MAP_OPTIONS[1] != "???":
                battle(window, playerChar, 'Mathias')
                break

        else:
            window.addstr("\nThe pressed key '{}' {} is not associated with a menu function.\n".format(chr(c), c))
            flush_input()
            window.getch()

def printChars(window, playerChar, enemyChar, enemyDict, playerDict):
        window.addstr('{}|hp: {:.2f}|\n'.format(enemyChar, max(enemyDict["currentHP"],0)))
        i = 0
        while i < enemyDict["currentHP"]:
            if enemyDict['currentHP'] >= (2/3) * enemyDict["baseHP"]:
                window.addstr("▬",green)
            elif enemyDict['currentHP'] >= (1/4) * enemyDict["baseHP"]:
                window.addstr("▬",yellow)
            else:
                window.addstr("▬",red)
            i = i + 10
        window.addstr("\n")
        enemyPrint(window,enemyChar,enemyDict)
        window.addstr("\n")
        playerPrint(window,playerChar,playerDict)
        window.addstr('                     {}|hp: {:.2f}|\n'.format(playerChar, max(playerDict["currentHP"],0)))
        window.addstr("                     ")
        i = 0
        while i < playerDict["currentHP"]:
            if playerDict['currentHP'] >= (2/3) * playerDict["baseHP"]:
                window.addstr("▬",green)
            elif playerDict['currentHP'] >= (1/4) * playerDict["baseHP"]:
                window.addstr("▬",yellow)
            else:
                window.addstr("▬",red)
            i = i + 10
        window.addstr("\n")

def printHud(window, playerChar, enemyChar, playerDict, enemyDict):
    selectedIndex = 0
    while True:
        window.refresh()
        window.clear()
        printChars(window, playerChar, enemyChar, enemyDict, playerDict)
        window.addstr(playerDict["move1"], black if 0 == selectedIndex else white)
        window.addstr(": {}/{}".format(playerDict["move1Count"],playerDict['move1Base']))
        spaces = 20 -len(playerDict["move1"])
        for i in range (0,spaces):
            window.addstr(" ")
        window.addstr(playerDict["move2"], black if 1 == selectedIndex else white)
        window.addstr(": {}/{}\n".format(playerDict["move2Count"],playerDict['move2Base']))
        window.addstr(playerDict["move3"], black if 2 == selectedIndex else white)
        window.addstr(": {}/{}".format(playerDict["move3Count"],playerDict['move3Base']))
        spaces = 20 -len(playerDict["move3"])
        for i in range (0,spaces):
            window.addstr(" ")
        window.addstr(playerDict["move4"], black if 3 == selectedIndex else white)
        window.addstr(": {}/{}".format(playerDict["move4Count"],playerDict['move4Base']))
        flush_input()
        c = window.getch()

        if c == curses.KEY_LEFT:
            # Loop around backwards.
            selectedIndex = (selectedIndex - 1 + len(playerDict)) % len(playerDict)
        elif c == curses.KEY_UP:
            selectedIndex = (selectedIndex - 2 + len(playerDict)) % len(playerDict)
        elif c == curses.KEY_DOWN:
            # Loop around forwards.
            selectedIndex = (selectedIndex + 2) % len(playerDict)
        elif c == curses.KEY_RIGHT:
            selectedIndex = (selectedIndex + 1) % len(playerDict)
 
        
        # If curses.nonl() is called, Enter key = \r else \n.
        elif c == curses.KEY_ENTER or chr(c) in '\r\n':
            if selectedIndex == 0 and playerDict['move1Count'] >0 :
                break
            elif selectedIndex == 1 and playerDict['move2Count'] >0 :
                break
            elif selectedIndex == 2 and playerDict['move3Count'] >0 :
                break
            elif selectedIndex == 3 and playerDict['move4Count'] >0 and playerChar== 'Max':
                choice = grubHubPreview(window, playerChar, enemyChar, enemyDict, playerDict)
                if choice == 0:
                    break
            elif selectedIndex == 3 and playerDict['move4Count'] >0 :
                break
            else:
                window.refresh()
            # If the last option, exit, is selected.
            if selectedIndex == len(playerDict) - 1:
                curses.endwin() # De-initialize the library, and return terminal to normal status.    <-- Works without this on Windows, however in Linux you can't type in the terminal after exiting without this :P
            
    return selectedIndex
def battle(window, playerChar, enemyChar):
    if enemyChar == 'Brendan':
        enemyDict = BRENDAN
        brendanIntro(window)
        pygame.mixer.music.load("IB.mp3")
        pygame.mixer.music.play()
    elif enemyChar == 'Mathias':
        enemyDict = MATHIAS
        MathiasIntro(window)
        pygame.mixer.music.load("FT.mp3")
        pygame.mixer.music.play()
    if playerChar == 'Max':
        playerDict = MAX
    elif playerChar == 'Brendan':
        playerDict = BRENDAN
    while enemyDict['currentHP'] > 0  and playerDict['currentHP'] > 0:
        selectedIndex = printHud(window, playerChar, enemyChar, playerDict, enemyDict)
        window.refresh()
        window.clear()
        printChars(window, playerChar, enemyChar, enemyDict, playerDict)
        window.refresh()  
        moveList(window, playerChar, playerDict, enemyChar, enemyDict, selectedIndex)
        flush_input()
        window.getch()
    if enemyDict['currentHP'] <= 0:
        if enemyChar == 'Brendan':
            BRENDAN['unlocked'] = True
        elif enemyChar == 'Mathias':
            MATHIAS['unlocked'] = True
        window.refresh()
        window.clear()
        window.addstr("\n")     
        window.addstr("\n")            
        window.addstr("\n")             
        window.addstr("\n")             
        window.addstr("\n")                
        window.addstr("\n")                  
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("                {} defeated!\n".format(enemyChar))
        window.addstr("\n")                          
        window.addstr("\n")                          
        window.addstr("\n")                           
        window.addstr("\n")                            
        window.addstr("\n")                               
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        flush_input()
        window.getch()
        window.refresh()
        window.clear()
        window.addstr("\n")     
        window.addstr("\n")            
        window.addstr("\n")             
        window.addstr("\n")             
        window.addstr("\n")                
        window.addstr("\n")                  
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("                {} now playable!\n".format(enemyChar))
        window.addstr("\n")                          
        window.addstr("\n")                          
        window.addstr("\n")                           
        window.addstr("\n")                            
        window.addstr("\n")                               
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        flush_input()
        window.getch()
    pygame.mixer.music.stop()
    resetDefaults(playerChar, playerDict)
    resetDefaults(enemyChar, enemyDict)
    window.refresh()
    window.clear()

def resetDefaults(playerChar, playerDict):
    playerDict['currentHP'] = playerDict['baseHP']
    playerDict['move1Count'] =  playerDict['move1Base']
    playerDict['move2Count'] =  playerDict['move2Base']
    playerDict['move3Count'] =  playerDict['move3Base']
    playerDict['move4Count'] =  playerDict['move4Base']
    playerDict['defense'] =  playerDict['defenseBase']
    playerDict['speed'] =  playerDict['speedBase']
    playerDict['strength'] =  playerDict['strengthBase']

    if playerChar == 'Max':
        playerDict['cashCurrent'] = playerDict['cashBase']
        playerDict['cashCurrent'] = playerDict['cashBase']
    elif playerChar == 'Brendan':
        playerDict['ghost'] = False
 

def grubHubPreview(window, playerChar, enemyChar, enemyDict, playerDict):
            selectedIndex = 0
            while True:
                window.refresh()
                window.clear()
                printChars(window, playerChar, enemyChar, enemyDict, playerDict)
                window.addstr("\n")
                window.addstr("                    Gax Cash:${}\n". format(playerDict['cashCurrent']))                       
                window.addstr("     ____________________________\n")             
                window.addstr("    |                            | \n") 
                for i in range(4):
                    window.addstr("    | ")
                    window.addstr(GRUHUBNAMES[i], black if i == selectedIndex else white)
                    if GRUHUBNAMES[i] == 'Wendys':
                        window.addstr(":     ${}/{}hp        |\n".format(GRUBHUB["WendyPrice"],GRUBHUB["WendyHP"]))
                        window.addstr("    |                            |\n")
                    elif GRUHUBNAMES[i] == 'Savvy':
                        window.addstr(":      ${}/{}hp       |\n".format(GRUBHUB["SavvyPrice"],GRUBHUB["SavvyHP"]))
                        window.addstr("    |                            |\n")
                    elif GRUHUBNAMES[i] == 'ShakeShack':
                        window.addstr(": ${}/{}hp       |\n".format(GRUBHUB["ShakeShackPrice"],GRUBHUB["ShakeShackHP"])) 
                        window.addstr("    |                            |\n")
                    elif GRUHUBNAMES[i] == "AppleBees":
                        window.addstr(":  ${}/100%hp     |\n".format(GRUBHUB["AppleBeesPrice"]))                               
                        window.addstr("    |____________________________|\n")
                        window.addstr("\n")
                window.addstr("Press 'x' to exit")
                flush_input()
                c = window.getch()
                
                if c == curses.KEY_UP or c == curses.KEY_LEFT:
                # Loop around backwards.
                    selectedIndex = (selectedIndex - 1 + 4) % 4

                elif c == curses.KEY_DOWN or c == curses.KEY_RIGHT:
                # Loop around forwards.
                    selectedIndex = (selectedIndex + 1) % 4
                # If curses.nonl() is called, Enter key = \r else \n.
                
                if chr(c) in 'x': 
                    return 1
                    

                elif c == curses.KEY_ENTER or chr(c) in '\r\n':

                    if selectedIndex == 0 and playerDict['cashCurrent'] >= GRUBHUB["WendyPrice"]:
                        break
                    elif selectedIndex == 1 and playerDict['cashCurrent'] >= GRUBHUB["SavvyPrice"]:
                        break
                    elif selectedIndex == 2 and playerDict['cashCurrent'] >= GRUBHUB["ShakeShackPrice"]:
                        break
                    elif selectedIndex == 3 and playerDict['cashCurrent'] >= GRUBHUB["AppleBeesPrice"]:
                        break
                     # De-initialize the library, and return terminal to normal status.    <-- Works without this on Windows, however in Linux you can't type in the terminal after exiting without this :P
                    else:
                        window.refresh()
                        window.addstr("\nNot enough Gax Cash!")
                        flush_input()
                        window.getch()
            playerDict['grubHubChoice'] = selectedIndex
            window.refresh()
            window.clear()
            return 0
    


def startScreen(window):
    while True:
        window.refresh()
        window.clear()
        window.addstr("\n")     
        window.addstr("\n")            
        window.addstr("\n")             
        window.addstr("\n")             
        window.addstr("\n")                
        window.addstr("\n")                  
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("                   CREAM FIGHTS\n")
        window.addstr("\n")                          
        window.addstr("                   >start game")                          
        window.addstr("\n")                           
        window.addstr("\n")                            
        window.addstr("\n")                               
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        flush_input()
        window.getch()
        break
def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    # import required modules

if __name__ == '__main__':
    pygame.mixer.init()
    pygame.mixer.music.load("smash.mp3")
    pygame.mixer.music.play()
    startScreen(window)
    while True:
        chooseChar(window)
        if BRENDAN["currentHP"] < 0:
            BRENDAN["unlocked"] = True
        BRENDAN["currentHP"] = BRENDAN["baseHP"]
        MAX["currentHP"] = MAX["baseHP"]
    #pygame.mixer.music.stop()
    display_menu(window)