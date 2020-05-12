"""

PRETTIFY CLARIFAI JSON RESPONSE AND SAVE IT TO A DATAFRAME THEN A CSV FILE.

"""

import pandas as pd
import json
import os

# set the path of the json file
path_json = 'PATH TO THE JSON.json'
root_dir = 'PATH TO THE DIR TO SAVE THE CSV FILE IN'

fileName = path_json.split('/')[-1].split('.')[0]
saveName = fileName + '.csv'

save_path = root_dir,'/',saveName

# Read the json file 
with open(path_json) as f:
    data = json.load(f)

# Iterate through the json object and save concept with their predicted values in a dictionary
data_dict = {}
for k,v in data['outputs'][0]['data'].items():
    
    for val in v: 
        print(val['name'],':', val['value'])
        
        data_dict[val['name']] = val['value']
        print('Value appended to the dictionary \n')

# Create a dataframe from the dictionary and then save that to a csv file
print('Creating a Dataframe\n ')
df = pd.DataFrame.from_dict(data_dict, orient='index').reset_index()        
df.columns = ['Concept', 'Probability']
print('DataFrame created, writing it to a csv in: \n', save_path, 'as \n', saveName)


df.to_csv('PATH TO SAVE/fileName2Save.csv', index= False)

print('\n CSV file created.')
