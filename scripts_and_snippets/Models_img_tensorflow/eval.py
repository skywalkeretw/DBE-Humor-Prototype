import os
import pandas as pd
import tensorflow as tf
import numpy as np
import shutil
import sys
import tensorflow_hub as hub
import tensorflow_text as text

ourExamples = pd.read_csv('ourExamples.csv')
#os.chdir("/models")
directories_in_curdir = sorted(list(filter(os.path.isdir, os.listdir(os.curdir))))
#directories_in_curdir = sorted(os.listdir("/models"))

available_models = [i for i in directories_in_curdir if i.startswith('model_')]

# Create Dataframe with Models and senteces 
header =  ourExamples['Sentence'].to_numpy().tolist()
header.insert(0, "MODEL")
evaluation = pd.DataFrame(columns=header)

#Loop over each model to create a row with values

for model in available_models:
    reloaded_model = tf.saved_model.load(model)
    reloaded_results = tf.sigmoid(reloaded_model(tf.constant(ourExamples['Sentence'])))
    results = [item for sublist in np.array(reloaded_results.numpy()).tolist() for item in sublist]
    row = [model] + results
    evaluation.loc[len(evaluation)] = row

fname ='result.csv'
evaluation.to_csv(fname, sep=',', encoding='utf-8')
with open(fname, "r") as f:
    shutil.copyfileobj(f, sys.stdout)