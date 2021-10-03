import csv
#from cryptography.fernet import Fernet
import numpy as np
from compression import uncompress

uncompress('fourieroutputsencrypted.csv.gz')

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

        with open('fourieroutputsdecrypted.csv') as file:
            content = file.readlines()
        header = content[:1]
        rows = content[1:]
        i = 0
        timeArr = []
        magX = []
        magY = []
        magZ = []
        accX = []
        accY = []
        accZ = []
        gyroX = []
        gyroY = []
        gyroZ = []
        Temp = []
        Pres = []
        Yaw = []
        Pitch = []
        Roll = []
        DCM1 = []
        DCM2 = []
        DCM3 = []
        DCM4 = []
        DCM5 = []
        DCM6 = []
        DCM7 = []
        DCM8 = []
        DCM9 = []
        MagNED1 = []
        MagNED2 = []
        MagNED3 = []
        AccNED1 = []
        AccNED2 = []
        ACCNED3 = []
        record = rows[1]
        arr = record.split()
        startTime = datetime.datetime.strptime(arr[0], '%Y-%m-%d-%H:%M:%S.%f')
    
        for record in rows[1:len(rows)-1]:
            arr = record.split()
            timeNow = datetime.datetime.strptime(arr[0], '%Y-%m-%d-%H:%M:%S.%f')
            timeint = (timeNow-startTime).total_seconds()
            timeArr.append(timeint)
            magX.append(float(arr[1]))
            magY.append(float(arr[2]))
            magZ.append(float(arr[3]))
            accX.append(float(arr[4]))
            # print(accX[i])
            accY.append(float(arr[5]))
            accZ.append(float(arr[6]))
            gyroX.append(float(arr[7]))
            gyroY.append(float(arr[8]))
            gyroZ.append(float(arr[9]))
            Temp.append(float(arr[10]))
            Pres.append(float(arr[11]))
            Yaw.append(float(arr[12]))
            Pitch.append(float(arr[13]))
            Roll.append(float(arr[14]))
            DCM1.append(float(arr[15]))
            DCM2.append(float(arr[16]))
            DCM3.append(float(arr[17]))
            DCM4.append(float(arr[18]))
            DCM5.append(float(arr[19]))
            DCM6.append(float(arr[20]))
            DCM7.append(float(arr[21]))
            DCM8.append(float(arr[22]))
            DCM9.append(float(arr[23]))
            MagNED1.append(float(arr[24]))
            MagNED2.append(float(arr[25]))
            MagNED3.append(float(arr[26]))
            AccNED1.append(float(arr[27]))
            AccNED2.append(float(arr[28]))
            ACCNED3.append(float(arr[29]))

if __name__ == '__main__':
    pass