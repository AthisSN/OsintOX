import PIL
from PIL import Image
from PIL.ExifTags import TAGS

def metadata():
	path = input("Enter the Image path to extract the metadata: ")
	image = Image.open(path)
	data = image.getexif()
	for tagid in data:
		tagname = TAGS.get(tagid,tagid)
		value = data.get(tagid)
		print(f"{tagname:25} : {value}")


