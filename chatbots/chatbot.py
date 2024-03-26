import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import numpy as np
import random
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

#importamos y cargamos el archivo JSON
randomwords = []
words = []
classes = []
documents = []
ignore_words =['¿', '?', '!']

data_file = open('chatbots/intents.json', encoding='utf-8').read()
intents = json.loads(data_file)
print(intents)

#preprocesamos los datos
#Creamos los tokens
#iteraremos a traves de los patrones y tokeniza
#y agregamos cada palabra en las lista de palbras
#nuestras etiquetas

for intent in intents['intents']:
    for pattern in intent['Patterns']:
        #tokenize each word
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        #agregamos el documento al corpus
        documents.append((w, intent['tag']))

        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#ahora lematizaremos cada palabra y eliminaremos
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
print(words)

pickle.dump(classes, open('classes.pkl', 'wb'))
pickle.dump(words, open('words.pkl', 'wb'))

#crear datos de entrenamiento y prueba
training = []
output_empy = [0] * len(classes)
for doc in documents:
    #Espacio para las palabras
    bag = []
    #lista de tokens
    pattern_words = doc[0]
    #separamos los tokens
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    #se crea nuestra matriz de palabras con 1, se se encuentra una coincidencia de 
    #en el patron actual y en caso de lo contrario se pondra un 0
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    
    output_row = list(output_empy)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
    print(training)

random.shuffle(training)
train_x = [t[0] for t in training]
train_y = [t[1] for t in training]

#se crea el modelo
model = Sequential()
model.add(Dense(128, input_shape = (len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(learning_rate = 0.01, decay = 1e-6, momentum= 0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer = sgd, metrics=['accuracy'])

hits = model.fit(np.array(train_x), np.array(train_y), epochs = 300, batch_size = 5, verbose = 1)
model.save('chatbot_model.h5', hits)