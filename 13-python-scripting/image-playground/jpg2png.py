import sys
import os
from PIL import Image

# python3 jpg2png.py Pokedex/ new/
# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# check is new/exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex
# convert images to png
# save to the new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')
