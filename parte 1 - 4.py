import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = np.array(Image.open('python_image.jpg'))
print('Shape da imagem: {}, dtype: {}'.format(image.shape, image.dtype))
plt.imshow(image)
plt.show()

print(np.sum(np.sum(image, axis=2) == 0))

pixeis_pretos = np.sum(image == 0)
print(pixeis_pretos)