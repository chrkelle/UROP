#*****************************************************************#
#This program does the following:
#1.Prints folder contents
#2.Prints file names and image sizes
#3.Changes image sizes
#4.Moves files into seperate folders based on size
#
#*Requires: JPEG images must be located explicitly in UROP folder
#*****************************************************************#


#LIBRARIES#****************************#
import os
import shutil
import glob
from PIL import Image
from resizeimage import resizeimage
#**************************************#

#Creates space between operations
def seperator():
    print("\n***********************************\n")

#Prints folder contents
def Print_Contents(Folder_Contents):
    print("This function prints out the contents of a Folder")
    print"Folder Contents: ", Folder_Contents
    return

#Prints name of image, and width/heigth dimensions
def Image_Sizes(Folder_Contents):
    for File in Folder_Contents:
        print File
        img = Image.open(File)
        width, height = img.size
        print("width: ", width)
        print("height: ", height)
    return

#Takes user input of width/height, then recreates images to specified dimensions        
def Image_Resize(Folder_Contents):
    width = input("Please enter a width: ")
    height = input("Please enter a height: ")
    for File in Folder_Contents:
        img = Image.open(File)
        img = img.resize((width, height), Image.BILINEAR)
        img.save(File, "JPEG")
    return


def Image_Seperate(Folder_Contents):
    folder = raw_input("Name the folder you would like to move files to: ")
    os.mkdir(folder)
    lowerWidth = int(raw_input("Input width lower bound: "))
    upperWidth = int(raw_input("Input width upper bound: "))
    lowerHeight = int(raw_input("Input height lower bound: "))
    upperHeight = int(raw_input("Input height upper bound: "))
    for File in Folder_Contents:
        img = Image.open(File)
        width, height = img.size
        if(width > lowerWidth & width < upperWidth & height > lowerHeight & height < upperHeight):
             shutil.copy(File,os.path.join(os.getcwd(),folder)) 
        
    
    

def main():
        Folder_Contents = glob.glob('*.jpg')
        while(True):
            print("Menu")
            print("\n1 - Print folder contents")
            print("2 - Print image name/size")
            print("3 - Change images size")
            print("4 - Move images to folder")
            print("0 - Quit")
            command = input("\nPlease select an option: ")
            seperator()
            if (command == 1):
                Print_Contents(Folder_Contents)
            elif (command == 2):
               Image_Sizes(Folder_Contents)
            elif (command == 3):
                Image_Resize(Folder_Contents)
            elif (command == 4):
                Image_Seperate(Folder_Contents)
            elif (command == 0):
                return
            seperator()
        return


        
            







main()
