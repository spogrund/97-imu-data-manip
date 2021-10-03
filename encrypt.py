import csv
from cryptography.fernet import Fernet
import numpy as np
import datetime


def encryptfile():
    key = Fernet.generate_key()

            # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

        # using the generated key
    fernet = Fernet(key)

        # opening the original file to encrypt
    with open('fourieroutputs.csv', 'rb') as file:
        original = file.read()

        # encrypting the file
    encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
    with open('fourieroutputsencrypted.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)