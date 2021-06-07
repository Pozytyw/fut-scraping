import os
from PIL import Image

# path to folder
path = "C:\\Users\\Pilot\\Downloads\\players"

for filename in os.listdir(path):
    with Image.open(os.path.join(path, filename)) as f:
        img = f.convert("RGBA")
        img_data = img.getdata()

        newData = []
        for item in img_data:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(os.path.join(path, filename), "PNG")
