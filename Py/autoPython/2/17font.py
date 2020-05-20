from PIL import ImageFont
from PIL import Image, ImageDraw, ImageFont
import os
im = Image.new('RGBA', (200, 200), 'white')

draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'C:\\Windows\\Fonts' # e.g. ‘/Library/Fonts’
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('text.png')