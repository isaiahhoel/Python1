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
# Assignment:Chapter 6 Project 7
# Date: 09/27/2021
# ---------------------------------------------------


import os 

def printFile(filePath):
    if os.path.isdir(filePath):
        files = os.listdir(filePath)
        for all in files:
            printFile(os.path.join(filePath, all))
    elif os.path.isfile(filePath):
        readFile = open(filePath, 'r')
        fileContent = readFile.readlines()
        print("\n", "Found File in Directory:", filePath)
        for content in fileContent:
            print(content)
        
        

filePath = input("Enter File name or Directory path: ")

printFile(filePath)