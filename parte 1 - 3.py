import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(0, 50, (5, 5))

a.sort()
print(np.where(a[:, 0], a, -1))