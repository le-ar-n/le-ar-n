from PIL import Image, ImageDraw, ImageFont

import string

def uppercase_image_char(char, font_size):

    position = (5, -15)
    width, height = 270, 300
    font_path = r"C:\Windows\Fonts\Roboto\Roboto-Medium.ttf"
    img = Image.new("RGB", (width, height), (255,255,255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, char.upper(), (0,0,0), font=font)
    #img.show()
    img.save('uppercase\\%s.jpg' % char)
 
def lowercase_image_char(char, font_size):

    position = (5, -90)
    width, height = 170, 200
    font_path = r"C:\Windows\Fonts\Roboto\Roboto-Medium.ttf"

    if char in ['b', 'd', 'f', 'h', 'k', 'l', 't']:
    	height = 250
    	position = (5, -40)
    elif char in ['g', 'p', 'q', 'y']:
    	height = 250
    	position = (5, -100)
    elif char in ['i']:
    	height = 230
    	position = (5, -55)
    elif char in ['j']:
    	height = 300
    	position = (5, -60)
    elif char in ['m', 'w']:
    	width = 250
    img = Image.new("RGB", (width, height), (255,255,255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, char, (0,0,0), font=font)
    #img.show()
    img.save('lowercase\\%s.jpg' % char)

for char in list(string.ascii_lowercase):

	lowercase_image_char(char, 300)
	#uppercase_image_char(char, 300)

"""
img = Image.new('RGB', (160, 300), color = (255, 255, 255))
 
draw = ImageDraw.Draw(img)
fnt = ImageFont.truetype("Roboto-Black.ttf", 105)

draw.text((10, 290), "a", fill=(0,0,0), font=fnt)
"""
 
#img.save('pil_text.png')