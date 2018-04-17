from tkinter import *
import sys, os

root = Tk()
root.title("High Score Reset")

app = Frame(root)
app.grid()

label = Label(app, text = "Are you sure you want to reset the high scores", wraplength = 160)
label.grid(columnspan = 2)

def YesClick():
    ResetHigh()
    DisplayExtra()

def NoClick():
    root.withdraw()
    os.system('StartUp.py')
    quit()

def ResetHigh():
    Highscores = open("Highscores.txt", "w")
    for i in range (1, 4):
            Highscores.write("N/A,0 \n")
    Highscores.close()

def DisplayExtra():
    Message = Label(app, text = "High Scores have been reset", wraplength =150, fg = 'red') 
    Message.grid(row=2,columnspan =2)
    MainButton = Button(app,text="MainMenu",command = NoClick)
    MainButton.grid(row=3,columnspan=2)
    MainButton.config(width=22)

    
NoButton = Button(app, text = "NO", command = NoClick)
NoButton.grid(row = 1, column = 0)
NoButton.config(width = 10 )

YesButton = Button(app, text = "YES", command = YesClick, fg='red')
YesButton.grid(row=1,column=1)
YesButton.config(width = 10 )

root.mainloop()
