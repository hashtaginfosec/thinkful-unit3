from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import sys
import os
import struct
import random


#password to secret.py is given through sys arguments
key = sys.argv[1].encode()

#hash the password with SHA256 so it can be used with AES
h = SHA256.new()
h.update(key)
password = (h.hexdigest())


def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    #We encrypt this file using AES CBC
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES)
