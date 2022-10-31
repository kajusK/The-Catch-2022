import os
from PIL import Image


box_position = (140, 120)
box_color = (0, 137, 75)
background_color = (242, 121, 48)


def is_similar(pixel, color):
    sum = 0
    for i in range(3):
        sum += abs(pixel[i] - color[i])

    return sum < 50


for root,_,files in os.walk('.'):
    if not len(files):
        continue

    for f in files:
        if not f.endswith('.png'):
            continue

        filename = os.path.join(root, f)
        im = Image.open(filename)
        pixels = im.load()

        if is_similar(pixels[0, 0], background_color) and is_similar(pixels[box_position], box_color):
            im.show()
            im.close()
            exit()
        im.close()
