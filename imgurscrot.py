#!/usr/bin/python2
# coding: utf-8
# takes a screenshot and uploads
# to imgur using the imgur API
# assuming you have an account
# Version: 20150329.1
# Author: Darren Martyn
import pyscreenshot as pyscrot
import requests
import json
import sys
import base64
import time
import os
from StringIO import *

def upload_image(pil_img, client_id):
    imgstr = StringIO()
    pil_img.save(imgstr, 'png')
    b64image = base64.standard_b64encode(imgstr.getvalue())
    headers = {'Authorization': 'Client-ID '+client_id}
    data = {'image': b64image, 'title': 'Screenshot-%s' %(time.strftime("%H:%M:%S-%d/%m/%Y"))}
    try:
        r = requests.post(url="https://api.imgur.com/3/upload.json", data=data, headers=headers)
    except Exception, e:
        print "[-] Image Upload Failed. Printing stack trace and exiting..."
        sys.exit(str(e))
    lol = json.loads(r.text)
    print lol['data']['link']

def main():
    client_id_env_var = 'IMGUR_CLIENT_ID'
    if client_id_env_var in os.environ.keys():
        client_id = os.environ[client_id_env_var]
    else:
        sys.exit("[-] Set environmental variable IMGUR_CLIENT_ID to your client_id :)")
    try:
        image = pyscrot.grab()
    except Exception, e:
        print "[-] Error in screencapture. Printing stack trace and exiting..."
        sys.exit(str(e))
    try:
        upload_image(pil_img=image, client_id=client_id)
    except Exception, e:
        print "[-] Problem uploading screenshot... Printing stack trace and exiting..."
        sys.exit(str(e))


if __name__ == "__main__":
    main()
