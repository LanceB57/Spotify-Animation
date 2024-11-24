from PIL import Image
from typing import Tuple

def generate_colored_logo(color: Tuple[int, int, int]) -> None:
    # Load the image
    image_path = "img/spotify.png"
    image = Image.open(image_path).convert("RGBA")

    # Get pixel data
    pixels = image.load()

    # Define the replacement color (R, G, B, A)
    replacement_color = color + (255,)
    s = set()
    # Loop through each pixel
    width, height = image.size
    for x in range(width):
        for y in range(height):
            if pixels[x, y] == (29, 185, 84, 255):
                pixels[x, y] = replacement_color

    # Save the modified image
    image.save("tmp/logo.png")