from PIL import Image
from PIL import ImageDraw
import piexif
from PIL import ImageFont

im = Image.open(input("Enter absolute photo path: "))
timestamp = piexif.load(im.info["exif"])["Exif"][36867].decode("ascii")
myFont = ImageFont.truetype("ArialHB.ttc", 60)
I1 = ImageDraw.Draw(im)
I1.text((20, 20), timestamp, font=myFont, fill=(0, 0, 0))
im.save(input("Enter absolute path for a new photo: "))
