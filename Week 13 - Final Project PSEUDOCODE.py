# ---------------------------------------------------
# Hannibal-LaGrange University
# CSC 303 - Program Design
# Fall 2021
# Instructor: Mr. Hammontree
#
# Student: Thompson, River
# Student ID: A0000033960
# Student Email: River.Thompson.10@student.hlg.edu
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

class Lineup: 
    def __init__(self, lineup, max_players):
        self.lineup = lineup 
        self.max_players = max_players 
        self.players = [] 

    def add_player(self, player): 
        if len(self.players) < self.max_players:
            self.players.append(player)
            return True 
        return False
    
    def get_batting_avg(self): 
        value = 0 
        for player in self.players: 
            value += player.get_avg()
        
        return value / len(self.players) 

playerList = []
for i in range (11):
    userPlayer = Player(first = input("Enter the player's first name: "), last = input("Enter the player's last name: "), 
    position = input("Enter the player's position: "), number = int(input("Enter the player's number: ")), 
    avg = float(input("Enter the player's batting average(example: .429): ")))

    print('\n' + userPlayer.first, userPlayer.last, "was added to the lineup.")
    playerList.append(userPlayer)
    for players in playerList:
        print(players.first, players.last)

lineup = Lineup("My Team", 10)

class Game: 
    def __init__(self, date, teamName, oppTeam, location):
        self.date = date
        self.teamName = teamName
        self.oppTeam = oppTeam
        self.location = location 
    


