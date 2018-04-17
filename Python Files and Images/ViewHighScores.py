from tkinter import *
import sys, os
root = Tk()
#root.title("View High Scores") #Poss
app = Frame(root)
app.grid()

def MainMenuClick():
    root.withdraw()
    os.system('StartUp.py')
    

def GetHighScores():
    #Open the file in read mode
    HighScoreFile = open("HighScores.txt", "r")
    #Initalise the big list of all scores
    AllScores = []
    #loop through the file one line at a time 
    for line in HighScoreFile:
            #initalise the name and score list
            NameAndScore = []
            #Assign a value to name and score, split the textline with a comma
            Name, Score = map(str, line.split(","))
            #Add the name to the NameAndScore list
            NameAndScore.append(Name)

            #Add the interger of the score to NameandScore list
            NameAndScore.append(int(Score))
            #Add the NameAndScore list to the AllScores list
            AllScores.append(NameAndScore)
    #Assign the sorted version of AllScores to NewList
    Newlist = sorted(AllScores, key=lambda NameAndScore: NameAndScore[1], reverse=True)
    #Assign the first value of the new list to FirstList
    Firstlist = Newlist[0]
    #Assign second value of Newlist to Secondlist
    Secondlist = Newlist[1]
    #Assign the third value of newlist to ThirdList
    Thirdlist = Newlist[2]
    #Assign names and scores to set variables
    FirstName, FirstScore, SecondName, SecondScore, ThirdName, ThirdScore = Firstlist[0], Firstlist[1], Secondlist[0], Secondlist[1], Thirdlist[0], Thirdlist[1]
    #Create variables that contain the name and score of the high scores
    First = FirstName + " " + str(FirstScore)
    Second = SecondName + " " + str(SecondScore)
    Third = ThirdName + " " + str(ThirdScore)
    return First, Second, Third
    HighScoresFile.close()

First = StringVar()
Second = StringVar()
Third = StringVar()
FirstScore, SecondScore, ThirdScore = GetHighScores()
First.set(FirstScore)
Second.set(SecondScore)
Third.set(ThirdScore)

TitleLabel = Label(app, text="HighScores")
TitleLabel.grid()
FirstLabel = Label(app, textvariable = First)
FirstLabel.grid()
SecondLabel = Label(app, textvariable = Second)
SecondLabel.grid()
ThirdLabel = Label(app, textvariable = Third)
ThirdLabel.grid()

MainMenuButton = Button(app, text = "Main Menu", command=MainMenuClick)
MainMenuButton.grid()

root.mainloop()
