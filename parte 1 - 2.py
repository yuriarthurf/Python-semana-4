import numpy as np
import matplotlib.pyplot as plt

a = np.arange(25).reshape(5, 5)
print(np.sum(a>10) + np.sum(a%2 == 0))