from PIL import Image
from math import sqrt

img = Image.open('Example.png')
size = img.size
pixels = img.load()

brightness_scaler = 1
colors = [
    (255, 0, 0),
    (255, 255, 0),
    (0, 0, 0)
]


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
