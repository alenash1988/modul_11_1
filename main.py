from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter

class Photo:
    def __init__(self, name):
        self.name = name
        self.front = 'snrif.ttf'
        self.size = 50
    def correct_photo(self):
        image = Image.open(self.name)
        print(image.format, image.size, image.mode)
        x, y = image.size
        image_2 = image.resize(x//2, y//2)
        blur_img = image_2.filter(ImageFilter.BLUR)
        draw = ImageDraw.Draw(blur_img)
        front = ImageFont.truetype(self.front, self.size)
        draw.text((200, 250), 'Hello, sea...', fill="red", front=front)
        blur_img.show()


sea = Photo('sea.jpg')
print(sea)



