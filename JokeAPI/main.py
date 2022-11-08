from flask import Flask, render_template, request
import json
import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

app=Flask(__name__)

vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 20000

# Desired accuracy of the training
DESIRED_ACCURACY = 0.922

def isFunnyTxt(prediction):
    ret = ""
    if len(prediction) > 1:
        for  v in enumerate(prediction):
            if v > 0.5:
                ret =  "is Funny" + str(v[0]*100) + "%"
            else:
                ret = "is Not Funny" + str(v[0]*100) + "%"
    else:
        if prediction > 0.5:
            ret =  "is Funny"
        else:
            ret = "is Not Funny"
    
    return ret

# callback function used to end training after DESIRED_ACCURACY is reached will stop even if epochs are still missing
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if (logs.get('accuracy')>DESIRED_ACCURACY):
            print(f"\nReached {DESIRED_ACCURACY * 100}% accuracy so cancelling training!", )
            self.model.stop_training = True

# Function to be called befor route function is called train the model that should be used to detect humor
@app.before_first_request
def _setup():
    data = pd.read_csv('/dataset.csv')

    sentences = data['text']
    labels = data['humor']

    training_sentences = sentences[0:training_size]
    testing_sentences = sentences[training_size:]
    training_labels = labels[0:training_size]
    testing_labels = labels[training_size:]

    global tokenizer
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(training_sentences)

    word_index = tokenizer.word_index

    training_sequences = tokenizer.texts_to_sequences(training_sentences)
    training_padded = pad_sequences(training_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

    testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
    testing_padded = pad_sequences(testing_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

    # Need this block to get it to work with TensorFlow 2.x
    training_padded = np.array(training_padded)
    training_labels = np.array(training_labels)
    testing_padded = np.array(testing_padded)
    testing_labels = np.array(testing_labels)
    global model
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

    num_epochs = 30
    callbacks = myCallback()
    model.fit(training_padded, training_labels, epochs=num_epochs, validation_data=(testing_padded, testing_labels), verbose=2, callbacks=[callbacks])


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
        print(joke)
        sentence.append(joke)
        sequences = tokenizer.texts_to_sequences(sentence)
        padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
        prediction = model.predict(padded)
        percentage = prediction[0][0]*100
        isFunny = isFunnyTxt(prediction)
    return render_template('index.html', joke=joke, isFunny=isFunny, percentage=percentage)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)