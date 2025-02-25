import webbrowser
import time
import keyboard
import os
import sys

def start():
    print("Welcome to Gris Launcher\n1 to Launch Program\n2 to Open Documentation\n3 to Check for Updates\nEnter to Exit")
    #global numinput
    el_input = input()
    checkinput(el_input)
    

def checkinput(numinput):
    if numinput == "1":
  
        mainprogram
    elif numinput == "2":
        print("Opening..")
        webbrowser.open_new_tab("https://example.com")
        start()
    elif numinput == "3":
        print("Please Stand By.")
        time.sleep(5)
        print("Contacting Server.")
        time.sleep(4)
        print("Error Contacting Server: 404")
        time.sleep(1)
        print("1 or Enter to Exit\n2 to Continue")
        theinput2 = input()
        if theinput2 == "2":
            start()
        elif theinput2 == "1":
            print("exiting")
        else:
            print("exiting")
    else:
        print("exiting")

def mainprogram():
    webbrowser.open("https://www.youtube.com/watch?v=ONiGWymnd1A")

start()