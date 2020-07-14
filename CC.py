from PIL import Image
from math import sqrt
import numpy as np

img = Image.open('Example.png')
size = img.size
pixels = img.load()

# Modify only below this
brightness_scaler = 1

colors = [
    (255, 0, 0),
    (0, 0, 0),
    (255, 255, 0)
]

use_auto_color_choice = False
number_of_colors = 7
# Modify only above this
if use_auto_color_choice:
    pixel_array = []

    for i in range(size[1]):
        for j in range(size[0]):
            pixel_array.append(pixels[j, i])

    pixel_array = np.asarray(pixel_array)

    from sklearn.cluster import KMeans

    classifier = KMeans(n_clusters=number_of_colors, init='k-means++')
    classifier.fit(pixel_array)

    centers = classifier.cluster_centers_


    def array3_to_tuple_int(array):
        return int(array[0]), int(array[1]), int(array[2])


    tuple_centers = []

    for i in range(len(centers)):
        tuple_centers.append(array3_to_tuple_int(centers[i]))

    colors = tuple_centers


def dis(c1, c2):
    diss = 0
    for i in range(3):
        diss += (c1[i] - c2[i]) ** 2
    return sqrt(diss)


def set_brightness(color, scale):
    return color[0] * scale, color[1] * scale, color[2] * scale, 255 if len(color) == 3 else color[3]


for i in range(size[1]):
    for j in range(size[0]):
        mindist = 100000000000
        tempcolor = (0, 0, 0)
        pixel = pixels[j, i]
        pixel = set_brightness(pixel, brightness_scaler)
        for z in range(len(colors)):
            tempdist = dis(pixel, colors[z])
            if tempdist < mindist:
                tempcolor = colors[z]
                mindist = tempdist

        pixels[j, i] = tempcolor if len(pixels[j, i]) == 3 else (
            tempcolor[0], tempcolor[1], tempcolor[2], pixels[j, i][3])

img.save('CCExample.png')
