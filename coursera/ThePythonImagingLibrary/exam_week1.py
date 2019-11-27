import PIL
from PIL import Image
from PIL import ImageEnhance

# read image and convert to RGB
image=Image.open("Kaptain.jpg")
image=image.convert('RGB')
# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)
r,g,b = image.split()
r.show()
g.show()
b.show()


irr= image.getchannel('R')
irr.show()
# enhancer=ImageEnhance.Color(image)

from PIL import ImageFilter

images=[]
for i in range(1, 10):
    print(i/10)
    # image.paste((200, 200, 200), [0, 0, image.size[0], image.size[1]])
    # image.convert('P', palette=Image.ADAPTIVE, colors=256)
    images.append(enhancer.enhance(i/10))

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.show()