#############################
import os
import glob
import fnmatch
import shutil
import random
#############################



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#







#Zach replace with Random Directory path on your computer
RandomDirectory = '/Users/Chris/Desktop/UROP/Random'








#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#






print("Starting directory: ")
print(os.getcwd())
print("")

#Loops through Directories
for Dir in glob.glob('*Brigade'):
    
    #Change Directory to Log files
    os.chdir(os.path.join(os.getcwd(),Dir))





#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#






    #Zach make sure this is the correct name of 'Log Files' on your computer
    os.chdir(os.path.join(os.getcwd(),'Log Files'))  







#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#





    print("Changed directory to: ")
    print(os.getcwd())

    #Get number of files in Log files
    NumFiles = len(os.listdir(os.getcwd()))

    #No files
    if (NumFiles == 0):
        continue

    #Less than or equal to 10 files
    elif (NumFiles <= 10):
        #For jpg files copy and move
        for File in glob.glob('*.jpg'):
            FileName = (Dir + File)
            shutil.copy(File, RandomDirectory + FileName)

        #For JPG files copy and move
        for File in glob.glob('*.JPG'):
            FileName = (Dir + File)
            shutil.copy(File, RandomDirectory + FileName)

    #More than 10 files
    else:
        i = 0

        #Create list of Used files
        Used = [];
        Directory = os.getcwd()

        #Grab 10 files
        while (i < 10):
            File = random.choice(os.listdir(os.getcwd()))

            #Checks for file already used
            if (fnmatch.fnmatch(File, '*.JPG')):
                while ((File in Used) or(fnmatch.fnmatch(File, '*.JPG')) == False):
                    File = random.choice(os.listdir(os.getcwd()))
            elif(fnmatch.fnmatch(File, '*.jpg')):
                while ((File in Used) or (fnmatch.fnmatch(File, '*.jpg')) == False):
                    File = random.choice(os.listdir(os.getcwd()))

            #If file type unknown continue
            else:
                print("Unknown file type")
                continue

            #Create new file name
            FileName = (Dir + File)

            #Copy and move with new name
            shutil.copy(File, RandomDirectory + FileName)

            #Add file to used list and update counter
            Used.append(File)
            i = i + 1

    #Change back to Brigade directories
    print("")
    os.chdir("..")
    os.chdir("..")
