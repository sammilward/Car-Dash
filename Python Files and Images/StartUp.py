from tkinter import *
import sys
import os

root = Tk()
#Setting the title of the frame
root.title("Car Dash Menu")
#Sets the size of the window
#root.geometry("450x600")


#Creating a frame
app = Frame(root)
app.grid()

label = Label(app, text="Welcome to Car Dash")
label.grid()

#Learning Buttons
def PlayGameClick():
    root.withdraw()
    os.system('EnterName.py')
    quit()

def ViewHighScoresClick():
    root.withdraw()
    os.system('ViewHighScores.py')
    quit()

def ResetHighScoresClick():
    root.withdraw()
    os.system('ConfirmReset.py')
    quit()

def InstructionsClick():
    root.withdraw()
    os.system('Instructions.py')
    
def ExitClick():
    quit()
    sys.exit()

    
PlayGameButton = Button(app, text = "Play game", command=PlayGameClick)
PlayGameButton.grid(row = 1, pady = 5)

ViewHighScoresButton = Button(app, text = "View High Scores", command=ViewHighScoresClick)
ViewHighScoresButton.grid(row = 2, pady = 5)

ResetHighScoresButton = Button(app, text = "Reset High Scores", command=ResetHighScoresClick)
ResetHighScoresButton.grid(row = 3, pady = 5)

InstructionsButton = Button(app, text= "Instructions", command=InstructionsClick)
InstructionsButton.grid(row = 4, pady = 5)

ExitButton = Button(app, text = "Exit", command=ExitClick)
ExitButton.grid(row = 5, pady = 5)

root.mainloop()
