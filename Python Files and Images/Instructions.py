from tkinter import *
import sys, os
root = Tk()
root.title("Instructions")
app = Frame(root)
app.grid()

def MenuClick():
    root.withdraw()
    os.system('StartUp.py')

title = Label(app, text = "Instructions")

title.config(font=("Courier", 30))
title.grid()

File = open("Instructions.txt", "r")
Instructions = StringVar()
Instructions.set(File.read())


DisInst = Label(app, textvariable = Instructions, wraplength=200)
DisInst.config(font=("Courier", 10))
DisInst.grid()

MainButton = Button(app, text = "Return to main menu", command=MenuClick)
MainButton.grid(pady = 5)



root.mainloop()
