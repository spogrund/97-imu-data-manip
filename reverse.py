import csv
from cryptography.fernet import Fernet
import numpy as np


def decrypt():
    fernet = Fernet(key)

    # opening the encrypted file
    with open('fourieroutputsencrypted.csv', 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open('fourieroutputsdecrypted.csv', 'wb') as dec_file:
        dec_file.write(decrypted)


if __name__ == '__main__':
    pass
