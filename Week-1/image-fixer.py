from PIL import Image
import re
import os

path = r"C:\Users\Raj\Documents\Bangkit 2022\Program & Shit\Final Course\Week-1\img"
def img_fix(imglist):
    for img in imglist:
        savepath = r"C:\Users\Raj\Documents\Bangkit 2022\Program & Shit\Final Course\Week-1\img-fixed"
        fullpath = os.path.join(path, img)
        open_image = Image.open(fullpath)
        new_name = re.sub('\.[a-z]*$', '.jpeg', img)
        print(new_name)
        open_image.rotate(-90).resize((128,128)).convert("RGB").save(savepath+"\\"+new_name)
        print(open_image.size)


def main():
    print(path)
    imgfiles = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    print(imgfiles)
    img_fix(imgfiles)

if __name__ == "__main__":
    main()