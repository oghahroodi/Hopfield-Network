from PIL import Image, ImageFont
from random import randint
import numpy as np

font_siza = 16
font = ImageFont.truetype("Tahoma.ttf", font_siza)

for char in "ABCDEFGHIJ":
    im = Image.Image()._new(font.getmask(char))
    data = np.array(im)
    for i in data:
        for j in range(len(i)):
            r = randint(1, 10)
            if r <= 1:
                i[j] = 0
                rescaled = (255.0 / data.max() *
                            (data - data.min())).astype(np.uint8)
                im = Image.fromarray(rescaled)
    im.save("test/16-10/"+char+".bmp")

    im = Image.Image()._new(font.getmask(char))
    data = np.array(im)
    for i in data:
        for j in range(len(i)):
            r = randint(1, 10)
            if r <= 3:
                i[j] = 0
                rescaled = (255.0 / data.max() *
                            (data - data.min())).astype(np.uint8)
                im = Image.fromarray(rescaled)
    im.save("test/16-30/"+char+".bmp")

    im = Image.Image()._new(font.getmask(char))
    data = np.array(im)
    for i in data:
        for j in range(len(i)):
            r = randint(1, 10)
            if r <= 6:
                i[j] = 0
                rescaled = (255.0 / data.max() *
                            (data - data.min())).astype(np.uint8)
                im = Image.fromarray(rescaled)
    im.save("test/16-60/"+char+".bmp")

font_siza = 32
font = ImageFont.truetype("Tahoma.ttf", font_siza)

for char in "ABCDEFGHIJ":
    im = Image.Image()._new(font.getmask(char))
    data = np.array(im)
    for i in data:
        for j in range(len(i)):
            r = randint(1, 10)
            if r <= 1:
                i[j] = 0
                rescaled = (255.0 / data.max() *
                            (data - data.min())).astype(np.uint8)
                im = Image.fromarray(rescaled)
    im.save("test/32-10/"+char+".bmp")

    im = Image.Image()._new(font.getmask(char))
    data = np.array(im)
    for i in data:
        for j in range(len(i)):
            r = randint(1, 10)
            if r <= 3:
                i[j] = 0
                rescaled = (255.0 / data.max() *
                            (data - data.min())).astype(np.uint8)
                im = Image.fromarray(rescaled)
    im.save("test/32-30/"+char+".bmp")

    im = Image.Image()._new(font.getmask(char))
    data = np.array(im)
    for i in data:
        for j in range(len(i)):
            r = randint(1, 10)
            if r <= 6:
                i[j] = 0
                rescaled = (255.0 / data.max() *
                            (data - data.min())).astype(np.uint8)
                im = Image.fromarray(rescaled)
    im.save("test/32-60/"+char+".bmp")


font_siza = 64
font = ImageFont.truetype("Tahoma.ttf", font_siza)

for char in "ABCDEFGHIJ":
    im = Image.Image()._new(font.getmask(char))
    data = np.array(im)
    for i in data:
        for j in range(len(i)):
            r = randint(1, 10)
            if r <= 1:
                i[j] = 0
                rescaled = (255.0 / data.max() *
                            (data - data.min())).astype(np.uint8)
                im = Image.fromarray(rescaled)
    im.save("test/64-10/"+char+".bmp")

    im = Image.Image()._new(font.getmask(char))
    data = np.array(im)
    for i in data:
        for j in range(len(i)):
            r = randint(1, 10)
            if r <= 3:
                i[j] = 0
                rescaled = (255.0 / data.max() *
                            (data - data.min())).astype(np.uint8)
                im = Image.fromarray(rescaled)
    im.save("test/64-30/"+char+".bmp")

    im = Image.Image()._new(font.getmask(char))
    data = np.array(im)
    for i in data:
        for j in range(len(i)):
            r = randint(1, 10)
            if r <= 6:
                i[j] = 0
                rescaled = (255.0 / data.max() *
                            (data - data.min())).astype(np.uint8)
                im = Image.fromarray(rescaled)
    im.save("test/64-60/"+char+".bmp")
