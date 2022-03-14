#!/usr/bin/env python3
from PIL import Image
import os
import requests

url = "http://localhost/upload/"
path =  os.path.join(os.path.expanduser('~'),'supplier-data','images')
def img_fix(imglist):
    for img in imglist:
        fullpath = os.path.join(path, img)
        with open(fullpath,"rb") as opened:
          r = requests.post(url, files={'file':opened})


def main():
    print(path)
    imgfiles = [x for x in os.listdir(path) if x.endswith(r".jpeg")]
    print(imgfiles)
    img_fix(imgfiles)

if __name__ == "__main__":
    main()