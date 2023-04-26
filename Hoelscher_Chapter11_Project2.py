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
# Assignment:Chapter 11 Project 2
# Date: 11/08/2021
# ---------------------------------------------------


#The time complexity of this function is O(n)
def reverse(lyst):
    i = 0
    numList = len(lyst) - 1
    while i < numList:
        lyst[i], lyst[numList] = lyst[numList], lyst[i]
        i += 1 
        numList -= 1
    return lyst

def main():
    """Tests with two lists."""
    lyst = list(range(4))
    print("Original list: " + str(lyst))
    reverse(lyst)
    print("Reverse list: " + str(lyst))
    lyst = list(range(3))
    print("Original list 2: " + str(lyst))
    reverse(lyst)
    print("Reverse list 2: " + str(lyst))

if __name__ == "__main__":
    main()