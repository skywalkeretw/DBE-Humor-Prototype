from flask import Flask, render_template, request

import pandas as pd
import numpy as np

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text


#-------------------------------------------

# Configure Flask Server Framework
app=Flask(__name__)
vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'

def isFunnyTxt(prediction):
    ret = ""

    if prediction > 0.5:
        ret =  "is funny"
    else:
        ret = "is not funny"
    
    return ret

# home / root function that is called when Page is loaded or a sentence is checked
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
        prediction = tf.sigmoid(model(tf.constant(sentence))).numpy()[0][0].item()
        percentage = prediction*100
        isFunny = isFunnyTxt(prediction)
    # Template generation for flask pass specify the name of the template variable and its data 'varname=data' e.g joke=joke
    return render_template('index.html', joke=joke, isFunny=isFunny, percentage=percentage)


if __name__ == '__main__':

    global model
    # Load Trained Model
    model =  tf.saved_model.load('/model')
    # Run Server on Port 8080
    app.run(debug=False, host='0.0.0.0', port=8080)