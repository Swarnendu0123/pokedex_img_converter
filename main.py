import sys
import os
from PIL import Image

# grab the first and second arguments
if len(sys.argv) == 3:
    first, second = sys.argv[1], sys.argv[2]
else:
    first, second = sys.argv[1], ""

# opening the folder
if (os.path.exists(first)):
    files = os.listdir(first)
    print(files)
else:
    print("No folder found")

# check if the /new exist or not if not then create it
if not os.path.exists(second):
    os.mkdir("converted_images")
    second = "./converted_images"

# loop througn poke_dex
for file in files:
    img = Image.open(first+"/"+file)
    # convert images to png 
    file = file.split(".")[0]
    path = file + ".png"
    #save the image
    img.save(os.path.join("./"+second, path))
