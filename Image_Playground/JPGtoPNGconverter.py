import sys
import os
from PIL import Image
from os import listdir

#grab first and second argument

input_path = sys.argv[1]
output_path = sys.argv[2]

#print(input_path, output_path) # command : python JPGtoPNGconverter.py pokedesk new
#check is new\ exists, if not create
if not os.path.exists(output_path):
    os.mkdir(output_path)


#loop through pokedex
for filename in os.listdir(input_path):
    img = Image.open(f'{input_path}\{filename}')
    img.save(f'{output_path}\{filename}.png','png')
    print('all done')

#convert img to png
#save to the new folder