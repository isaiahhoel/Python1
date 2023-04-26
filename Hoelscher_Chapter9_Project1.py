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


import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(random.randint(0, 100))

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
        
    # Write method definitions here
    def __eq__(self, student):
        return self.scores == student.scores

    def __ge__(self, student):
        return self.scores >= student.scores

    def __lt__(self, student):
        return self.scores < student.scores

def main():
    studentList = []
    """Student 1"""
    student_1 = Student("Ken", 5)
    print(student_1)
    studentList.insert(0, student_1)

    """student 2"""
    student_2 = Student("Bob", 5)
    print(student_2)
    studentList.insert(1, student_2)

    """student 3"""
    student_3 = Student("Billy", 5)
    print(student_3)
    studentList.insert(2, student_3)

    """student 4"""
    student_4 = Student("Jeff", 5)
    print(student_4)
    studentList.insert(3, student_4)

    """student 5"""
    student_5 = Student("Fred", 5)
    print(student_5)
    studentList.insert(4, student_5)


    random.shuffle(studentList)
    studentList = sorted(studentList, key=lambda p: p.name)

    print("\nTesting Equality...\n" + str(student_1 == (student_2)) + "\n")
    print("Testing if Ken is greater than or equal to Bob...\n" + str(student_1 >= (student_2)) + "\n")
    print("Testing if Ken is less than Bob...\n" + str(student_1 < (student_2)) + "\n")
    print("Putting students in list and shuffling...\n")
    print("Shuffling and sorting list...\n")

    for info in studentList:
        print(info.__str__())

if __name__ == "__main__":
    main()
