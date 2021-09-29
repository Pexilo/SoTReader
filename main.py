print('''\n
    Made by Pexilo,
    Github: https://github.com/Pexilo / Discord: Pexilo#7866

    Welcome ! 

    I made this small tool for book note taking, 
    to make your life and lore documentation easier :)


    Make sure to have a folder named "images",
    then drop your screenshots of the books inside,\n
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
        print ("Done")

import cv2

date=time.strftime("%m-%d_%H-%M",time.localtime())
name='Result_'+date+'.txt'
savePath = os.path.dirname(__file__) + '\\results\\' + name

path = "images/*.*"
imgNumber = 1
reader = easyocr.Reader(['fr', 'en'], gpu=False)
print('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n''')

with open(savePath, 'w') as f:

    for file in glob.glob(path):
        print(file, " - Processing image", imgNumber)
        img = cv2.imread(file, 0)
        results = reader.readtext(img, detail=0, paragraph=True)
        print("     ", results[0], "\n")
     ################################################################################################################          
     #  REPLACE line below (and above if you read the console) to  results  if you having trouble with text output  # 
     #              (Basically, remove "[0]" from results[0] variable, don't forget to save the file)               #
     ################################################################################################################
        line = "• ", file, " - Image", str(imgNumber), "\n", str(results[0]), "\n\n" 
        f.writelines(line)
        imgNumber += 1

winsound.Beep(1000, 400)
print("Done. Check for mistakes :)\n➜ File " + name + " created for backup in results folder.")