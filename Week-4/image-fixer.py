#!/usr/bin/env python3
from PIL import Image
import os

path =  os.path.join(os.path.expanduser('~'),'supplier-data','images')
def img_fix(imglist):
    for img in imglist:
        savepath = os.path.join(os.path.expanduser('~'),'supplier-data','images')
        fullpath = os.path.join(path, img)
        open_image = Image.open(fullpath)
        new_name = img.split(".")[0] + ".jpeg"
        print(new_name)
        new_path = os.path.join(savepath,new_name)
        open_image.resize((600,400)).convert("RGB").save(new_path)
        print(open_image.size)


def main():
    print(path)
    imgfiles = [x for x in os.listdir(path) if x.endswith(r".tiff")]
    print(imgfiles)
    img_fix(imgfiles)

if __name__ == "__main__":
    main()