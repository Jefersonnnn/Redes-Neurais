# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:33:20 2019

@author: Jeferson-PC
"""

import numpy as np
#Tabela verdade operador E
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,0,0,1])

entradas = np.array([[0,0,0],
                     [0,0,1],
                     [0,1,1],
                     [1,1,1],
                     [1,0,0],
                     [1,0,1],
                     [1,1,0]
                     ])
saidas = np.array([0,1,1,1,1,1])

#Tabela verdade operador OU
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,1,1,1])

#Tabela verdade operador XOR
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saidas = np.array([0,1,1,0])
#pesos = np.array([0.0,0.0])
pesos = np.array([0.0,0.0,0.0])
taxaAprendizagem = 0.1

def stepfunction(soma):
    if (soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepfunction(s)

#Encontrar os pesos
#Minizando o erro
def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))

treinar()
print('Rede neural treinada')
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))
print(calculaSaida(entradas[4]))
print(calculaSaida(entradas[5]))