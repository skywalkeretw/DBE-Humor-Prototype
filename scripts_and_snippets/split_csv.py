import pandas as pd
from sklearn.model_selection import train_test_split
import os
import shutil



def split_csv_into_dir(csv_name, label, feature):

    # Read in dataset
    data = pd.read_csv(csv_name)
    total_data = len(data)
    print("---")
    print("Data has been read in")
    print(data.head())
    print("There are", total_data, "entries")
    print("")
    
    # Use mask to split list into pos and neg
    mask = data[label] == True
    pos, neg = data[mask], data[~mask]
    print("---")
    print("Data has been split into True and False\n")
    print("pos len:", len(pos))
    print(pos.head())
    print("\n-\n")
    print("neg len:", len(neg))
    print(neg.head())
    print("")
    
    # Split pos data and neg into train and test set
    data = {'train': {'pos': [],'neg': [],},'test': {'pos': [],'neg': [],}}
    data['train']['pos'], data['test']['pos'] = train_test_split(pos, test_size=0.2)
    data['train']['neg'], data['test']['neg'] = train_test_split(neg, test_size=0.2)
    print("---")
    print("Datasets Have been Split into train and test")
    print("")    

    # Create Folder structure and save files into it 
    # Code fails if folders already exist
    print("---")
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
                print("Cleaning Dir:", new_dir)
                shutil.rmtree(new_dir)
                os.mkdir(new_dir)
                pass
            print("Dir", new_dir, "has been created")
            
            data_len = len(data[train_test_dir][pos_neg_dir])
            
            for idx, row in data[train_test_dir][pos_neg_dir].reset_index(drop=True).iterrows():
                #create new file named after current index
                with open(os.path.join(new_dir, str(idx)+".txt"), "w") as file:
                    # write the text into the new file
                    file.write(row[feature])
            
            folder_content_len = 0
            for path in os.scandir(new_dir):
                if path.is_file():
                    folder_content_len += 1
            if data_len != folder_content_len:
                print('Dir ', new_dir ,'is missing Jokes', "Data:", data_len, "Dir Content", folder_content_len)
            else:
                print("All files have been Created!")
    print("Success")



# download our dataset from git this makes it easier to move our notebooks
csv_name = 'https://raw.githubusercontent.com/skywalkeretw/DBE-Humor-Prototype/master/Datasets/dataset.csv'
label = 'humor'
feature = 'text'

split_csv_into_dir(csv_name, label, feature)