import os

#Implementation displayFiles method

#that expects pathname as argument

def displayFiles(pathname):

    # check the file is exist or not

    if os.path.isfile(pathname):

        #Get the name of the file

        name = os.path.basename(pathname)

        #name of the file to be displayed

        #open the file in read mode

        openFile = open(pathname,"r")

        #Get the contents from file

        fileContents = openFile.readlines()

        #Iterate the contents

        for eachContent in fileContents:

            #Display each line from file

            print(eachContent)

    #check whether pathname is directory or not     

    elif os.path.isdir(pathname):

        #get all the directories

        GetDirectories = os.listdir(pathname)

        #Iterate the loop

        for eachItem in GetDirectories:

            #join the pathname and to get complete

            #path

            completePath = os.path.join(pathname,eachItem)

            print("File name: ",completePath)

            isdirectory = os.path.isdir(completePath)

            #check whether given path is

            #directory or not

            if isdirectory or os.path.isfile(completePath):

                #if it is true

                #call the recursive function

                displayFiles(completePath)

#Get the file name

pathname = input("Enter File name/directory path: ")

#call displayFiles method

displayFiles(pathname)