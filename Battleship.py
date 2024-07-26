# IF SHIP is hit value = 🔥 IF SHOT MISSES value = 💣 BASE SHIP value = 🚢 


#Battlship Main .py
import random
import os
import time
from colorama import Fore


def place_ships_randomly(playerGridY, gridSize, shipsLocationPlayer, shipsLocationBot, placePlayerRandom, gridY): #Randomly generates spots on the grid for the ship
    maxSize = gridSize - 1
    if placePlayerRandom == True:
        for i in range(2):

            while True:
                shipName = str(input("Enter ship name. ")).lower()
                if shipName in shipsLocationPlayer:
                    print("This name is already in use. Please retry")
                else:
                    break

            while True:
                try:
                    horix1 = random.randint(0, maxSize)
                    vertiy1 = random.randint(0, maxSize)
                    orientation = random.choice(['horizontal', 'vertical'])
                    if orientation == 'horizontal':
                        vertiy2 = vertiy1
                        if horix1 == 0:
                            horix2 = horix1 + 1
                        elif horix1 == maxSize:
                            horix2 = horix1 - 1
                        else:
                            plusOrMinus = random.randint(1,2) # 1 is plus 2 is minus
                            if plusOrMinus == 1:
                                horix2 = horix1 + 1
                            else:
                                horix2 = horix1 - 1

                    else:
                        horix2 = horix1
                        if vertiy1 == 0:
                            vertiy2 = vertiy1 + 1
                        elif vertiy1 == maxSize:
                            vertiy2 = vertiy1 - 1
                        else:
                            plusOrMinus = random.randint(1,2) # 1 is plus 2 is minus
                            if plusOrMinus == 1:
                                vertiy2 = vertiy1 + 1
                            else:
                                vertiy2 = vertiy1 - 1
                    for key, value in shipsLocationPlayer.items():
                        if value[0] == (horix1, vertiy1) or value[0] == (horix2, vertiy2) or value[1] == (horix1, vertiy1) or value[1] == (horix2, vertiy2): 
                            raise
                    break
                except:
                    None
            
            playerGridY[vertiy1][horix1] = "🚢"
            playerGridY[vertiy2][horix2] = "🚢"
            shipsLocationPlayer[shipName] = [(horix1, vertiy1), (horix2, vertiy2)]

        for i in range(2):
            shipName = str(i)
            while True:
                try:
                    horix1 = random.randint(0, maxSize)
                    vertiy1 = random.randint(0, maxSize)
                    orientation = random.choice(['horizontal', 'vertical'])
                    if orientation == 'horizontal':
                        vertiy2 = vertiy1
                        if horix1 == 0:
                            horix2 = horix1 + 1
                        elif horix1 == maxSize:
                            horix2 = horix1 - 1
                        else:
                            plusOrMinus = random.randint(1,2) # 1 is plus 2 is minus
                            if plusOrMinus == 1:
                                horix2 = horix1 + 1
                            else:
                                horix2 = horix1 - 1

                    else:
                        horix2 = horix1
                        if vertiy1 == 0:
                            vertiy2 = vertiy1 + 1
                        elif vertiy1 == maxSize:
                            vertiy2 = vertiy1 - 1
                        else:
                            plusOrMinus = random.randint(1,2) # 1 is plus 2 is minus
                            if plusOrMinus == 1:
                                vertiy2 = vertiy1 + 1
                            else:
                                vertiy2 = vertiy1 - 1
                    for key, value in shipsLocationBot.items():
                        if value[0] == (horix1, vertiy1) or value[0] == (horix2, vertiy2) or value[1] == (horix1, vertiy1) or value[1] == (horix2, vertiy2): 
                            raise
                    break
                except:
                    None

            shipsLocationBot[shipName] = [(horix1, vertiy1), (horix2, vertiy2)]

            print(shipsLocationBot)
            
            for key, value in shipsLocationBot.items():
                print(f'{value[0]} and {value[1]}')
            
    else:
        for i in range(2):
            shipName = str(i)
            while True:
                try:
                    horix1 = random.randint(0, maxSize)
                    vertiy1 = random.randint(0, maxSize)
                    orientation = random.choice(['horizontal', 'vertical'])
                    if orientation == 'horizontal':
                        vertiy2 = vertiy1
                        if horix1 == 0:
                            horix2 = horix1 + 1
                        elif horix1 == maxSize:
                            horix2 = horix1 - 1
                        else:
                            plusOrMinus = random.randint(1,2) # 1 is plus 2 is minus
                            if plusOrMinus == 1:
                                horix2 = horix1 + 1
                            else:
                                horix2 = horix1 - 1

                    else:
                        horix2 = horix1
                        if vertiy1 == 0:
                            vertiy2 = vertiy1 + 1
                        elif vertiy1 == maxSize:
                            vertiy2 = vertiy1 - 1
                        else:
                            plusOrMinus = random.randint(1,2) # 1 is plus 2 is minus
                            if plusOrMinus == 1:
                                vertiy2 = vertiy1 + 1
                            else:
                                vertiy2 = vertiy1 - 1
                    for key, value in shipsLocationBot.items():
                        if value[0] == (horix1, vertiy1) or value[0] == (horix2, vertiy2) or value[1] == (horix1, vertiy1) or value[1] == (horix2, vertiy2): 
                            raise
                    break
                except:
                    None
                    
            shipsLocationBot[shipName] = [(horix1, vertiy1), (horix2, vertiy2)]


def place_ships_manually(playerGridY, maxSize, shipsLocation): #player places ships
    for x in range(1,3):
        ship_size = 2
        print(f"Placing ship of size {ship_size}")

        while True:
                shipName = str(input("Enter ship name. ")).lower()
                if shipName in shipsLocation:
                    print("This name is already in use. Please retry")
                else:
                    break
        # Make sure input isnt seperated weridly and make it flow better
        while True:
            try:
                print(f"This is for ship {x}")
                horix1 = int(input(f"Please enter the column coordinate (1 - {maxSize}) for ship {shipName} "))
                if horix1 < 1 or horix1 > maxSize:
                    print("hori1")
                    raise ValueError
                vertiy1 = int(input(f"Please enter the row coordinate (1 - {maxSize} for ship {shipName} "))
                if vertiy1 < 1 or vertiy1 > maxSize:
                    print("verty1")
                    raise ValueError
                horix2 = int(input(f"Please enter the column coordinate (1 - {maxSize}) for ships {shipName} "))
                if horix2 < 1 or horix2 > maxSize:
                    raise ValueError
                vertiy2 = int(input(f"Please enter the row coordinate (1 - {maxSize} for ship size {ship_size}) "))
                if vertiy2 < 1 or vertiy2 > maxSize:
                    raise ValueError

                #Horizontal and vertical checker.
                if vertiy1 == vertiy2 and (horix1 + 1 == horix2 or horix1 - 1 == horix2):
                    print("Horizontal selection.")
                    
                elif horix1 == horix2 and (vertiy1 + 1 == vertiy2 or vertiy1 - 1 == vertiy2):
                    print("vertical selection.")

                else:
                    raise SyntaxError
                # Match internal board plus dictionary
                horix1 -= 1
                horix2 -= 1
                vertiy1 -= 1
                vertiy2 -= 1               
                for key, value in shipsLocation.items():
                    if value[0] == (horix1, vertiy1) or value[0] == (horix2, vertiy2) or value[1] == (horix1, vertiy1) or value[1] == (horix2, vertiy2): 
                        print("Ships Location")
                        raise SystemError
                break
            except ValueError:
                print("Please enter a valid integer.")
            except SyntaxError:
                print("Error with horizontal and vertical checker, make sure coordinates line up. ")
            except SystemError:
                print("You have entered in coordinates that have already been used. Try again. ")
            except:
                print("Please enter a valid input.")

        playerGridY[vertiy1][horix1] = "🚢"
        playerGridY[vertiy2][horix2] = "🚢"
        shipsLocation[shipName] = [(horix1, vertiy1), (horix2, vertiy2)]

        for key, value in shipsLocation.items():
            print(f'{value[0]} and {value[1]}')
        
        if x == 3:
            return False

def isShipSunk(playerList, botList, shipLocationPlayer, shipLocationBot,computerTurn):
    sunkShip = None
    shipNameThatsSunk = None
    for key, value in shipLocationPlayer.items():
        shipLocation1Y = value[0][0]
        shipLocation1X = value[0][1]
        shipLocation2Y = value[1][0]
        shipLocation2X = value[1][1]
        if(computerTurn):
            for key, value in shipLocationPlayer.items():
                shipLocation1Y = value[0][0]
                shipLocation1X = value[0][1]
                shipLocation2Y = value[1][0]
                shipLocation2X = value[1][1]
            if botList[shipLocation1Y][shipLocation1X] == "🔥" and botList[shipLocation2Y][shipLocation2X] == "🔥":
                print(f"The bot has sunk one of your ships! Step it up")
                sunkShip = True
                shipNameThatsSunk = key
                if sunkShip == True:
                    del shipLocationPlayer[shipNameThatsSunk]
                    sunkShip = False
                    if len(shipLocationPlayer) == 0:
                        print("The bot sunk all your ships, you have lost! (🥺")
                        quit()
                    sunkShip = None
                    shipNameThatsSunk = None
        else:
            for key, value in shipLocationBot.items():
                shipLocation1Y = value[0][0]
                shipLocation1X = value[0][1]
                shipLocation2Y = value[1][0]
                shipLocation2X = value[1][1]
            if playerList[shipLocation1X][shipLocation1Y] == "🔥" and playerList[shipLocation2X][shipLocation2Y] == "🔥":
                print("You have sunk one of the bots ships!")
                sunkShip = True
                shipNameThatsSunk = key
                if sunkShip == True:
                    del shipLocationBot[shipNameThatsSunk]
                    sunkShip = False
                    if (len(shipLocationBot) == 0):
                        print("You have sunk all of the bots ships! You have won!")
                        quit()
    # Reset values 
    




def displayGrid(displayGridList, displayPlayerGrid,computerTurn): #Grid shown to player
        if(computerTurn):
            length = 5 #This grabs the length of display list
            xCordList = []
            for i in range(0, length): #This prints for the length of display list
                xCordList.append(str(i + 1))
                Fore.RED
            if (i < 9):
                print(Fore.RED + "     1    2    3    4    5    6    7    8    9    10")
            else:
                print(Fore.RED +"     1    2    3    4    5    6    7    8    9    10")
            for i in range(0, length):
                print(Fore.RED + f'{str(i + 1)}  {str(displayGridList[i])}')
            print("   Opposing Force \n \n \n   Player")
            xCordPlayerList = []
        else:
            length = 5 #This grabs the length of player display list
            for i in range(0, length): #This prints for the length of player display list
                xCordPlayerList.append(str(i + 1))
            if (i < 9):
                print(Fore.RED + "     1    2    3    4    5    6    7    8    9    10")
            else:
                print(Fore.RED  + "     1    2    3    4    5    6    7    8    9    10")
                Fore.RED
            for i in range(0, length):
                print(Fore.RED + f'{str(i + 1)}  {str(displayPlayerGrid[i])}')
            
 


def userInputGridSize(displayGridList, displayPlayerGrid): #Allows the user to determnine the grid size
    userGridSizeRunning = 1
    while (userGridSizeRunning != 0):
        userGridInput = 10
        if (userGridInput < 5):
            "Enter a number at or above the minimum."
        elif (userGridInput == 5): #If the size they entered is five, the minimum and the default, it just returns it with no special stuff afterwards
            gridSize = userGridInput
            return gridSize
        elif (userGridInput > 5):
            gridSize = userGridInput
            gridSizeLoop = gridSize 
            while (gridSizeLoop != 0): #This while loop adds the correct amount of lists to the grid 
                displayGridList.append([])
                displayPlayerGrid.append([])
                gridSizeLoop = gridSizeLoop - 1
            return gridSize #returns gridSize. This is VERY IMPORTANT as many  of my functions use this variable to function properly.

def gridCreation(gridSize, displayGridList, displayPlayerGrid): #This function is very important, it adds all of the tiles and assigns them default values. Requires gridSize.
    length = int(len(displayGridList)) #This grabs the length of display list
    gridCreateRun = 0
    while (gridCreateRun != gridSize):
        for i in range(0, length):
            displayGridList[i].append('O') #Here it is looping adding the correct amount of default blank tiles. One append does the internal, the other here does the display list
            displayPlayerGrid[i].append('O')
        gridCreateRun = gridCreateRun + 1 #This iterates until the grid reaches the proper size
color = [Fore.BLUE,Fore.CYAN,Fore.GREEN,Fore.LIGHTBLACK_EX,Fore.LIGHTBLUE_EX,Fore.LIGHTCYAN_EX,Fore.LIGHTGREEN_EX,Fore.LIGHTMAGENTA_EX,Fore.LIGHTRED_EX,Fore.LIGHTWHITE_EX,Fore.LIGHTYELLOW_EX,Fore.MAGENTA,Fore.RED,Fore.WHITE,Fore.YELLOW]
colorchoice = random.choice(color)




def shot_function(gridSize,displayGridList,displayPlayerGrid,shipsLocationBot,computerTurn):#user inputs in coordinates
    if(computerTurn):
        comp_maxsize = gridSize - 1
        comp_shotrow = random.randint(0, comp_maxsize)
        comp_shotcol = random.randint(0, comp_maxsize)
        if (displayPlayerGrid[comp_shotcol][comp_shotrow] == '🚢'):
            displayPlayerGrid[comp_shotcol][comp_shotrow] = '🔥'
        else:
            displayPlayerGrid[comp_shotcol][comp_shotrow] = "💣"
    else:
        user_cord = str(input("Where do you want to shoot? Coordinates plz e.g 2,3: ")+ "~") #Makes a string of user's input plus ~ at the end to let the program know that's the end of the string
        print (user_cord)
        if user_cord.count(",") == 1:
            user_cordx = user_cord[0:user_cord.index(",")] #reads and stores everything from the start of the string to the , 
            user_cordy = user_cord[user_cord.index(",") + 1:user_cord.index("~")] #reads and stores everything from the comma to the end point denoted by ~
            user_cordx = int(user_cordx) - 1
            user_cordy = int(user_cordy) - 1
            botLocationList = [None, None]
            counter = 0
            for key, value in shipsLocationBot.items():
                botLocationList[counter] = key
                counter += 1
            choosing_location=True
            while(choosing_location):
                try:
                    if (displayGridList[user_cordy][user_cordx] != '💣'):
                        print (shipsLocationBot)
                        if  (user_cordy == shipsLocationBot[botLocationList[0]][0][1] and user_cordx  == shipsLocationBot[botLocationList[0]][0][0]):
                            if (displayGridList[user_cordy][user_cordx] != '🔥'):
                                displayGridList[user_cordy][user_cordx] = '🔥'
                                return displayGridList
                        elif  (user_cordy == shipsLocationBot[botLocationList[0]][1][1] and user_cordx  == shipsLocationBot[botLocationList[0]][1][0]):
                            if (displayGridList[user_cordy][user_cordx] != '🔥'):
                                displayGridList[user_cordy][user_cordx] = '🔥'
                                return displayGridList
                        elif(user_cordy == shipsLocationBot[botLocationList[0]][0][1] and user_cordx  == shipsLocationBot[botLocationList[1]][0][0]):
                            if (displayGridList[user_cordy][user_cordx] != '🔥'):
                                        displayGridList[user_cordy][user_cordx] = '🔥'
                                        return displayGridList
                        elif(user_cordy == shipsLocationBot[botLocationList[1]][1][1] and user_cordx  == shipsLocationBot[botLocationList[1]][1][0]):
                                    if (displayGridList[user_cordy][user_cordx] != '🔥'):
                                        displayGridList[user_cordy][user_cordx] = '🔥'
                                        return displayGridList
                        else:
                            displayGridList[user_cordy][user_cordx] = '💣'
                            return displayGridList
                except:
                    continue
                
def main():
        displayGridList = []
        displayPlayerGrid = []
        shipsLocationPlayer = {}
        shipsLocationBot = {}
        #it's small now


        gridSize = userInputGridSize(displayGridList, displayPlayerGrid)
        gameRunning = 1
        gridCreation(gridSize, displayGridList, displayPlayerGrid)
        userGen = int(input("Random or Manually place ships?(1 for random or 0 for manual) "))

        if (userGen == 1):
            print("Generating!")
            placePlayerRandom = True
            place_ships_randomly(displayPlayerGrid, gridSize, shipsLocationPlayer, shipsLocationBot, placePlayerRandom, displayGridList)

        elif (userGen == 0):
            print("You got it!")
            # Going to reuse the random function so need a true or false value to not randomly generate player but use random for bot.
            placePlayerRandom = place_ships_manually(displayPlayerGrid, gridSize, shipsLocationPlayer)
            place_ships_randomly(displayPlayerGrid, gridSize, shipsLocationPlayer, shipsLocationBot, placePlayerRandom, displayGridList)    

        gridSize = userInputGridSize(displayGridList, displayPlayerGrid)

        #place_ships_randomly(displayGridList)
        gameIterate = 0
        while (gameRunning == 1):
            computerTurn=True
            if(computerTurn):
                time.sleep(.1)
                os.system('cls')
                isShipSunk(displayGridList, displayPlayerGrid, shipsLocationPlayer, shipsLocationBot,computerTurn)
                print (shipsLocationBot)
                displayGrid(displayGridList, displayPlayerGrid,computerTurn)
                displayGridList=shot_function(gridSize,displayGridList,displayPlayerGrid,shipsLocationBot,computerTurn)
                gameIterate = gameIterate + 1
                computerTurn=False
                if (gameIterate == 20):
                    os.system('cls')
                    print("You've run out of anti - ship missles! \n \n womp womp \n \n Game over: \n")
                    displayGrid(displayGridList, displayPlayerGrid,computerTurn)
                    gameRunning = 0
            else:
                time.sleep(.1)
                os.system('cls')
                isShipSunk(displayGridList, displayPlayerGrid, shipsLocationPlayer, shipsLocationBot,computerTurn)
                print (shipsLocationBot)
                displayGrid(displayGridList, displayPlayerGrid,computerTurn)
                displayGridList=shot_function(gridSize,displayGridList,displayPlayerGrid,shipsLocationBot,computerTurn)
                gameIterate = gameIterate + 1
                computerTurn=True
                if (gameIterate == 20):
                    os.system('cls')
                    print("You've run out of anti - ship missles! \n \n womp womp \n \n Game over: \n")
                    displayGrid(displayGridList, displayPlayerGrid,computerTurn)
                    gameRunning = 0

main()

# Game changing comment
