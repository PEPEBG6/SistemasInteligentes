options = ["piedra", "tijeras", "papel"]

def search_winner(player1, player2):
    if player1 == player2:
        result = 0
    elif player1 == "piedra" and player2 == "tijeras":
        result = 1
    elif player1 == "piedra" and player2 == "papel":
        result = 2
    elif player1 == "tijeras" and player2 == "piedra":
        result = 2
    elif player1 == "tijeras" and player2 == "papel":
        result = 1
    elif player1 == "papel" and player2 == "piedra":
        result = 1
    elif player1 == "papel" and player2 == "tijeras":
        result = 2
    return result

resultado = (search_winner("piedra","tijeras"))
print("Gana el jugador ",resultado)

test = [
    ["piedra", "piedra",0],
    ["piedra","tijeras",1],
    ["piedra", "papel",2]
]

for partida in test:
    print ("Player 1: %s player 2: %s Winner: %s Validation: %s"
           % (
                partida[0],
                partida[1],
                search_winner(partida[0], partida[1]),
                partida[2])
           )

    from random import choice
    def get_choice():
        return choice(options)
    
    for i in range(10):
        player1 = get_choice()
        player2 = get_choice()
        print("player 1: %s player 2: %s Winner: %s" % (player1, player2, search_winner(player1, player2)))

    def srt_to_listo(option):
        if option == "piedra":
            res = [1,0,0]
        elif option == "tijeras":
            res = [0,1,0]
        else:
            res = [0,0,1]
        return res
data_X = list(map(srt_to_listo, ["piedra", "tijeras", "papel"]))
data_Y = list(map(srt_to_listo, ["papel", "piedras", "tijeras"]))

print(data_X)
print(data_Y)

#iniciamos la red neuronal
#intalar libreria sklearn
from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(verbose=False, warm_start=True)

model = clf.fit([data_X[0]], [data_Y[0]])
print(model)

def play_and_learn(iters=10, debug=False):
    score = {"WIN":0, "LOSE":0}

    data_X = []
    data_Y = []

    for i in range(iters):
        player1 = get_choice()

        predict = model.predict_proba([srt_to_listo(player1)])[0]

        if predict[0] >= 0.95:
            player2 = options[0]
        elif predict[1] >= 0.95:
            player2 = options[1]
        elif predict[2] >=0.95:
            player2 =  options[2]
        else:
            player2 = get_choice()

        if debug==True:
            print("Player1: %s Player2 (modelo): %s -->%s" % (player1, predict, player2))
        
        winner = search_winner(player1, player2)
        if debug==True:
            print("Comprobamos: P1 vs P2: %s" % (winner))

        if winner == 2:
            data_X.append(srt_to_listo(player1))
            data_Y.append(srt_to_listo(player2))

            score["WIN"]+=1

        else:
            score["LOSE"]+=1
    return score, data_X, data_Y

score, data_X, data_Y = play_and_learn(1, debug=True)
print(data_X)
print(data_Y)
print("Score: %s %s %%" %(score, (score["WIN"]*100/(score["WIN"]+score["LOSE"]))))
if len(data_X):
    model = model.partial_fit(data_X, data_Y)

i=0
historic_pct = []
while True:
    i+=1
    score, data_X, data_Y = play_and_learn(1000, debug=False)
    pct = (score["WIN"]*100 / (score["WIN"]+ score["LOSE"]))
    historic_pct.append(pct)
    print("Items %s -score: %s %s %%" %(i, score, pct))

    if len(data_X):
        model = model.partial_fit(data_X, data_Y)

    if sum(historic_pct[-9:]) == 900:   
        break


import matplotlib.pyplot as plt
import numpy as np

x = range(len(historic_pct))
y = historic_pct

fig, ax = plt.subplots()
ax.set_ylabel('%')
ax.set_xlabel('Iter')
ax.set_title("Procentaje de aprendizake de iteración")
plt.plot(x,y)
plt.show()