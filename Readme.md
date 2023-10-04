## HACTOBERFEST 2023

# PokeDex Image Converter

PokeDex Image Converter is a Python script that converts images of Pokémon from the `poke_dex` folder to PNG, JPEG, GIF, or BMP format. The script takes images with names `['bulbasaur.jpg', 'charmander.jpg', 'pikachu.jpg', 'squirtle.jpg']` and converts them to PNG files.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
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

## Example

### Source Images (poke_dex folder):

1. Bulbasaur:
![Bulbasaur](poke_dex/bulbasaur.jpg)
2. Charmander:
![Charmander](poke_dex/charmander.jpg)
3. Pikachu:
![Pikachu](poke_dex/pikachu.jpg)
4. Squirtle:
![Squirtle](poke_dex/squirtle.jpg)

### Converted Images (converted_images folder):

1. Bulbasaur:
![Bulbasaur Converted](converted_images/bulbasaur.png)
2. Charmander:
![Charmander Converted](converted_images/charmander.png)
3. Pikachu:
![Pikachu Converted](converted_images/pikachu.png)
4. Squirtle:
![Squirtle Converted](converted_images/squirtle.png)

## Contributing

If you want to contribute to this project and make it better, your help is very welcome. Open an issue or submit a pull request to propose changes or additions.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.

---

In this example, I've added placeholders for the source and converted images. You can replace them with actual links to your images hosted online or update them with the appropriate relative paths if you are hosting the images within your project repository.
