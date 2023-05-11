from PIL import Image
import os
source_folder = "/media/wiktor/Nowy/FOTO/OSKAR 10X15/"
output_folder = "/media/wiktor/Nowy/FOTO/OSKAR 10X15/scaled/"
props = 10/15

folder_path = source_folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".JPG") or file_name.endswith(".jpeg"):
        file_path = os.path.join(folder_path, file_name)
        with Image.open(file_path) as image:
            w = image.width
            h = image.height
            if w > h:
                print("vertical")
                print(w/h)
                img = image
                w = image.width
                h = image.height
                new_h = int(w * props)
                area = (0, (h - new_h) / 2, w, (h + new_h) / 2)
                img = img.crop(area)
                img.save(output_folder + file_name)

            if h > w:
                print("horizontal")
                print(w/h)
                img = image.rotate(90, resample=0, expand=1, center=None, translate=None, fillcolor=None)
                w = img.width
                h = img.height
                new_h = int(w * props)
                area = (0, (h - new_h) / 2, w, (h + new_h) / 2)
                img = img.crop(area)
                img = img.rotate(270, resample=0, expand=1, center=None, translate=None, fillcolor=None)
                img.save(output_folder+ file_name)
