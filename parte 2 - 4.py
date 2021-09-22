import numpy as np
import matplotlib.pyplot as plt


def plot_triangle(vertices, center=None):
    trishape = plt.Polygon(vertices, edgecolor='r', alpha=0.2, lw=5)
    _, ax = plt.subplots(figsize=(4, 4))
    ax.add_patch(trishape)
    ax.set_ylim([.5, 3.5])
    ax.set_xlim([.5, 3.5])
    if center is not None:
        ax.scatter(*center, color='g', marker='D', s=70)
    ax.scatter(vertices[:, 0], vertices[:, 1], color='b', s=70)
    plt.show()


coordenadas = np.array([[1, 1], [3, 1], [2, 3]])

mediana1 = 1, 3, 2
mediana2 = 1, 1, 3
x = (sum(mediana1)) / 3
y = (sum(mediana2)) / 3
print(x, y)

plot_triangle(coordenadas, center=[2.0, 1.7])
