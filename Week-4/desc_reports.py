#!/usr/bin/env python3
import os
import reports
import emails
from datetime import date

path =  os.path.join(os.path.expanduser('~'),'supplier-data','descriptions')
desc = []
def txt_desc(txtlist):
    for txt in txtlist:
        fullpath = os.path.join(path, txt)
        with open(fullpath,"r") as text:
            textlist = text.readlines()
            desc.append("name: {}<br/>weight: {}\n".format(textlist[0],textlist[1]))
    return desc 


def main():
    print(path)
    txtfiles = [x for x in os.listdir(path) if x.endswith(r".txt")]
    print(txtfiles)
    summary = txt_desc(txtfiles)

    filename = "/tmp/processed.pdf"
    title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
    additional_info = "<br/><br/>".join(summary)
    reports.generate(filename,title,additional_info)

    subject = "Upload Completed - Online Fruit Store"
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate(sender, receiver, subject, body, filename)
    emails.send(message)

if __name__ == "__main__":
    main()