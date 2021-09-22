import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = np.array(Image.open('python_image.jpg'))
print('Shape da imagem: {}, dtype: {}'.format(image.shape, image.dtype))
media = np.mean(image, axis=(0,1))
media_canal_1 = np.mean(image[:,:,0])
media_canal_2 = np.mean(image[:,:,1])
media_canal_3 = np.mean(image[:,:,2])
image2 = image - (media_canal_1 + media_canal_2 + media_canal_3)
plt.imshow((image2*255).astype(np.uint8))
plt.show()
