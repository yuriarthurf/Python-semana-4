import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

a = np.arange(25).reshape(5, 5)

#1
row = a[[0,2,3], :]
media_1 = np.mean(row)
#print(media_1)

#2
column = a[:, [0,1, -1]]
media_2 = np.mean(column)
#print(media_2)

#3
indice_diagonal_1 = np.arange(5)
diagonal = a[indice_diagonal_1, indice_diagonal_1]
row = a[::-1]
diagonal2 = np.diagonal(row)
soma = sum(diagonal2) + sum(diagonal)
#print(soma)