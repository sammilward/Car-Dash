#Car Dash --- Programming Project 28/11/2016
#Avoid all oncoming vehicles and collect coins to increase score.



#Importing all the modules needed for the game to run
import pygame, random, time, os

#Retrieving the players name through reading the text file the TKinter file created
NameFile = open("PlayersNameFile.txt" , "r")
PlayersName = NameFile.read()
NameFile.close()
#Initialising PYGAME
pygame.init()
#Setting the screen dimensions
screenWidth = 450
screenHight = 600
#Initalising the first clock so that score can be calculated
FirstTime = time.time()
#Setting the colours
Black = (0,0,0)
#Setting up the display
GameScreen = pygame.display.set_mode((screenWidth, screenHight))
#Setting the title of the game
pygame.display.set_caption("Car Dash")
#Loads images
RedCar = pygame.image.load("RedCar.png")
YellowCar = pygame.image.load("YellowCar.png")
GreenCar = pygame.image.load("GreenCar.png")
BlueCar = pygame.image.load("BlueCar.png")
BackGround = pygame.image.load("Back.png")
RoadMarking = pygame.image.load("RoadMarkings.png")
Bush = pygame.image.load("Bush.png")
Coin = pygame.image.load("Coin.png")
GameOver = pygame.image.load("GameOver.png")
GameScreen.blit(BackGround, (0,0))
pygame.display.update()

#The movement of the lines in the road. Fixed X Val but Algorithm for Y (labeled z)
def DecorationMove(DecorationStartPoint):
        GameScreen.blit(RoadMarking, (114,DecorationStartPoint))
        GameScreen.blit(RoadMarking, (215,DecorationStartPoint))
        GameScreen.blit(RoadMarking, (321,DecorationStartPoint))
        GameScreen.blit(RoadMarking, (114,OtherMove))
        GameScreen.blit(RoadMarking, (215,OtherMove))
        GameScreen.blit(RoadMarking, (321,OtherMove))
        GameScreen.blit(Bush, (40,OtherMove))
        GameScreen.blit(Bush, (20,DecorationStartPoint))
        GameScreen.blit(Bush, (380,OtherMove))
        GameScreen.blit(Bush, (410,DecorationStartPoint))        

#Function to calculate the players score. Finds difference between two times
#Then puts the int value of the calculation in the top left hand of the screen
def Score(FirstTime, CoinCollected, AmountofCoins):
        ExtraPoints = 5
        if CoinCollected == True:
                AmountofCoins = AmountofCoins + 1 
        SecondTime = time.time()
        Score = ((SecondTime - FirstTime) + (AmountofCoins*ExtraPoints))
        font = pygame.font.SysFont(None, 25)
        text = font.render("Score: "+str(int(Score)), True, Black)
        GameScreen.blit(text, (10,10))
        return int(Score)

def DisplayHighScore(FirstPlace, SecondPlace, ThirdPlace):
    font = pygame.font.SysFont(None, 20)
    Title = font.render("High Scores", True, Black)
    FirstScore = font.render(str(FirstPlace), True, Black)
    SecondScore = font.render(str(SecondPlace), True, Black)
    ThirdScore = font.render(str(ThirdPlace), True, Black)

    GameScreen.blit(Title, (365,10))
    GameScreen.blit(FirstScore, (365,25))
    GameScreen.blit(SecondScore, (365,40))
    GameScreen.blit(ThirdScore, (365,55))

#Function to Save the players name and score. First assigns a string to Textline
#Then opens and appends the variable textline to the end of the text file.
def SaveScore(Name, Score):
        TextLine = str(Name) + "," + str(Score) + "\n"
        HighScoresFile = open("HighScores.txt", "a")
        HighScoresFile.write(TextLine) 
        HighScoresFile.close()
        
#A function that retrieves the high score from the textfile
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
    HighScoreFile.close()
    #Creates variables for the new sorted file. Uses , for split and \n for newline
    sortFirst = FirstName + "," + str(FirstScore) +"\n"
    sortSecond = SecondName + "," + str(SecondScore)+"\n"
    sortThird = ThirdName + "," + str(ThirdScore)+"\n"
    SortHighScores(sortFirst, sortSecond, sortThird)
    return First, Second, Third


def SortHighScores(First, Second, Third):
        #open file write mode to remove any information currently held in the file
        HighScoreFile = open("HighScores.txt", "w")
        #Writes the top three high scores to the file
        HighScoreFile.write(First)
        HighScoreFile.write(Second)
        HighScoreFile.write(Third)
        #Closes the file
        HighScoreFile.close()
        
#Increment of count, changes the speed of the y axis change        
def SpeedIncrement(count):
        if count < 2:
                count = count + 0.01
        if count < 8:  
                count = count + 0.0005
        else:
                count = count + 0.0000000000000001
        return count

def ResetHighScores():
        HighScoresFile = open("HighScores.txt", "w")
        for i in range(0,3):
                HighScoresFile.write("N/A 0 \n")

#Places the players red car on the screen
def FriendlyCar (LaneCoord,PlayersYval):
        GameScreen.blit(RedCar, (LaneCoord,PlayersYval))

#This function chooses a random number that will later select the lane of the car
#that has just spawned at the top of the window
def RandomLane():
        FirstCarLane = random.randint(0,2)
        CoinLane = random.randint(0,2)

        while FirstCarLane == CoinLane:
                CoinLane = random.randint(0,2)
        
        return FirstCarLane, CoinLane

#This function produces a random number which will then determine the colour of
#the new car being spawned
def WhichCar():
        CarType = random.randint(0,2)
        
        if CarType == 0:
                Car = YellowCar
        elif CarType == 1:
                Car = GreenCar
        elif CarType == 2:
                Car = BlueCar
        return Car

#Sets the x coord of the car based on RandomLane value and then places the
#car on to the window. Also returns OtherCarLane 
def OtherCars(yAxis, LaneNo, Car):
        if LaneNo == 0:
                OtherCarLane = 97.5
        elif LaneNo == 1:
                OtherCarLane = 198.5
        elif LaneNo == 2:
                OtherCarLane = 305.5
        GameScreen.blit(Car, (OtherCarLane,yAxis))
        return OtherCarLane

def SpawnCoin(yaxis, LaneNo, Coin, AlreadyCollected):
        Adjustment = 10
        if LaneNo == 0:
                CoinLane = 97.5 + Adjustment
        elif LaneNo == 1:
                CoinLane = 198.5 + Adjustment
        elif LaneNo == 2:
                CoinLane = 305.5 + Adjustment

        if AlreadyCollected == False:
                GameScreen.blit(Coin, (CoinLane,yaxis+Adjustment-3))

#This Function tests if the players car and the other car has collided
#This is done by comparison of the lanes the cars are in and the height of the cars
def TestCrash(PlayersLane, OtherCarVertical, OtherCarLane):
        if PlayersLane == OtherCarLane and int(OtherCarVertical) < 525 and int(OtherCarVertical) > 442 :
                gameExit = True
                return gameExit
                
def CoinCollection(PlayersLane, CoinVertical, CoinLane):
        CoinXAxis = 0
        if CoinLane == 0:
            CoinXAxis = 97.5
        elif CoinLane == 1:
            CoinXAxis = 198.5
        elif CoinLane == 2:
            CoinXAxis = 305.5

        if AlreadyCollected == False:
                if PlayersLane == CoinXAxis and int(CoinVertical) < 525 and int(CoinVertical) > 480:
                                Collected = True
                                return Collected

                        
#Telling the game it has not crashed to start
gameExit = False
#Initalising Variables to start off
count = 0
LaneNo, CoinLane = RandomLane()
PlayersCarLane = 198.5
PlayersVerticalVal = 500
DecorationStartPoint = 300
OtherMove = 0
Car = YellowCar
AmountofCoins = 0 
AlreadyCollected = False
#Call Function to get the high Scores
FirstPlace, SecondPlace, ThirdPlace = GetHighScores() 
DisplayHighScore(FirstPlace, SecondPlace, ThirdPlace)

#This is the main game loop and will continue to run untill player crashes
while gameExit == False:
        #Lets user quit the game using the red cross in the top corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #If a key is pressed down, left key move a lane to the left, right move a lane to the right
        if event.type == pygame.KEYDOWN:
            if PlayersCarLane == 198.5:
                if event.key == pygame.K_LEFT:
                    PlayersCarLane = 97.5
                elif event.key == pygame.K_RIGHT:
                    PlayersCarLane = 305.5

            elif PlayersCarLane == 97.5:
                if event.key == pygame.K_UP: 
                    PlayersCarLane = 198.5

            elif PlayersCarLane == 305.5:
                if event.key == pygame.K_UP:
                    PlayersCarLane = 198.5
        
        #Count is calculated by the result of the function SpeedIncrement
        count = SpeedIncrement(count)
        #DecorationStartPoint is the y axis value of the decorations(Roadmarkings and the bushs)
        #When the Y value gets so high it is set to 0 to be increased again
        DecorationStartPoint = DecorationStartPoint + count
        if DecorationStartPoint > 590:
                DecorationStartPoint = 0
        #This is the algorithm to increment OtherMove. This variable is the y axis
        #For the other cars and some decoration. When it reaches 590 function LaneNo
        #and WhichCar are called
        OtherMove = OtherMove + count
        if OtherMove > 590:
                OtherMove =0
                LaneNo, CoinLane = RandomLane()
                AlreadyCollected = False
                Car = WhichCar()
        #Build and show the background to cover the previous frame        
        GameScreen.blit(BackGround, (0,0))
        #Call DecorationMove with the parameter DecorationStartPoint
        DecorationMove(DecorationStartPoint)
        #Calls the FriendlyCar Function with parameters PlayersCarLane and PlayersVerticalVal
        FriendlyCar(PlayersCarLane,PlayersVerticalVal)
        #Assigns value to OtherCarLane from the return of OtherCars function
        OtherCarLane = OtherCars(OtherMove, LaneNo, Car)
        #Assigns a value to the varable PlayerScore whilst also running the function
        #score with FirstTime as a parameter
        PlayerScore = Score(FirstTime, CoinCollection(PlayersCarLane, OtherMove, OtherCarLane), AmountofCoins)
        SpawnCoin(OtherMove, CoinLane, Coin, AlreadyCollected)
        DisplayHighScore(FirstPlace, SecondPlace, ThirdPlace)
        #Updates the display
        pygame.display.update()
        #Call function to see if a coin has been collected
        if CoinCollection(PlayersCarLane, OtherMove, CoinLane) == True:
                AlreadyCollected = True
                AmountofCoins = AmountofCoins + 1
                Score(FirstTime, CoinCollection(PlayersCarLane, OtherMove, CoinLane), AmountofCoins)
        #If TestCrash returns True then stop the loop
        if TestCrash(PlayersCarLane, OtherMove, OtherCarLane) == True:
                SaveScore(PlayersName, PlayerScore)
                GetHighScores()
                GameScreen.blit(GameOver, (80,200))
                pygame.display.update()
                time.sleep(2)
                gameExit = True
#Calls the function SaveScore to store PlayersName and PlayerScore to a textfile
pygame.quit()
os.system('StartUp.py')
#Save .pyw to stop console window from appearing
