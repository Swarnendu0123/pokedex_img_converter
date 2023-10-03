import sys
import os
from PIL import Image
from rembg.bg import remove
from tqdm import tqdm


def export(array, bool=False):
    for i in array:
        img = Image.open(source_folder + "/" + i)
        if bool == True:
            print(f"Removing background from {i}")
            img = remove(img)
        i = i.split(".")[0]
        path = i + ".png"
        img.save(os.path.join("./" + output_folder, path))


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
    input = input("Do you want to remove background from all images? (y/n): ")
    if input == "y":
        export(files, True)
    else:
        export(files, False)
else:
    print("No files found")
