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
# Assignment:Chapter 6 Project 5
# Date: 09/27/2021
# ---------------------------------------------------


def isSorted(L):
    sortedList = True
    for number in range(1, len(L)):
        if(L[number] >= L[number - 1]):
            continue
        else:
            sortedList = False
            break
    return sortedList

list = []

listLength = int(input("Enter the length of the list you would like to create: "))       #establishes the length of the list for customizable lengths and list numbers

for x in range(0, listLength):
    inputList = list.append(int(input("Enter a set of Numbers to be added to the list: ")))
    x += 1

print("The listed is sorted:", isSorted(list))               #Gives a statement that the list is sorted and 
                                                             #states whether it is or isn't sorted




