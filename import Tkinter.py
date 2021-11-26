from tkinter import *


def startNav():
    #shortest path s-t
    #redisplay path
    print("starting nav")

def step1():
    print("step 1")
def step10():
    print("step 10")
def step100():
    print("step 100")
def step1000():
    print("step 1000")


gui = Tk(className = "iMaps - COP3530 Graph Project\tEvan & Chaitra")
# Code to add widgets will go here...
descript_label = Label(gui, text = "Welcome to iMaps created by Evan & Chaitra!\nThis navigation app uses a road network of\nthe United States and gives the fastest route\nfrom any two points. Enter a location\n(number 1-129163) to start and end navigation\nthen click \"Start Navigation\". Step through\neach direction using the buttons below.", bg="#e33939", font=("Courier", 16), width = 46, height = 9)
descript_label.place(x=20, y=20)
my_label = Label(gui, text = "Step through navigation\n (step size)", bg="#e33939", font=("Courier", 26), width = 28, height = 2)
my_label.place(x=20, y=460)
gui.geometry("1280x720")
startNav_button = Button(gui, command = startNav, text = "Start Navigation",font=("Courier", 26), bg="#61aaed", width = 28, height = 2)
startNav_button.place(x=20, y=340)
step1_button = Button(gui, command = step1, text = "  1 step  ",font=("Courier", 20), bg="#61aaed", width = 7, height = 2)
step1_button.place(x=20, y=560)
step10_button = Button(gui, command = step10, text = " 10 step ",font=("Courier", 20), bg="#61aaed", width = 8, height = 2)
step10_button.place(x=150, y=560)
step100_button = Button(gui, command = step100, text = " 100 step ",font=("Courier", 20), bg="#61aaed", width = 9, height = 2)
step100_button.place(x=295, y=560)
step1000_button = Button(gui, command = step1000, text = "1000 step",font=("Courier", 20), bg="#61aaed", width = 9, height = 2)
step1000_button.place(x=455, y=560)
gui.mainloop()



