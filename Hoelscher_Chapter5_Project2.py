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
# Assignment:Chapter 9 Project 1
# Date: 11/01/2021
# ---------------------------------------------------


class student(object):
    #student
    def __init__(self, name, number):
        # creates a student with given name, # of scores and sets scores to zero
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        return self.name
    
    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]

    def getAverage(self):
        return sum(self.scores) / len(self.scores)

    def getHighScore(self): 
        return max(self.scores)

    def __str__(self):
        return "Name: " +self.name + "\nScores: " + \
            " ".join(map(str, self.scores))