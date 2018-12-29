#Python 3 - Chris Luginbuhl
#replaces picStuff.py found in GANGogh repo (which seems to be written windows-specific).abs
#Resizes and renames files for processing with GANGogh. adjust size and path on lines 9-12.


import os
from PIL import Image

SIZE = 64

inPath = os.path.normpath('/home/ubuntu/wikiart/images')
outPath = os.path.normpath('/home/ubuntu/wikiart64x64/')

for root, dirs, files in os.walk(inPath):
    p, style = os.path.split(root)
    newPath = os.path.join(outPath, style)
    os.makedirs(newPath, exist_ok=True)
    i = 0
    print("Opening folder: ", root)
    for f in files:
        source = os.path.join(root, f)
        if f == '.DS_Store':
            continue
        if os.path.isfile(source):
            source = os.path.join(root, f)
            newName = str(i) + '.png'
            try:
                im = Image.open(source)
                inputSize = im.size
                ratio = float(SIZE) / max(inputSize)
                new_image_size = tuple([int(x*ratio) for x in inputSize])
                im = im.resize(new_image_size, Image.ANTIALIAS)
                new_im = Image.new("RGB", (SIZE, SIZE))
                new_im.paste(im, ((SIZE-new_image_size[0])//2, (SIZE-new_image_size[1])//2))
                new_im.save(os.path.join(newPath, newName), 'PNG', quality=70)
                i += 1
            except:
                print("Skipping file: ", source)
        print("Resized ", i, " Images in folder: ", root)
