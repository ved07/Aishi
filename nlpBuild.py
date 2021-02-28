import numpy as np

import time
from mlp import multiLayeredPerceptron
network = multiLayeredPerceptron()
initialisedData = network.dataFrameInit('data.csv')
#print(nps.get_most_similar_symptoms("tirednese"))


mlp = network.runNeuralNet(dataFrame=initialisedData)
def pred(input_data):
    global mlp
    diag = network.initPredData(initialisedData, input_data)
    pred = network.predict(diag, initialisedData, 0, mlp)
    while pred == None:
        mlp = network.runNeuralNet(dataFrame=initialisedData)
        pred = network.predict(diag, initialisedData, 0, mlp)
    return (pred)
pred(initialisedData["Common Cold"])