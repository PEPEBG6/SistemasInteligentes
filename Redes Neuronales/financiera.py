import numpy as np
from keras.models import Sequential
from keras.layers import Dense


np.random.seed(7)

# Generar datos sintéticos
num_samples = 100
num_features = 4

# Estado Civil: Soltero=0, Casado=1, Divorciado=2
estado_civil = np.random.randint(0, 3, num_samples)

# Género: Hombre=0, Mujer=1
genero = np.random.randint(0, 2, num_samples)

# Edad: entre 18 y 70 años
edad = np.random.randint(18, 71, num_samples)

# Ingresos: entre 10,000 y 999,999,999
ingresos = np.random.randint(10000, 1000000000, num_samples)


fiabilidad = np.zeros(num_samples)

for i in range(num_samples):
   
    if edad[i] >= 25 and ingresos[i] >= 29000:
        fiabilidad[i] = 1
    else:
        fiabilidad[i]=0

# Concatenar datos en una matriz de características
X = np.column_stack((estado_civil, genero, edad, ingresos))


max_ingresos = np.max(X[:, 3])
X[:, 3] = X[:, 3] / max_ingresos

# Definir etiquetas de salida
Y = fiabilidad

# Crear modelo
model = Sequential()
model.add(Dense(12, input_dim=num_features, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar modelo
history = model.fit(X, Y, epochs=100, batch_size=10, verbose=1)

# Evaluar modelo
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# Generar datos de prueba
num_test_samples = 5

estado_civil_test = np.random.randint(0, 3, num_test_samples)
genero_test = np.random.randint(0, 2, num_test_samples)
edad_test = np.random.randint(18, 71, num_test_samples)
ingresos_test = np.random.randint(10000, 1000000000, num_test_samples)

X_test = np.column_stack((estado_civil_test, genero_test, edad_test, ingresos_test))
X_test[:, 3] = X_test[:, 3] / max_ingresos

# Realizar predicciones
predictions = model.predict(X_test)
print("Predicciones de fiabilidad:")
print(predictions)
