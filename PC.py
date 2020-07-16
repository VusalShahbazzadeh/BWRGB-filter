from PIL import Image
from math import sqrt
import numpy as np

img = Image.open('Example.png')
# img = img.resize((300, 300))
size = img.size
pixels = img.load()

pixel_array = []

for i in range(size[1]):
    for j in range(size[0]):
        pixel_array.append([pixels[j, i][0], pixels[j, i][1], pixels[j, i][2], j, i])

from sklearn.cluster import KMeans

classifier = KMeans(n_clusters=100, init='k-means++')
classifier.fit(pixel_array)
centers = classifier.cluster_centers_

preds = classifier.predict(pixel_array)

for z in range(len(pixel_array)):
    j, i = pixel_array[z][3], pixel_array[z][4]
    pred = int(centers[preds[z]][0]), int(centers[preds[z]][1]), int(centers[preds[z]][2]), pixels[j, i][3] if len(
        pixels[j, i]) == 4 else 255
    pixels[j, i] = pred

img.show()
img.save('PCExample.png')
