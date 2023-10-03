import sys
import os
from PIL import Image
from rembg import remove

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

filetype = ".png"

print("Select the desired output format. Available Options: ")
print("     1. PNG")
print("     2. JPEG")
print("     3. GIF")
print("     4. BMP")
user_choice = input("Enter the number of your choice: ")

#Makes sure user put in a valid option, otherwise converts to PNG
if (user_choice.isnumeric()):
    if (user_choice == '1'):
        # If user select PNG Check if user want bg remover or not
        print("Select Option. Available Options:")
        print("     1. Remove Background")
        print("     2. Not Remove Background")
        background_color = input("Enter the number of your choice: ")
    if (user_choice == "2"):
        filetype = ".jpeg"
    elif (user_choice == "3"):
        filetype = ".gif"
    elif (user_choice == "4"):
        filetype = ".bmp"
    

# loop througn poke_dex
try:
    for file in files:
        img = Image.open(source_folder+"/"+file)
        file = file.split(".")[0]
        
        if background_color == '1':
            img = remove(img)
            file = file + "_bgremoved"

        # else :
        #     img = Image.open(source_folder+"/"+file)
        
        # convert images to png 
        path = file + filetype
        #save the image
        img.save(os.path.join("./"+output_folder, path))
except Exception as e:
    print(f"There is an error in conversion: {e}")
