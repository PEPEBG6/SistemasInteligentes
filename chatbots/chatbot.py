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

#Procesamos los datos
#Crearemos los tokens
#Iteraremos a traves de los patrones y tokenizacion
#y agregamos cada palabra en listas de palabras


for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            
#Ahora Lematizaremos cada palabra y eliminaremos 
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
print(words)

pickle.dump(classes,open('classes.pkl','wb'))
pickle.dump(words,open('words.pkl','wb'))

#Crear datos de entrenamiento y prueba
training = []
output_empty = [0] * len(classes)
for doc in documents:
    #Espacio para palabras
    bag=[]
    #Lista de tokens
    pettern_words = doc[0]
    #Separamos los tokens
    pattern_words = [lemmatizer.lemmatize(words.lower()) for word in pattern_words]
    
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
        
    output_row = list(output_empty)
    