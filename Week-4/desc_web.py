#!/usr/bin/env python3
import os
import requests

path =  os.path.join(os.path.expanduser('~'),'supplier-data','descriptions')
def txt_upload(txtlist):
    for txt in txtlist:
        dirf = {}
        fullpath = os.path.join(path, txt)
        with open(fullpath,"r") as text:
            textlist = text.readlines()
            weight = textlist[1].replace("lbs"," ")
            print(weight)
            dirf["name"] = textlist[0].strip()
            dirf["weight"] = int(weight)
            dirf["description"] = textlist[2].strip()
            dirf["image_name"] = txt.split(".")[0] + ".jpeg"
            response = requests.post("http://35.188.86.145/fruits/", json=dirf)
            print(response.status_code)
            response.raise_for_status()


def main():
    print(path)
    txtfiles = [x for x in os.listdir(path) if x.endswith(r".txt")]
    print(txtfiles)
    txt_upload(txtfiles)

if __name__ == "__main__":
    main()