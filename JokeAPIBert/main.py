from flask import Flask, render_template, request

import pandas as pd
import numpy as np

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text


#-------------------------------------------

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
        prediction = tf.sigmoid(model(tf.constant(sentence)))
        percentage = prediction[0][0]*100
        isFunny = isFunnyTxt(prediction)
    return render_template('index.html', joke=joke, isFunny=isFunny, percentage=percentage)


if __name__ == '__main__':

    global model
    model =  tf.saved_model.load('/model')

    app.run(debug=False, host='0.0.0.0', port=8080)