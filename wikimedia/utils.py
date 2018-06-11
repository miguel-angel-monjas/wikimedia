#!/usr/bin/python
# -*- coding: latin-1 -*-

import pywikibot as pb
from hashlib import sha1
from io import BytesIO

def is_commons_file (sha):
    """Determine whether the image is already in Commons"""
    commons_site = pb.Site("commons", "commons")
    result = False
    for page in pb.site.APISite.allimages(commons_site, sha1=sha) :
        print (page)
        result = True
        break
    return result
    
def get_hash (file_path):
    """Get the SHA-1 hash of an image"""
    image_file = open(file_path, "rb")
    byte_stream = BytesIO(image_file.read()).getvalue()
    image_file.close()
    
    hashObject = sha1()
    hashObject.update(byte_stream)
    return hashObject.hexdigest()

def remove_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)