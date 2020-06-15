import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
from PIL import ImageOps
from PIL import ImageFont
images = []

image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')
width, height = image.size

for k in (0.1, 0.5, 0.9):
    image=Image.open("readonly/msi_recruitment.gif")
    image=image.convert('RGB')
    for i in range(width):
        for j in range(height):
            pix = image.load()
            R, G, B = pix[i, j]
            image.putpixel( (i, j) , (R, int(G*k), B))
            
    img_with_border = ImageOps.expand(image,border=(0,0,0,50),fill='black')
    font = ImageFont.truetype("readonly/fanwood-webfont.ttf",40)
    draw = ImageDraw.Draw(img_with_border)
    draw.text((0, height+10),"channel 0 intensity {}".format(k),(255,int(255*k),255),font=font)
    images.append(img_with_border)
    
for k in (0.1, 0.5, 0.9):
    image=Image.open("readonly/msi_recruitment.gif")
    image=image.convert('RGB')
    for i in range(width):
        for j in range(height):
            pix = image.load()
            R, G, B = pix[i, j]
            image.putpixel( (i, j) , (int(R*k), G, B))

    img_with_border = ImageOps.expand(image,border=(0,0,0,50),fill='black')
    font = ImageFont.truetype("readonly/fanwood-webfont.ttf",40)
    draw = ImageDraw.Draw(img_with_border)
    draw.text((0, height+10),"channel 0 intensity {}".format(k),(int(255*k),255,255),font=font)
    images.append(img_with_border)
    
for k in (0.1, 0.5, 0.9):
    image=Image.open("readonly/msi_recruitment.gif")
    image=image.convert('RGB')
    for i in range(width):
        for j in range(height):
            pix = image.load()
            R, G, B = pix[i, j]
            image.putpixel( (i, j) , (R, G, int(B*k)))
 
    img_with_border = ImageOps.expand(image,border=(0,0,0,50),fill='black')
    font = ImageFont.truetype("readonly/fanwood-webfont.ttf",40)
    draw = ImageDraw.Draw(img_with_border)
    draw.text((0, height+10),"channel 0 intensity {}".format(k),(255,255,int(255*k)),font=font)
    images.append(img_with_border)
    
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    contact_sheet.paste(img, (x, y) )
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
 
