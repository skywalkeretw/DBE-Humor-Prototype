import pandas as pd
from sklearn.model_selection import train_test_split
import os
import shutil

# Read in dataset
jokes = pd.read_csv('dataset.csv')

# Use mask to split list into funny and not_funny
mask = jokes['humor'] == True
funny, not_funny = jokes[mask], jokes[~mask]

# Split funny and not_funny into train and test set
data = {'train': {'pos': [],'neg': [],},'test': {'pos': [],'neg': [],}}
data['train']['pos'], data['test']['pos'] = train_test_split(funny, test_size=0.2)
data['train']['neg'], data['test']['neg'] = train_test_split(not_funny, test_size=0.2)

# Create Folder structure and save files into it 
# Code fails if folders already exist
data_dir = ['test', 'train']
split_dir = ['pos', 'neg']
for d in data_dir:
    try:
        os.mkdir(d)
    except FileExistsError:
        pass

    
    for sd in split_dir:
        new_dir = os.path.join(d, sd)
        try:
            os.mkdir(new_dir)
        except FileExistsError:
            shutil.rmtree(new_dir)
            os.mkdir(new_dir)
            pass
        
        reindexed = data[d][sd].reset_index(drop=True)
        for idx, row in reindexed.iterrows():
            filename = os.path.join(new_dir, str(idx)+".txt")
            with open(filename, "w") as file:
                file.write(row.text)
