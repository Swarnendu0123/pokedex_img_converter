import sys
import os
from PIL import Image
from rembg.bg import remove
from tqdm import tqdm

# grab the source_folder and output_folder arguments
if len(sys.argv) == 3:
    source_folder, output_folder = sys.argv[1], sys.argv[2]
else:
    source_folder, output_folder = sys.argv[1], ""

# opening the folder
if os.path.exists(source_folder):
    files = os.listdir(source_folder)
else:
    print("No folder found")

# check if the /new exist or not if not then create it
if not os.path.exists(output_folder):
    os.mkdir("converted_images")
    output_folder = "./converted_images"

# loop througn poke_dex
if files != 0:
    print(f"Beginning to remove background from {len(files)} images")
    for file in files:
        img = Image.open(source_folder + "/" + file)
        img = remove(img)
        print(f"Removing background from {file}")
        # convert images to png
        file = file.split(".")[0]
        path = file + ".png"
        # save the image
        img.save(os.path.join("./" + output_folder, path))
else:
    print("No files found")
