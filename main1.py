from PIL import Image
import os
source_folder = "/media/wiktor/Nowy/FOTO/OSKAR 21x30/"
output_folder = "/media/wiktor/Nowy/FOTO/OSKAR 21x30/scaled/"
props = 21/30

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

# with Image.open("/home/wiktor/Pictures/Screenshots/a.jpg") as image:
#     w = image.width
#     h = image.height
#     if w > h:
#         print("vertical")
#         print(w / h)
#         area = ((w - h) / 2, 0, (w + h) / 2, h)
#         img = image.crop(area)
#     if h > w:
#         print("horizontal")
#         print(w / h)
#         area = (0, (h - w) / 2, w, (h + w) / 2)
#         img = image.crop(area)
#
#     # Crop to 16:9 aspect ratio
#     w = img.width
#     h = img.height
#     if w / h > 16 / 9:
#         new_w = int(h * 16 / 9)
#         area = ((w - new_w) / 2, 0, (w + new_w) / 2, h)
#         img = img.crop(area)
#     else:
#         new_w = int(h * 16 / 9)
#         area = ((w - new_w) / 2, 0, (w + new_w) / 2, h)
#         img = img.crop(area)
#
#     # Saved in the same relative location
#     img.save("/home/wiktor/cropped_picture.png")
