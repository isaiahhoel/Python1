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
# Assignment: PersonType.py MODULE
# Date: 08-24-2021
# --------------------------------------


# This module asks the user for their attributes
# and determines if they are an Adult, Teenager
# or child.

# Ask the User for their attributes
firstName = input("What is your FIRST name? ")
lastName = input("What is your LAST name? ")
age = int(input("What is your AGE today? "))

if(age < 13):
    print("You are a CHILD, " + firstName + " " + lastName)
    personType = "Child"
elif(age >= 13 and age < 18):
    print("You are a TEENAGER, " + firstName + " " + lastName)
    personType = "Teenager"
else:
    print("You are an ADULT, " + firstName + " " + lastName)
    personType = "Adult"
