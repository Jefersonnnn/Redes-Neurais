# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 13:31:37 2019

@author: Jeferson
"""
import numpy as np

entradas = np.array([-1,7,5])
pesos = np.array([0.8,0.1,0])

def soma(e, p):
#e.dot(p) representa
#(ei * pi) + (ei2 * pi2) + ()....
   return e.dot(p)
# dot product / produto escalar
        
s = soma(entradas, pesos)

def stepfunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepfunction(s)