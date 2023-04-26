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
# Assignment:Chapter 4 Project 3 Part one
# Date: 08/27/2021
# ---------------------------------------------------


enterText = input("Enter a file name to be decrypted:")  #Need a pre made text file to encrypt
outPutCode = input("Enter name of file to write to: ")
distance = int(input("Enter the distance value: "))

textRead = open(enterText, 'r')
codeWrite = open(outPutCode, 'w')
fileInput = textRead.read()
code = ""
for ch in fileInput:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('~'):
        cipherValue = chr(32) + distance - \
                        (chr(126) - ordvalue + 1)
    code += chr(cipherValue)
codeWrite.write(code)

textRead.close()
codeWrite.close()


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
# Assignment:Chapter 4 Project 3 Part two
# Date: 08/27/2021
# ---------------------------------------------------


code = input("Enter the name of the coded text file: ")  #File name of encrypted code
outputTextFile = input("Enter the file name the decrypted code will go on: ")
distance = int(input("Enter the distance value from previous encryption: "))
readFile = open(code, 'r')
textWrite = open(outputTextFile, 'w')
textInFile = readFile.read()
outputText = ""
for ch in textInFile:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord(' '):
        cipherValue = chr(126) - (distance - (chr(32) - ordvalue - 1))
    outputText += chr(cipherValue)
textWrite.write(outputText)

textWrite.close()
readFile.close()

if not ".csv" in directPath:
        return

    if os.path.isfile(directPath):
        files = os.listdir(directPath)