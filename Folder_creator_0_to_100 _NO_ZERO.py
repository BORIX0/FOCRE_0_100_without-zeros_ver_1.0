# Welcome Folder creator 0 to 100 ver 1.0.(WITHOUT ZEROS) this tool creates 100 folders in a order. Like this = 1,2,3,4,5,6,10,20,50,60,80,100.
# TOOL NAME: FOLDER_CREATOR_0_to_100 (WITHOUT ZEROS) AND VERSION IS =  1.0 version... :) ...


import os 

# here you need to put your own path where you want the folders to be :)

path= 'D:\\res'
os.chdir(path)
for i in range (1,10):
        NewFolder='' + str(i)
        os.makedirs(NewFolder)

# same with here put the same path here too!

path= 'D:\\res'
os.chdir(path)
for i in range (10,101):
        NewFolder='' + str(i)
        os.makedirs(NewFolder)

print("Thank me later :) ")

#made by BORIX
