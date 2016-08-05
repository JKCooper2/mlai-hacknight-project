# Requires Pillow
# pip install Pillow
#
# 1. Put images to be resized into images/srouce
# 2. Run


import os
import PIL.Image


def save_image(img, save_type, name):
    if not os.path.exists('images/' + save_type):
        os.makedirs('images/' + save_type)

    img.save('images/' + save_type + '/' + save_type + '-' + name)


def convert_image(image_file):
    img = PIL.Image.open("images/source/"+image_file)

    img64 = img.resize((64, 64), PIL.Image.ANTIALIAS)
    save_image(img64, 'rgb64', image_file)

    img64bw = img64.convert('L')
    save_image(img64bw, 'bw64', image_file)

    img32 = img.resize((32, 32), PIL.Image.ANTIALIAS)
    save_image(img32, 'rgb32', image_file)

    img32bw = img32.convert('L')
    save_image(img32bw, 'bw32', image_file)


def main():
    image_files = [img for img in os.listdir("images/source")]

    for image_file in image_files:
        convert_image(image_file)


if __name__ == "__main__":
    main()
