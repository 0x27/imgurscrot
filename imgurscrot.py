#!/usr/bin/python2
# coding: utf-8
# takes a screenshot and uploads
# to imgur using the imgur API
# assuming you have an account
# Version: 20150328.1
# Author: Darren Martyn
# Licence: WTFPL
import pyscreenshot as pyscrot
import requests
import json
import random
import sys
import string
import base64
import time
import os

# globals. alter these
client_id = GET_YOUR_OWN

def upload_image(tempfile):
    f = open(tempfile, 'rb')
    b64image = base64.b64encode(f.read())
    headers = {'Authorization': 'Client-ID '+client_id}
    data = {'image': b64image, 'title': 'Screenshot-%s' %(time.strftime("%H:%M:%S-%d/%m/%Y"))}
    try:
        r = requests.post(url="https://api.imgur.com/3/upload.json", data=data, headers=headers)
    except Exception, e:
        print "[-] Image Upload Failed. Printing stack trace and exiting..."
        sys.exit(str(e))
    lol = json.loads(r.text)
    print lol['data']['link'] #['id']['link']

def main():
    try:
        image = pyscrot.grab()
    except Exception, e:
        print "[-] Error in screencapture. Printing stack trace and exiting..."
        sys.exit(str(e))
    try:
        randomfilename = ''.join(random.SystemRandom().choice(string.uppercase + string.digits) for _ in xrange(6))
        tempfile = "/tmp/%s.png" %(randomfilename)
        image.save(tempfile)
    except Exception, e:
        print "[-] Problem saving tempfile... Printing stack trace and exiting..."
        sys.exit(str(e)) 
    try:
        upload_image(tempfile)
    except Exception, e:
        print "[-] Problem uploading screenshot... Printing stack trace and exiting..."
        sys.exit(str(e))
    try:
        os.unlink(tempfile)
    except Exception, e:
        print "[-] Problem deleting our tempfile... Printing stack trace and exiting..."
        sys.exit(str(e))


if __name__ == "__main__":
    main()
