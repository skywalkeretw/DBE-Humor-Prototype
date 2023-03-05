from flask import Flask, render_template, request

import json, math, random

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

def getAnswer(percentage):
    # rounds number up to the next 10 step e.g 0.1 -> 10, 33 -> 40, 91 -> 100
    answer = answers[str(int(math.ceil(percentage/ 10.0)) * 10)]
    # Get a random emoji and comment
    comment = random.choice(answer['comments'])
    emoji = random.choice(answer["emojis"])
    return comment, emoji

# home / root function that is called when Page is loaded or a sentence is checked
@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    joke = ""
    percentage = ""
    comment = ""
    emoji = ""
    if request.method == 'POST':
        joke = request.form['joke']
        sentence = []
        sentence.append(joke)
        prediction = tf.sigmoid(model(tf.constant(sentence))).numpy()[0][0].item()
        percentage = prediction*100
        comment, emoji = getAnswer(percentage) 
        percentage = round(percentage, 1)
    # Template generation for flask pass specify the name of the template variable and its data 'varname=data' e.g joke=joke
    return render_template('index.html', joke=joke, percentage=percentage, comment=comment, emoji=emoji)


if __name__ == '__main__':
    from waitress import serve
    global model
    # Load Trained Model
    model =  tf.saved_model.load('/model')
    global answers
    with open('answers.json') as json_file:
        answers = json.load(json_file)

    # Run Server on Port 8080
    #app.run(debug=False, host='0.0.0.0', port=8080)
    serve(app, host="0.0.0.0", port=8080)
