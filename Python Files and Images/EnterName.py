from tkinter import *
import sys, os
root = Tk()
root.title("Play Game")
app = Frame(root)
app.grid()

def PlayClick():
    PlayersName = str(InputBox.get())
    if len(PlayersName) == 3:
        for Char in PlayersName:
            if (ord(Char)>= 65 and ord(Char) <= 90) or (ord(Char) >=97 and ord(Char) <=122):
                Valid = True
            else:
                Valid = False
                break
            
        if Valid == True:
            WriteName(PlayersName.upper())
            root.withdraw()
            os.system('OfficialProj.py')
            quit()
        else:
            #Run error window explaining 3 letter required length
            Title = Label(app, text = "Enter 3 letters as a name/initals", fg = 'red')
            Title.grid(row = 0, columnspan = 2)
    else:
        #Run error window explaining 3 letter required length
        Title = Label(app, text = "Enter 3 letters as a name/initals", fg = 'red')
        Title.grid(row = 0, columnspan = 2)
        
    
def Back():
    root.withdraw()
    os.system('StartUp.py')
    quit()

def WriteName(Name):
    PlayersNameFile = open("PlayersNameFile.txt", "w")
    PlayersNameFile.write(Name)
    PlayersNameFile.close()

Title = Label(app, text = "Enter 3 letters as a name/initals")
Title.grid(row = 0, columnspan = 2)

InputBox = Entry(app)
InputBox.grid(row = 1, column = 0)

PlayButton = Button(app, text = "Play Game!", command = PlayClick)
PlayButton.grid(row = 1, column = 1)

mainButton = Button(app, text = "Back to Main Menu", command = Back)
mainButton.grid(row = 2 , columnspan = 2, padx = 10)

root.mainloop()


#row = 0, column = 0
#row = 1, column = 0
#row = 1, column = 1
