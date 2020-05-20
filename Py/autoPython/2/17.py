import PIL

PIL.ImageColor.getcolor('red', 'RGBA')

from PIL import ImageColor
ImageColor.getcolor('red', 'RGBA')
from PIL import Image
catIm = Image.open('zophie.png')
catIm.size
width, height = catIm.size
catIm.format
catIm.save('zophie.jpg')