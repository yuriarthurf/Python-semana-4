import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


dataset = np.loadtxt('wine_data.csv', delimiter=',')
dataset = dataset[:, :4] # ['Class label', 'Alcohol', 'Malic acid']
print(dataset.shape)

z_score = stats.zscore(dataset, axis=1)

plt.scatter(z_score[:, 1], z_score[:, 2], c=z_score[:, 0])
plt.title('Alcohol and Malic Acid content of the wine dataset')
plt.xlabel('Alcohol')
plt.ylabel('Malic acid')
plt.show()

# x_{i} = \frac{x_{i} - \mu_{i}}{\sigma_{i}}