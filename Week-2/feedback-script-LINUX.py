#! /usr/bin/env python3
import os
import requests

path = "/data/feedback"
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
            response = requests.post("http://35.184.32.200/feedback/", json=dirf)
            print(response.status_code)
            response.raise_for_status()
def main():
    filelist = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    print(filelist)
    text_to_json(filelist)

if __name__ == "__main__":
    main()