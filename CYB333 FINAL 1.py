# pip install Pillow
from PIL import Image  # Python Image Library - Image Processing

import glob

print(glob.glob("*.jpg"))
#prints list of JPEG files in folder

for file in glob.glob("*.jpg"):
    im = Image.open(file)
    rgb_im = im.convert('RGB')
    rgb_im.save(file.replace("jpg", "png"), quality=95)
#convert all
