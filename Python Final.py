# ---------------------------------------------------

# Hannibal-LaGrange University

# CSC 303 - Program Design

# Fall 2021

# Instructor: Mr. Hammontree

#

# Student: Hoelscher, Isaiah

# Student ID: A0000033934

# Student Email: isaiah.hoelscher.18@student.hlg.edu

#

# Assignment: Program Design Final - Lineup Builder v1.0

# Date: 11/11/2021

# ---------------------------------------------------

 

'''GOAL OF PROGRAM: Create a lineup using a player's name, number, and

batting average. Allow the user to sort the lineup using various filters.

The user is then able to export the lineup to an output file.'''

 

#Classes are types of data essentially

#Objects are things belonging to a particular class

#Methods are acting upon objects, and can have parameters

#Use p.set_x(self, x) for the edit function

#Possibly add sound to program

#try to figure out how to print the correct list

 

import os

 

class Player:

    def __init__(self, first, last, position, number, avg):

        self.first = first

        self.last = last

        self.position = position

        self.number = number

        self.avg = avg

 

    def get_first(self):

        return self.first

   

    def get_last(self):

        return self.last

   

    def get_position(self):

        return self.position

   

    def get_number(self):

        return self.number

   

    def get_avg(self):

        return self.avg

 

    def __lt__(self, other):

        return self.avg > other.avg

 

    def __gt__(self, other):

        return self.avg < other.avg

 

    def __eq__(self, other):

        return self.avg == other.avg

 

class Game:

    def __init__(self, date, teamName, oppTeam, location):

        self.date = date

        self.teamName = teamName

        self.oppTeam = oppTeam

        self.location = location

 

def menu():

   

    print('\n'"Please select an option: ")

    print('\n'"[1] View today's lineup w/ Avg.")

    print("[2] Sort Lineup from Highest to Lowest Batting Avg.")

    print("[3] Calculate team batting average from today's lineup.")

    print("[4] Output Lineup to .txt file")

    print("[5] Exit Lineup Builder v1.0")

 

    option = (input('\n'"Hit enter to add a new player or choose and option: "))

 

    while option != 0:

       

        if option == "1":

            viewLineup(playerList)

            menu()

        elif option == "2":

            playerList.sort()

            viewLineup(playerList)            

            menu()

        elif option == "3":

            teamAvgCalculator(playerList)

            menu()                                #team avg calc. currently

        elif option == "4":

            outputLineup(playerList)

            menu()
        
        elif option == "5":

            print('\n'"Thank you for using Lineup Builder!"'\n')

            quit()

        elif option == "":
            if len(playerList) > 9:
                menu()
            else:
                break

           

        break

 

def viewLineup(playerList):

    print('\n'"Today's lineup", userGame.date, "for game between", userGame.teamName,

    "and", userGame.oppTeam, "at",userGame.location)

    print('\n' + userGame.teamName)

    print("-----------------------------------------------")

    print("%-21s%-13s%-5s" % ("Player(#)", "Pos.", "Batting Avg."))

    for players in playerList:

        playerNameNum = players.first + " " + players.last + "(" + str(players.number) + ")"

        print("%-21s%-13s%-5.3f" % (str(playerNameNum), players.position, players.avg))

 

def outputLineup(playerList):

    lineupFile = input("Enter the desired file name (example.txt): ")

    with open(lineupFile, 'w') as outputLineup:

       

        for players in playerList:

            playerNameNum = players.first + " " + players.last + "(" + str(players.number) + ")"

            outputLineup.write("%-21s%-13s%-5.3f" % (str(playerNameNum), players.position, players.avg) + "\n")

        print('\n'"Writing Lineup to file", lineupFile,"...")

        print('\n'"DONE! Lineup has been written to", lineupFile)

 

def teamAvgCalculator(playerList):

    avgTotal = 0.0

    for player in playerList:

        avgTotal += player.avg

    teamAverage = avgTotal / len(playerList)

    print('\n'"The team average is", round(teamAverage, 3)) 

def userPlayerInput():

    for count in range(10):

        count = 1

        userPlayer = Player(first = input('\n'"Enter the player's first name: "), last = input("Enter the player's last name: "),

        position = input("Enter the player's position: "), number = int(input("Enter the player's number: ")),

        avg = float(input("Enter the player's batting average(example: .429): ")))

       

        print('\n' + userPlayer.first, userPlayer.last, "was added to the lineup.")

        print('\n'+ "------Current Lineup for",userGame.teamName + "------")

       

        playerList.append(userPlayer)

        for player in playerList:

            leftToGo = 10 - count

            print(str(count) + ".", player.first, player.last)

            count += 1

        print('\n',leftToGo, "players left to go!")

 

        exitOption = input('\n'"Press ENTER to add another player or type SET to set current lineup and view more options: ")

           

        while exitOption != 0:

            if exitOption == "SET":

                viewLineup(playerList)

                menu()

            break

               

    print("\nLineup for the",userGame.teamName,"is complete!")

 

    menu()

 

if "__main__" == __name__:

    #ask for date, name, oppteam, and location

    playerList = []

 

    print("WELCOME TO LINEUP BUILDER v1.0!")

    print('\n'"Created by Isaiah Hoelscher and River Thompson")

    input('\n'"Press ENTER to continue...")

 

    userGame = Game(date = input('\n' "Enter the date of the game(MM/DD/YYYY): "),

    teamName = input("Enter the name of your team: "), oppTeam = input("Enter the name of the opposing team: "),

    location = input("Enter the location of the game: "))

 

    userPlayerInput()
