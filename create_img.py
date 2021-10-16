from PIL import Image, ImageFont

font_siza = 16
font = ImageFont.truetype("Tahoma.ttf", font_siza)

for char in "ABCDEFGHIJ":
    im = Image.Image()._new(font.getmask(char))
    im.save("train/16/"+char+".bmp")


font_siza = 32
font = ImageFont.truetype("Tahoma.ttf", font_siza)

for char in "ABCDEFGHIJ":
    im = Image.Image()._new(font.getmask(char))
    im.save("train/32/"+char+".bmp")

font_siza = 64
font = ImageFont.truetype("Tahoma.ttf", font_siza)

for char in "ABCDEFGHIJ":
    im = Image.Image()._new(font.getmask(char))
    im.save("train/64/"+char+".bmp")
