#!/usr/bin/env python3
import os
import shutil
import psutil
import socket
import emails

def check_cpu():
    cpu = psutil.cpu_percent(1)
    return cpu < 80
def check_disk(disk):
    usage = shutil.disk_usage(disk)
    free = usage.free / usage.total * 100
    return free > 20
def check_memory():
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500
def check_host():
    host = socket.gethostbyname('localhost')
    return host == '127.0.0.1'

def main():
    error_dict = {check_cpu():"CPU usage is over 80%", check_disk("/"): "Available disk space is less than 20%",
    check_memory(): "Available memory is less than 500MB", check_host():"localhost cannot be resolved to 127.0.0.1"}

    error = False
    for err, errmessage in error_dict.items():
        if not err: 
            error_message = errmessage
            error = True
    if error:
        try:
            sender = "automation@example.com"
            receiver = "{}@example.com".format(os.environ.get('USER'))
            subject = "Error - {}".format(error_message)
            body = "Please check your system and resolve the issue as soon as possible"
            message = emails.generate_error(sender, receiver, subject, body)
            emails.send(message)
        except NameError:
            pass

if __name__ == "__main__":
    main()
