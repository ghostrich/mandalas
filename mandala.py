from PIL import Image, ImageDraw, ImageOps 

haeckse = Image.open("haeckse2.png")
im = Image.open("background2.png")
im.paste(haeckse,(200,200), haeckse)

feuer = Image.open("feuer8.png")
im2 = Image.open("background2.png")
im2.paste(feuer,(300,300),feuer)
#im2.save("feuertest.png")

background = Image.new('RGB', (1500, 1500), color = (255,255,255))
draw = ImageDraw.Draw(background)
draw.ellipse((300, 300, 1200, 1200), fill=None, outline=(0, 0, 0), width=22)
draw.ellipse((450, 450, 1050, 1050), fill=None, outline=(0, 0, 0), width=22)
draw.ellipse((50, 50, 1450, 1450), fill=None, outline=(0, 0, 0), width=50)
draw.ellipse((-200, -200, 1700, 1700), fill=None, outline=(0, 0, 0), width=270)


number_of_images = 5
angle = int(360/number_of_images)
for x in range(number_of_images):
   im1 = im.rotate(angle*x, expand=False, center=(750,750))
   background.paste(im1, (0,0), im1)


number_of_images = 5
angle = int(360/number_of_images)
for x in range(number_of_images):
   im3 = im2.rotate(angle*x, expand=False, center=(406,308))
   background.paste(im3, (343,441), im3)

background_inv = ImageOps.invert(background)
background_inv.show()
background_inv.save("mandala.png")
