print('''\n
    Made by Pexilo,
    Github: https://github.com/Pexilo | Discord: Pexilo#7866

    Welcome !

    I made this small tool for book note taking,
    to make your life and lore documentation easier :)


    Make sure to have a folder named "images" and a one named "results" where main.py is located,
    then drop screenshots of your choice inside "/images".\n
    ''') # Welcome message and instructions

import subprocess as sp
import winsound 
import sys 
import os 
import glob 

while True: # Infinite loop to keep the program running while the package are being installed
    check = True # default value for check
    try: # Check if the package is already installed
        import easyocr # pip install easyocr 

    except ImportError as err: # if a error is raised change the value of check to False
        check = False # set check to false to continue the loop
 
    if check == True: # if easyocr is installed
        break # break the loop

    else: # if easyocr is not installed
        print ("Installing easyocr package...") # print this message to the user
        sp.check_call([sys.executable, "-m", "pip", "install", "easyocr"]) # install the package
        print ("\nInstallation done.\n") # print this message to inform the user that the package is installed

import cv2 # pip install opencv-python after installing easyocr to prevent errors


arguments = len(sys.argv) - 1 # get the number of arguments passed to the program
arg = False # default value for arg

if arguments == 1 and sys.argv[1].lower() == 'fix': # if the user wants to fix the texts detected
    arg = True # set arg to true
    print("You will now get all texts on the screenshots.\n") # print this message

if arguments == 1 and sys.argv[1].lower() != 'fix':  # default
    print ("You specified: " + sys.argv[1] + "\nUsage: If you having trouble with missing text, please use <python main.py fix>") # print this message if the user specified something else

if arguments > 1: # if the user specified more than one argument
    print ("More than one argument has been specified.\nUsage: If you having trouble with missing text, please use <python main.py fix>") # print this message
    exit() # exit the program


temp_fileName="__temp.txt"  # set the name of the file by concatenating the date and time
savePath = os.path.dirname(__file__) + '\\results\\' # set the path of the file

path = "images/*.*" # set the path of the images
imgNumber = 1 # define the number count of the image
reader = easyocr.Reader(['fr', 'en'], gpu=False) # set the reader to french and english
print('\n\nProcessing please wait...\n\n') # print this message


for file in glob.glob(savePath + "__temp*"): # for each file that contains __temp inside savePath
    os.remove(file) # remove the file


with open(savePath + temp_fileName, 'w') as f: # open the text result file

    for file in glob.glob(path): # for each image in the folder

        print(">", file, "- Processing image", imgNumber) # print the image number and the image name
        img = cv2.imread(file, 0) # read the image
        results = reader.readtext(img, detail=0, paragraph=True) # read the text

        if arg == True: # if the user wants to fix the texts detected
            resultsString = "" # define the string to be written in the file

            for i in range(len(results)): # for each text detected
                resultsString += results[i] + "\n  " # concatenate the text with a new line and a space
                
            print(" ", resultsString, "\n") # print the text detected
            line = "• {} - Image {}\n  {}\n\n".format(file, imgNumber, resultsString) # set the line text to be written in the file

        else: # default
            print("     {}\n".format(results[0])) # print the text detected
            line = "• {} - Image {}\n  {}\n\n".format(file, imgNumber, results[0]) # set the line text to be written in the file

        f.writelines(line) # write the line to the file
        imgNumber += 1 # increase the image number count by 1


if imgNumber != 1: # if the images folder is not empty
    new_fileName = str(results[0][:45] + '..' if len(results[0]) > 45 else results[0]) + ".txt" # set the new file name
    try: # try to remove the new file name if it already exists in the results folder to avoid errors
        os.remove(savePath + new_fileName) # remove the file that contains the new file name
    except OSError: # if the file does not exist in the results folder
        pass # pass the error

    old_file = os.path.join("results", temp_fileName) # set the path of the file to be deleted
    new_file = os.path.join("results", new_fileName) # set the path of the file to be renamed and if the text is too long, shorten it
    os.rename(old_file, new_file) # rename the file


winsound.Beep(1000, 400) # play a sound to notify the user that the program is done

if imgNumber == 1: # if the user didn't have any image
    print("\nError, your images folder is empty. Please provide at least 1 image.\n> {}\\images".format(os.path.dirname(__file__))) # print this message
    print("\nPress enter to exit...") # print this message
    input() # keep the program open

else: # default
    print("\nDone. Check for mistakes :)\n> File: '{}'\nCreated in '{}' directory.".format(new_fileName, savePath)) # print this message
    print("\nPress enter to exit...") # print this message
    input() # keep the program open