import sys
import os
from PIL import Image
from rembg import remove
from pokebase import pokemon
from requests import get
from io import BytesIO

# grab the source_folder and output_folder arguments
if len(sys.argv) == 3:
    source_folder, output_folder = sys.argv[1], sys.argv[2]
else:
    source_folder, output_folder = sys.argv[1], "converted_images"

# opening the folder
if (os.path.exists(source_folder)):
    files = os.listdir(source_folder)
else:
    print("No folder found")

# check if the /new exist or not if not then create it
if not os.path.exists(output_folder):
    os.mkdir("converted_images")
    output_folder = "./converted_images"
    output_files = os.listdir(source_folder)


# function to fetch pokemon
def fetch_pokemon(name):
    print("Fetching " + name)
    name = name.lower()
    try:
        poke = pokemon(name)
        pic = get(poke.sprites.front_default).content
        image = Image.open(BytesIO(pic))
        filetype = ".png"
        path = name + filetype
        new_size = (3000, 3000)
        image = image.resize(new_size)
        image.save(os.path.join("./"+source_folder, path))
    except Exception as e:
        print(f"Error : {e}")


new_pokemon_choice = input("Do you want to download a new pokemon(y/n): ")

if new_pokemon_choice == "y":
    new_pokemon = input("Enter the name of the pokemon : ")
    fetch_pokemon(new_pokemon)

# If user select PNG Check if user want bg remover or not
remove_background = input("Do you want to remove the background(y/n): ")

print("Select the desired output format. Available Options: ")
print("     1. PNG")
print("     2. JPEG")
print("     3. GIF")
print("     4. BMP")
img_format = input("Enter the number of your choice: ")


compress_choice = input("Do you want to Compress Images?(y/n): ")
if compress_choice == 'y':
    print("What is size you want to compress?")
    width, height = int(input("Enter the width (in pixel): ")), int(
        input("Enter the height (in pixel): "))

# Makes sure user put in a valid option, otherwise converts to PNG
match img_format:
    case "2":
        filetype = ".jpeg"
    case "3":
        filetype = ".gif"
    case "4":
        filetype = ".bmp"
    case _:
        filetype = ".png"

# loop through poke_dex
try:
    for file in files:
        if remove_background == 'y':
            img = Image.open(source_folder+"/"+file)
            img = remove(img)
            img = img.convert('RGB') if img_format == "2" else img
            file = file.split(".")[0]
            file = file + "_bgremoved"
        else:
            img = Image.open(source_folder+"/"+file)
            file = file.split(".")[0]
        # convert images to png

        path = file + filetype
        # save the image
        if compress_choice == "1":
            new_size = (width, height)
            img = img.resize(new_size)
            img.save(os.path.join("./"+output_folder, path), optimize=True)
        else:
            img.save(os.path.join("./"+output_folder, path))
except Exception as e:
    print(f"There is an error in conversion: {e}")
