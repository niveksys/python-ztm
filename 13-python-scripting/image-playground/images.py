# pip3 install Pillow
from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print(img)
# print(dir(img))

print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('smooth.png', 'png')

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('sharpen.png', 'png')

filtered_img = img.convert('L')
filtered_img.save('grey.png', 'png')

filtered_img.show()

crooked = filtered_img.rotate(90)
crooked.save('rotate.png', 'png')

resize = filtered_img.resize((300, 300))
resize.save('resize.png', 'png')

box = (100, 100, 400, 400)
crop = filtered_img.crop(box)
crop.save('crop.png', 'png')

img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
img.show()
print(img.size)
