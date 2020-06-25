
"""
The purpose of this script is to go through folders and use those names to create concepts in an app

HOW TO LABEL THE FOLDERS:

The folders should be labeled with the names that are going to become concepts. 
    The names that I got were of the type 
                00_Engagement-Sessions
                01_Prep-Ceremony
                01a_First_Look 
                and so-on
    This scipt parses these names of the folders and gets rid of the numbers in the begining. 

Then it creates a list with those proper names and creates concepts with those names in 
the app whose API you provide. 


Provide path to the mainDir where all the folders containing the labeled folders with images 
in them. 
Provide the API key you generated for your app in app

"""
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import os

# Path to all the images 
mainDir = 'ENTER_PATH_TO_THE_FOLDER_WHERE_FOLDERS_CONTAINING_IMAGES_ARE_LOCATED.'

empty_folders = []
concept_list = []
for files in os.listdir(mainDir):
    if not files.startswith('.'): # This skips any hidden files which usually begin with .xyz 
        if len(os.listdir(mainDir+'/'+files)) == 0:
            concept_name = files.rsplit('_',1)
            empty_folders.append(concept_name[1])
            print(files , 'is empty\n')
        else:
            concept_name = files.rsplit('_',1)
            concept_list.append(concept_name[1])
            print(files, 'is good\n')
    else: 
        pass

# print('\nThere are ', len(empty_folders), empty_folders)

print('\nthe concepts are as follows:')

for x in range(len(concept_list)):
    print(concept_list[x])

#Provide the API key you generated for your app in app
app = ClarifaiApp(api_key = 'YOUR_API_KEY')
model = app.models.create('Eivan-model', concepts = concept_list)

