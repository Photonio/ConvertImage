# Convert:
# https://search.brave.com/search?q=convert+webp+to+png+python&original=web
# https://www.pycodemates.com/2023/10/webp-to-png-conversion-using-python.html

# Scale:
# https://cloudinary.com/guides/bulk-image-resize/python-image-resize-with-pillow-and-opencv

# AI
# https://chat.openai.com/share/7d24c939-08d3-4446-968e-61b397fc1dcd
# https://chat.openai.com/c/fc923815-b652-48e9-b166-c318ea348d58

from pathlib import Path
from PIL import Image # Open a WebP image


original = "1_rAO0XWvBPdETsDNbqvi_dA.webp"
name = original.split('.')[0]


def convertToPng():
    webp_image = Image.open(original)

    png_image = webp_image.convert("RGBA")

    try:
        png_image = webp_image.convert("RGBA")
        png_image.save(f"{name}.png")
    except Exception as e:
        print(f"An error occurred: {e}")

def scale_image(input_path, output_path, scale_percent):
    # Open the image file
    original_image = Image.open(input_path)

    # Calculate the new dimensions
    width, height = original_image.size
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)

    # Resize the image
    resized_image = original_image.resize((new_width, new_height))

    # Save the resized image
    resized_image.save(output_path)

# Example usage:
output_image_path = f"scaled_{name}.png"
scale_percent = 50  # Change this to the desired percentage

scale_image(original, output_image_path, scale_percent)
convertToPng()
