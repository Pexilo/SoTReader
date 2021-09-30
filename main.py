print('''\n
    Made by Pexilo,
    Github: https://github.com/Pexilo | Discord: Pexilo#7866

    Welcome !

    I made this small tool for book note taking,
    to make your life and lore documentation easier :)


    Make sure to have a folder named "images" and a one named "results" where main.py is located,
    then drop screenshots of your choice inside "/images".\n
    ''')

import subprocess
import winsound
import time
import sys
import os
import glob

while True:
    check = True
    try:
        import easyocr

    except ImportError as err:
        check = False
 
    if check == True:
        break
    else:
        print ("Installing easyocr package...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "easyocr"])
        print ("\nInstallation done.\n")

import cv2

arguments = len(sys.argv) - 1
arg = False

if arguments == 1 and sys.argv[1].lower() == 'fix':
    arg = True
    print("You will now get all texts on the screenshots.\n")
if arguments == 1 and sys.argv[1].lower() != 'fix': 
    print ("You specified: " + sys.argv[1] + "\nUsage: If you having trouble with missing text, please use <python main.py fix>")
    exit()
if arguments > 1:
    print ("More than one argument has been specified.\nUsage: If you having trouble with missing text, please use <python main.py fix>")
    exit()

date=time.strftime("%m-%d_%H-%M",time.localtime())
name='Result_'+date+'.txt'
savePath = os.path.dirname(__file__) + '\\results\\' + name

path = "images/*.*"
imgNumber = 1
reader = easyocr.Reader(['fr', 'en'], gpu=False)
print('''\n\nProcessing please wait...\n\n\n''')


with open(savePath, 'w') as f:

    for file in glob.glob(path):
        print(file, "- Processing image", imgNumber)
        img = cv2.imread(file, 0)
        results = reader.readtext(img, detail=0, paragraph=True)

        if arg == True:
            print("     ", results, "\n")
            line = "• ", file, " - Image ", str(imgNumber), "\n", str(results), "\n\n"
        else:
            print("     ", results[0], "\n")
            line = "• ", file, " - Image ", str(imgNumber), "\n", str(results[0]), "\n\n" 

        f.writelines(line)
        imgNumber += 1

winsound.Beep(1000, 400)

if imgNumber == 1: 
    print("Error, your images folder is empty. Please provide at least 1 image.\n")
else: 
    print("Done. Check for mistakes :)\n> File " + name + " created for backup in results folder.\n")