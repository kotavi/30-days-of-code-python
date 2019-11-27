from PIL import Image
import inspect
from urllib.request import urlopen

file = "Kaptain.jpg"

image = Image.open(file, 'r')
print(image) # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=604x625 at 0x10B48D350>

print("The type of the image is " + str(type(image)))
print(inspect.getmro(type(image))) # Return tuple of base classes (including cls) in method resolution order.

# image.show()


img = Image.open(urlopen("https://i.stack.imgur.com/9Jg2f.jpg?s=328&g=1"))
# img.show()

help(img.copy)
help(img.save)

img.save('fly.gif', 'gif')
print(inspect.getmro(type(img)))