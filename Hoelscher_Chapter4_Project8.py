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
# Assignment:Chapter 4 Project 8
# Date: 09/10/2021
# ---------------------------------------------------


fileCopy = input("Enter the name of the file to be copied: ")
filePaste = input("Enter the name of the file you want the contents to be copied to: ")

fileRead = open(fileCopy, 'r')
fileWrite = open(filePaste, 'w')

fileTranslate = fileRead.read()

fileWrite.write(fileTranslate)

fileWrite.close()
fileRead.close()