def enemyPrint(window, chararacter,characterDict):
    if  characterDict["damaged"]: 
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
    elif(chararacter == 'Brendan'):
        window.addstr("    o\n")
        window.addstr("  _/O\\_\n")
        window.addstr("   / \\        \n")
        window.addstr("  /   \\ \n")
    elif(chararacter == 'Max'):
        window.addstr("\n")
        window.addstr("    o\n")
        window.addstr("   /O\\        >\n")
        window.addstr("   / \\\n")
    elif(chararacter == "Mathias"):
        window.addstr("\n")
        window.addstr("\n")
        window.addstr(" \\_o_/       \n")
        window.addstr("  / \\ \n")
   

def playerPrint(window, character,characterDict):
    if characterDict["damaged"]: 
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
    elif(character == 'Brendan'):
        window.addstr("                     o\n")
        window.addstr("                   _/O\\_\n")
        window.addstr("                    / \\        \n")
        window.addstr("                   /   \\ \n")
    elif(character == 'Max'):
        window.addstr("\n")
        window.addstr("                     o\n")
        window.addstr("                    /O\\        \n")
        window.addstr("                    / \\\n")
    elif(character == "Mathias"):
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("                  \\_o_/       \n")
        window.addstr("                   / \\ \n")
