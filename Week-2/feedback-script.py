import os
import requests

path = r"C:\Users\Raj\Documents\Bangkit 2022\Program & Shit\Final Course\Week-2\txt"
def text_to_json(filelist):
    for file in filelist:
        dirf = {}
        fullpath = os.path.join(path, file)
        with open(fullpath,"r") as text:
            textlist = text.readlines()
            dirf["title"] = textlist[0].strip()
            dirf["name"] = textlist[1].strip()
            dirf["date"] = textlist[2].strip()
            dirf["feedback"] = textlist[3].strip()
            print(dirf)

def main():
    filelist = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    print(filelist)
    text_to_json(filelist)

if __name__ == "__main__":
    main()