from PIL import Image

img = Image.open('Example.png')
size = img.size
pixels = img.load()

for i in range(size[1]):
    for j in range(size[0]):
        if (len(pixels[0, 0]) == 4):
            (R, G, B, A) = img.getpixel((j, i))
            MMM = list((R, G, B))
            MMM.sort()
            T = MMM[1]
            if (G == MMM[2]):
                pixels[j, i] = (R, T, B, A)
            elif (R == MMM[2]):
                pixels[j, i] = (T, G, B, A)
            elif (B == MMM[2]):
                pixels[j, i] = (R, G, T, A)
        elif (len(pixels[0, 0]) == 3):
            (R, G, B) = img.getpixel((j, i))
            MMM = list((R, G, B))
            MMM.sort()
            T = MMM[1]
            if (G == MMM[2]):
                pixels[j, i] = (R, T, B)
            elif (R == MMM[2]):
                pixels[j, i] = (T, G, B)
            elif (B == MMM[2]):
                pixels[j, i] = (R, G, T)


img.show()
img.save('BWCMYExample.png')
