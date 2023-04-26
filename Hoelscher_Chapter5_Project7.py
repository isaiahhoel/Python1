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
# Assignment:Chapter 5 Project 7
# Date: 09/20/2021
# ---------------------------------------------------


import re

fileSort = input("Enter the input file name: ")
fileRead = open(fileSort, 'r')

wordList = []

for text in fileRead:
    lowerWord = text.lower()
    stripWord = re.sub(r'[^\w\s]', '', lowerWord)      #strip Punctuation
    newWord = stripWord.strip().split(" ") #Strip and split words in file at 
                                           #spaces and new lines
    
    wordList += newWord

wordList.sort()

for word in wordList:
    print(word)

fileRead.close()