import re
import pandas as pd
from deep_translator import GoogleTranslator
import nltk

nltk.download()
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.corpus import wordNetLemmatizer    


#Paso 1: Limpiaar y traduccion del texto

#Cargamos el archivo con los comentarios
data = pd.read_csv(filepath_or_buffer='Análisis de Sentimientos o Minería de Opiniones/Ejercicio1/comentarios.csv', delimiter=",")
data.head()

#Eliminamos la columna Unnamed:1
mydata = data.drop('Unnamed: 1', axis=1)
mydata.head()
print(mydata)

#Traducimos el texto de Español a Ingles
translator = GoogleTranslator(source="es", target="en")
mydata.review = mydata.review.apply(translator.translate)
print(mydata)

#Funcion para limpiar el texto del archivo
def clean(text):
    #Removemos los caracteres y numeros que no se ocuparan
    text = re.sub('[^A-Za-z]+','',text)
    return text

#Limpiamos el texto en la columna comentario
mydata['Cleaned_Reviews'] = mydata['review'].apply(clean)
mydata.head()
print(mydata)

#Paso2:
# 2.1 Tokenizacion = Es el proceso para dividir el texto en diferentes partes llamadas tokens
# 2.2 Etiquetado POS(Etiquetado gramatical): Es el proceso de conversacion de cada token en un tupla que tiene la forma (palabra, etiqueta)
# 2.3 Eliminacion de palabras irrelevantes

#Generamos el diccionario de etiquetado gramatical
# J = Adjetivo  V = Verbo  N = sustantivo y R = Adverbio