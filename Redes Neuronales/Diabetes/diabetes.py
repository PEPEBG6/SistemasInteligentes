#crea tu primer MLP en Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy

#Fija las semillas aleatorias para la reproducibilidad
numpy.random.seed(7)

#carga los datos
dataset =  numpy.loadtxt("Diabetes/pima-indians-diabetes.csv", delimiter=",")
#dividido en varibales de entrada (X) y salida (Y)
X = dataset[:,0:8]
Y = dataset[:,8]

#crea el modelo
model = Sequential()
model.add(Dense(12, input_dim=8, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

#compila el modelo--
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Ajusta el modelo
model.fit(X, Y, epochs=150, batch_size=10)

#evalua el modelo
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# Calcula las predicciones
predictions = model.predict(X)
print (predictions)

# Redondeamos las predicciones
rounded = [round(x[0]) for x in predictions]
print(rounded)