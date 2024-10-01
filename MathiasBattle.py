import time
from array import *
import streamlit as st
def MathiasIntro(window):
    #message= array(['I',' ','g'])
    message=["H","e","y"]
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
        window.addstr("\n")
        window.addstr("                  \\_o_/       \n")
        window.addstr("                   / \\ \n")
        window.addstr("\n")
        window.addstr("  Mathias: ")
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
        flush_input()      
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
        window.addstr("\n")
        window.addstr("\n")
        window.addstr("                  \\_o_/       \n")
        window.addstr("                   / \\ \n")
        window.addstr("\n")
        window.addstr("  Mathias: ")
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
        flush_input()      
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
        window.addstr("               Level 2: Mathias\n")
        window.addstr("                   \n")
        window.addstr("                   Aptive Tower        \n")
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