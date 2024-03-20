import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

# Semilla aleatoria para reproducibilidad
np.random.seed(7)

# Generar datos sintéticos
num_samples = 150
num_features = 4

# Salud: Débil=0, Medio=1, Fuerte=2
salud = np.random.randint(0, 3, num_samples)

# Tiene cuchillo: No=0, Sí=1
cuchillo = np.random.randint(0, 2, num_samples)

# Tiene arma: No=0, Sí=1    
arma = np.random.randint(0, 2, num_samples)

# Número de enemigos: entre 1 y 10
enemigos = np.random.randint(1, 11, num_samples)

# Acciones: Escapar=0, Andar=1, Atacar=2, Esconderse=3
acciones = np.zeros(num_samples)

#reglas de asociación para las acciones
for i in range(num_samples):
    if salud[i] == 0:  # Salud Débil
        if cuchillo[i] == 0 and arma[i] == 0 and enemigos[i] > 5:
            acciones[i] = 0  
        elif cuchillo[i] == 0 and arma[i] == 0 and enemigos[i] <= 5:
            acciones[i] = 3  
        elif cuchillo[i] == 0 and arma[i] == 1 and enemigos[i] > 5:
            acciones[i] = 0  
        elif cuchillo[i] == 0 and arma[i] == 1 and enemigos[i] <= 5:
            acciones[i] = 3  
        elif cuchillo[i] == 1 and arma[i] == 0 and enemigos[i] > 5:
            acciones[i] = 0  
        elif cuchillo[i] == 1 and arma[i] == 0 and enemigos[i] <= 5:
            acciones[i] = 3  
        elif cuchillo[i] == 1 and arma[i] == 1 and enemigos[i] > 5:
            acciones[i] = 0  
        elif cuchillo[i] == 1 and arma[i] == 1 and enemigos[i] <= 5:
            acciones[i] = 3  
    elif salud[i] == 1:  # Salud Media
        if cuchillo[i] == 0 and arma[i] == 0 and enemigos[i] > 5:
            acciones[i] = 0  
        elif cuchillo[i] == 0 and arma[i] == 0 and enemigos[i] <= 5:
            acciones[i] = np.random.choice([1, 3])  
        elif cuchillo[i] == 0 and arma[i] == 1 and enemigos[i] > 5:
            acciones[i] = 0  
        elif cuchillo[i] == 0 and arma[i] == 1 and enemigos[i] <= 5:
            acciones[i] = np.random.choice([1, 3])  
        elif cuchillo[i] == 1 and arma[i] == 0 and enemigos[i] > 5:
            acciones[i] = np.random.choice([0, 2])  
        elif cuchillo[i] == 1 and arma[i] == 0 and enemigos[i] <= 5:
            acciones[i] = np.random.choice([1, 3])  
        elif cuchillo[i] == 1 and arma[i] == 1 and enemigos[i] > 5:
            acciones[i] = np.random.choice([0, 2])  
        elif cuchillo[i] == 1 and arma[i] == 1 and enemigos[i] <= 5:
            acciones[i] = np.random.choice([1, 3])  
    elif salud[i] == 2:  # Salud Fuerte
        if cuchillo[i] == 0 and arma[i] == 0 and enemigos[i] > 5:
            acciones[i] = np.random.choice([0, 2])  
        elif cuchillo[i] == 0 and arma[i] == 0 and enemigos[i] <= 5:
            acciones[i] = np.random.choice([1, 2])  
        elif cuchillo[i] == 0 and arma[i] == 1 and enemigos[i] > 5:
            acciones[i] = np.random.choice([0, 2])  
        elif cuchillo[i] == 0 and arma[i] == 1 and enemigos[i] <= 5:
            acciones[i] = np.random.choice([1, 2])  
        elif cuchillo[i] == 1 and arma[i] == 0 and enemigos[i] > 5:
            acciones[i] = np.random.choice([0, 2]) 
        elif cuchillo[i] == 1 and arma[i] == 0 and enemigos[i] <= 5:
            acciones[i] = np.random.choice([1, 2])  
        elif cuchillo[i] == 1 and arma[i] == 1 and enemigos[i] > 5:
            acciones[i] = np.random.choice([0, 2])  
        elif cuchillo[i] == 1 and arma[i] == 1 and enemigos[i] <= 5:
            acciones[i] = np.random.choice([1, 2])  


X = np.column_stack((salud, cuchillo, arma, enemigos))

# Normalizar características
X = X / np.max(X, axis=0)

# Codificar las etiquetas de salida
Y = to_categorical(acciones, num_classes=4)

# Crear modelo
model = Sequential()
model.add(Dense(12, input_dim=num_features, activation='relu'))
model.add(Dense(8, activation='relu'))

# Capa de salida
model.add(Dense(4, activation='softmax'))

# Compilar el modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


X_train, X_eval = X[:-5], X[-5:]
Y_train, Y_eval = Y[:-5], Y[-5:]

# Ajustar el modelo a los datos de entrenamiento
model.fit(X_train, Y_train, epochs=120, batch_size=10, verbose=1)

# Predecir con nuevos datos
predictions = model.predict(X_eval)


predictions_percent = np.round(predictions * 100, 2)

# Aprender de los resultados
for i, prediction in enumerate(predictions_percent):
    if np.max(prediction) > 75:
        selected_action = np.argmax(prediction)
        print(f"Registro {i+1}: Predicción {prediction}%, Acción seleccionada: {selected_action}")
