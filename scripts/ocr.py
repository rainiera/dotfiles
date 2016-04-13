"""
Story:
    I am the social chair of a student org. I was tasked with constructing
    a survey for our formal's meal options, and was given two menus as
    PNGs with a lot of text I didn't want to have to type out.

Setup:
    Get tesseract through one of the installation methods described here:
        https://github.com/tesseract-ocr/tesseract/wiki
    Download the Pytesser raw script from here:
        https://github.com/RobinDavid/Pytesser/blob/master/pytesser.py
    Make sure the Pytesser deps (OpenCV, etc.) are installed (you will
    probably get ImportErrors if you don't) and make sure the Tesseract
    binary is in your PATH.

Usage:
    `python ocr.py entree_dessert.png soup_salad.png`
"""

import pytesser
import sys

for arg in sys.argv[1:]:
    txt = pytesser.image_to_string(arg)
    with open("{}.txt".format(arg.split('.')[0]), 'w') as f:
        f.write(txt)

