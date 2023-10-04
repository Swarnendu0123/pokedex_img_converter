## HACTOBERFEST 2023

# PokeDex Image Converter

PokeDex Image Converter is a versatile Python script designed to simplify the process of converting Pokémon images. Whether you have existing Pokémon images or you want to download new ones, this script provides a user-friendly solution. It allows you to perform various operations, including background removal, format conversion, and image compression.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Installation

Make sure you have Python installed. Clone the repository and install the required packages using `pip`.

```bash
git clone https://github.com/Swarnendu0123/pokedex_img_converter.git
cd pokedex_img_converter
python3 -m pip install -r requirements.txt
```

## Usage

Run the script from the command line, providing the source folder and an optional destination folder.

```bash
python main.py poke_dex converted_images
```

- `poke_dex`: Source folder containing Pokémon images.
- `converted_images`: Destination folder where converted PNG images will be saved.

## Features

### 1. **Command Line Interface:**
The script accepts command line arguments for specifying the source folder (containing Pokémon images) and an optional output folder. If no output folder is provided, it defaults to "converted_images".

```bash
python main.py poke_dex
```

### 2. **Pokémon Image Fetching:**
 Users can choose to download images of new Pokémon. The script fetches the images of the specified Pokémon from an online source (pokebase API) and saves them in the source folder.

```bash
Do you want to download a new pokemon(y/n): y
Enter the name of the pokemon : meowth
Fetching meowth
```

`poke_dex/meowth.png`
![Meowth](poke_dex/meowth.png)
    
The script asks the user if they want to download a new Pokémon image. If the user chooses to download a new Pokémon and enters the name (for example, meowth), the fetch_pokemon function is called.

### 3. **Background Removal:**
 Users have the flexibility to remove the background from the Pokémon images. The script utilizes the `rembg` library to achieve this functionality.

 `poke_dex/pikachu.jpg`
![poke_dex/pikachu.jpg](poke_dex/pikachu.jpg)

`converted_images/pikachu_bgremoved.png`
![poke_dex/pikachu.jpg](converted_images/pikachu_bgremoved.png)

### 4. **Image Format Conversion:**
 Users can select the desired output image format from options such as PNG, JPEG, GIF, or BMP. The script converts the images accordingly.

### 5. **Image Compression (Optional):**
 Users can opt to compress the images by specifying the desired width and height in pixels. The images are resized before saving, allowing for efficient storage.

### 6. **Error Handling:**
 The script includes robust error handling to catch exceptions during the conversion process. Informative error messages are provided to guide users in case of issues.

### 7. **File Management:**
  The script checks if the specified source folder exists. If not, it prints an error message. It also verifies the existence of the output folder; if absent, the script creates it.


#### Source Images (poke_dex folder):

`poke_dex/bulbasaur.jpg`
![Bulbasaur](poke_dex/bulbasaur.jpg)

`poke_dex/charmander.jpg`
![Charmander](poke_dex/charmander.jpg)

`poke_dex/pikachu.jpg`
![Pikachu](poke_dex/pikachu.jpg)

`poke_dex/squirtle.jpg`
![Squirtle](poke_dex/squirtle.jpg)

#### Converted Images (converted_images folder):

`converted_images/bulbasaur_bgremoved.png`
![Bulbasaur Converted](converted_images/bulbasaur_bgremoved.png)

`converted_images/charmander_bgremoved.png`
![Charmander Converted](converted_images/charmander_bgremoved.png)

`converted_images/pikachu_bgremoved.png`
![Pikachu Converted](converted_images/pikachu_bgremoved.png)

`converted_images/squirtle_bgremoved.png`
![Squirtle Converted](converted_images/squirtle_bgremoved.png)

### 8. **External Libraries:**
 The script utilizes external libraries, including `PIL` (Pillow) for image processing, `rembg` for background removal, `pokebase` for fetching Pokémon images, and `requests` for making HTTP requests.

## Contributing

If you want to contribute to this project and make it better, your help is very welcome. Open an issue or submit a pull request to propose changes or additions.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.

---

In this example, I've added placeholders for the source and converted images. You can replace them with actual links to your images hosted online or update them with the appropriate relative paths if you are hosting the images within your project repository.
