import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

a = np.random.normal(loc=3, size=(50000, 2))
normalizado = preprocessing.normalize(a)
# media_colunas = np.mean(a, axis=1, keepdims=True)
# a2 = a - media_colunas
plt.hist2d(normalizado[:, 0], normalizado[:, 1], bins=100)
cbar = plt.colorbar()
cbar.ax.set_ylabel('Frequência')
plt.show()
