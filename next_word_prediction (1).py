# -*- coding: utf-8 -*-
"""Next Word Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ABGPLwNKf-QLA10Ohost7ubsFNgtzv8q

CODE FOR PROJECT
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences # Fixed the typo: sequencve -> sequence
from tensorflow.keras.layers import Embedding # Fixed the typo: Layers -> layers
from tensorflow.keras.layers import Embedding, Dense, LSTM

with open('/content/sherlock-holm.es_stories_plain-text_advs.txt', 'r', encoding='utf-8') as file:
    text = file.read()

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in text.split('\n'):
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

max_sequence_len = max([len(seq) for seq in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

X = input_sequences[:, :-1]
y = input_sequences[:, -1]

y = np.array(tf.keras.utils.to_categorical(y, num_classes=total_words))

import tensorflow as tf

# Then use tf.keras.Sequential to define the model
model = tf.keras.Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequence_len-1))
model.add(LSTM(150))
model.add(Dense(total_words, activation='softmax'))
print(model.summary())

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

seed_text = "I love my"
next_words = 2

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted = np.argmax(model.predict(token_list), axis=-1)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word

print(seed_text)

seed_text = "i am proud"
next_words =3

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted = np.argmax(model.predict(token_list), axis=-1)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word

print(seed_text)

model.save('model2.h5')
model= tf.keras.models.load_model('model2.h5')
seed_text = "i am happy"
next_words =3

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted = np.argmax(model.predict(token_list), axis=-1)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word

print(seed_text)

"""CODE TO EXECUTE THE TRAINED MODEL IN SPYDER"""

import numpy as np
import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os

# Get the current directory of the script.
current_directory = os.getcwd()

# Build the file path relative to the current directory or your desired path
file_path = os.path.join(current_directory, 'sherlock-holm.es_stories_plain-text_advs.txt')
# If your data file is not in the same directory as the script, replace 'sherlock-holm...' with the actual relative or absolute path

# Attempt to open and read the file.
with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])

import os
os.getcwd()

import os
import tensorflow as tf

# Get the current directory of the script.
current_directory = os.getcwd()

# Build the file path relative to the current directory
file_path = os.path.join(current_directory, 'model2.h5')

# Load the model
model = tf.keras.models.load_model(file_path)

seed_text = "hi how are you hope"
next_words = 6

for _ in range(next_words):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=17, padding='pre')
    predicted = np.argmax(model.predict(token_list), axis=-1)
    output_word = ""
    for word, index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word

print(seed_text)

"""CODE TO CREATE A WEB APPLICATION Using STREAMLIT"""

import numpy as np
import tensorflow as tf
import streamlit as st

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('/content/sherlock-holm.es_stories_plain-text_advs.txt') as file:
    text = file.read()

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])

model2= tf.keras.models.load_model('/content/model2.h5')

#function
def pred(seed_text,next_words):

    for _ in range(int(next_words)):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=17, padding='pre')
        predicted = np.argmax(model2.predict(token_list), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word

    return seed_text

def main():

    #title for interface
    st.title("Next Word Prediction Web App")

    #getting the input data
    sentence=st.text_input('sentence to complete')
    no_of_words=st.text_input('number_of_words')

    str=''

    if st.button('Generate Words'):
        str=pred(sentence,no_of_words)

    st.success(str)

if __name__=='__main__':
    main()