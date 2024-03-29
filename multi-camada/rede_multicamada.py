# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:03:13 2019

@author: Jeferson-PC
"""

import numpy as np

#Funcao de ativação sigmoid
def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

#a = sigmoid(-50)
    
entradas = np.array([[0,0],
                    [0,1],
                    [1,0],
                    [1,1]])
    
saidas = np.array([0,1,1,0])

pesos0 = np.array([[-0.424, -0.740, -0.961],
                   [0.358,-0.577,-0.469]])

pesos1 = np.array([[-0.017],[-0.893],[0.148]])

#tempo de treinamento
epocas = 100

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada,pesos0)
    camadaOculta = sigmoid(somaSinapse0)