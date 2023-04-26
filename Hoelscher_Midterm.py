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
# Assignment: Mid-Term Project
# Date: 10/11/2021
# ---------------------------------------------------


import os

myDict = dict()      #dictionary for data

#find all .csv files recursively and send to splitFile 
def searchFile(directPath):
    if directPath.endswith(".csv"):
        splitFile(directPath)
    elif os.path.isdir(directPath):
        files = os.listdir(directPath)
        for all in files:
            searchFile(os.path.join(directPath, all))
    else:
        return 
    
#open .csv file, read it, split/Strip commas and n/, and create a list to add to myDict
def splitFile(files):
    print("Processing data file: " + files +" ...\n")
    file = open(files, 'r')
    fileData = file.readlines()
    for eachLine in fileData:
        (studentid, lastname, username, firstname, password, DOB, gradelevel) = eachLine.strip("\n").split(",")
        myDict[username] = password
    return myDict

#open new file and write dictionary to file sorted a-z
def writeData(data):
    outputFile = "output.txt"
    print("Formatting and sorting the output...\n")
    with open(outputFile, 'w') as fileWrite:
        for listItem in sorted(data):
            fileWrite.write(listItem + "|" + data[listItem] + "\n")
    print("Writing the output file to output.txt...\n")        


print("\nData File Translation Program - v0.1\n" + "-" * 36)
filePrint = input("Please enter a pathname of a file or a directory containing data files: ")
print("\n" + "Searching the file path for data files...\n")
searchFile(filePrint)
writeData(myDict)
print("DONE!\n") 