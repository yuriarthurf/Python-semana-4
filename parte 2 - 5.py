import numpy as np
import math


def normalização(x):
    x = np.asarray(x)
    return (x - x.min()) / math.sqrt((np.ptp(x**2).sum()))


a = np.random.normal(size=(20, 100))

print(normalização(a))
