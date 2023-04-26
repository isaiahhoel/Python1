# --------------------------------------
# Hannibal-LaGrange University
# CSC 303 - Program Design
# Fall 2021
# Instructor: Mr. Hammontree
#
# Student: Hammontree, Jeff
# Student ID: n/a
# Student Email: jeff.hammontree@hlg.edu
#
# EXAMPLE: GameSelect.py PROGRAM
# Date: 09-01-2021
# --------------------------------------


import PersonType

# Pull attributes of the User from the PersonType module
thisFirstName = PersonType.firstName
thisLastName = PersonType.lastName
thisPerson = PersonType.personType

# This program determines what kind of game they can purchase
print("")
print("Pick a game to purchase: ")
print("%-2s%-18s%-10s%6s" % ("#", "Game Title", "Rating", "Price"))
print("-" * 36)
print("%-2d%-18s%-10s$%4.2f" % (1, "Tetris", "E", 10.9))
print("%-2d%-18s%-10s$%4.2f" % (2, "Metroid Prime", "T", 99.99))
print("%-2d%-18s%-10s$%4.2f" % (3, "Speed Limit", "M", 19.7))
print("")

gameNbr = input("Choose the number associated with the game. Enter 'X' to finish purchase: ")
runningTotal = 0.0
while gameNbr != "X":
    selectNbr = int(gameNbr)
    if(selectNbr > 3):
        print("Invalid selection. Try again")
    elif(selectNbr == 3 and thisPerson == "Adult"):
        runningTotal += 19.7
        print("Speed Limit added to cart.")
    elif(selectNbr == 2 and (thisPerson == "Adult" or thisPerson == "Teenager")):
        runningTotal += 99.99
        print("Metroid Prime added to cart.")
    elif(selectNbr == 1):
        runningTotal += 10.9
        print("Tetris added to cart.")
    else:
        print("A " + thisPerson + " is not allowed to purchase this game.  Sorry " + thisFirstName + "!")
    gameNbr = input("Choose another item or enter 'X' to finish your purchase: ")

print("Your cart total is $%8.2f" % runningTotal)
print("Thank you for your purchase " + thisFirstName + " " + thisLastName + ".  Enjoy!")
