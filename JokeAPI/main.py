from flask import Flask, render_template, request
import json
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app=Flask(__name__)
vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'

def isFunnyTxt(prediction):
    ret = ""
    if len(prediction) > 1:
        for  v in enumerate(prediction):
            if v > 0.5:
                ret =  "is funny" + str(v[0]*100) + "%"
            else:
                ret = "is not funny" + str(v[0]*100) + "%"
    else:
        if prediction > 0.5:
            ret =  "is funny"
        else:
            ret = "is not funny"
    
    return ret


#http://localhost:8082/isfunny/My%20IQ%20test%20results%20came%20back.%20They%20were%20negative.
#endpoint to check if a joke passed is funny or not
@app.route("/isfunny/<joke>")
def is_joke(joke):
    sentence = []
    print(joke)
    sentence.append(joke)
    sequences = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    isFunny = isFunnyTxt(model.predict(padded))
    return joke + " : " +isFunny


@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    isFunny = ""
    joke = ""
    percentage = ""

    if request.method == 'POST':
        joke = request.form['joke']
        sentence = []
        sentence.append(joke)
        sequences = tokenizer.texts_to_sequences(sentence)
        padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
        prediction = model.predict(padded)
        percentage = prediction[0][0]*100
        isFunny = isFunnyTxt(prediction)
    return render_template('index.html', joke=joke, isFunny=isFunny, percentage=percentage)


if __name__ == '__main__':

    global model
    model = tf.keras.models.load_model('joke')

    global tokenizer

    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    app.run(debug=True, host='0.0.0.0', port=8080)