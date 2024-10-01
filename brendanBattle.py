import time
from array import *
import streamlit as st
def brendanIntro(window):
    #message= array(['I',' ','g'])
    message=["I", " ", "g", "u", "e", "s","s"," ", "w","e"," ", "h","a","v","e"," ","t","o", " ", "f", "i", "g", "h","t",".",".","."]
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
        window.addstr("                     o\n")
        window.addstr("                   _/O\\_\n")
        window.addstr("                    / \\        \n")
        window.addstr("                   /   \\ \n")
        window.addstr("\n")
        window.addstr("  Brendan: ")
        window.refresh()
        time.sleep(.2)
        window.addstr("H")
        window.refresh()
        time.sleep(.2)
        window.addstr("e")
        window.refresh() 
        time.sleep(.2)
        window.addstr("y")
        window.refresh()  
        time.sleep(.2)
        window.addstr(" ")
        window.refresh()  
        time.sleep(.2)
        window.addstr("m")
        window.refresh()
        time.sleep(.2)
        window.addstr("a")
        window.refresh()  
        time.sleep(.2)
        window.addstr("n.\n")
        window.refresh()                             
        window.addstr("\n")                               
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        window.getch()
        break
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
        window.addstr("                     o\n")
        window.addstr("                   _/O\\_\n")
        window.addstr("                    / \\        \n")
        window.addstr("                   /   \\ \n")
        window.addstr("\n")
        window.addstr("  Brendan: ")
        i = 0
        while i < len(message):
            window.refresh()
            time.sleep(.1)
            window.addstr(message[i])
            i = i +1
        window.addstr("\n")
        
        window.addstr("\n")                               
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("\n")
        window.getch()
        break
    while True:
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
        window.addstr("               Level 1: Brendan\n")
        window.addstr("                   \n")
        window.addstr("                   Bolz Hall        \n")
        window.addstr("                   \n")
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