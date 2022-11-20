import pandas as pd
from sklearn.model_selection import train_test_split
import os
import shutil



def split_csv_into_dir(csv_name, label, feature):

    # Read in dataset
    data = pd.read_csv(csv_name)

    # Use mask to split list into pos and neg
    mask = data[label] == True
    pos, neg = data[mask], data[~mask]

    # Split pos data and neg into train and test set
    data = {'train': {'pos': [],'neg': [],},'test': {'pos': [],'neg': [],}}
    data['train']['pos'], data['test']['pos'] = train_test_split(pos, test_size=0.2)
    data['train']['neg'], data['test']['neg'] = train_test_split(neg, test_size=0.2)

    # Create Folder structure and save files into it 
    # Code fails if folders already exist
    train_test_dirs = ['test', 'train']
    pos_neg_dirs = ['pos', 'neg']
    for train_test_dir in train_test_dirs:
        try:
            os.mkdir(train_test_dir)
        except FileExistsError:
            pass

        
        for pos_neg_dir in pos_neg_dirs:
            new_dir = os.path.join(train_test_dir, pos_neg_dir)
            try:
                os.mkdir(new_dir)
            except FileExistsError:
                shutil.rmtree(new_dir)
                os.mkdir(new_dir)
                pass
            
            for idx, row in data[train_test_dir][pos_neg_dir].reset_index(drop=True).iterrows():
                #create new file named after current index
                with open(os.path.join(new_dir, str(idx)+".txt"), "w") as file:
                    # write the text into the new file
                    file.write(row[feature])

csv_name = 'dataset.csv'
label = 'humor'
feature = 'text'

split_csv_into_dir(csv_name, label, feature)