import csv
from cryptography.fernet import Fernet
import numpy as np
import datetime
import encrypt
import time
import cmath
from fourierclass import invfourier, fourier
from compression import uncompress
import os

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
header = ""

def decomp():
    uncompress('fourieroutputsencrypted.csv.gz')


def decrypt():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

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


def writefour():
    global header, rows
    with open('fourieroutputsdecrypted.csv') as file:
        content = file.readlines()

        header = content[:1]
        rows = content[1:]
        i = 0

        record = rows[2]
        arr = record.split()
        # startTime = datetime.datetime.strptime(arr[0], '%Y-%m-%d-%H:%M:%S.%f')

        for record in rows[1:len(rows) - 1]:

                #print(type(record))
                #print(record.find(","))
                arr = record.split(",")
                #timeNow = datetime.datetime.strptime(arr[0], '%Y-%m-%d-%H:%M:%S.%f')
                # timeint = (timeNow - startTime).total_seconds()
                # timeArr.append(timeint)
                #print(arr)
                #print(len(arr))

                if (len(arr) > 1):
                    magX.append((arr[1]))
                    #print(magX)
                    timeArr.append(arr[0])
                    magY.append((arr[2]))
                    magZ.append((arr[3]))
                    accX.append((arr[4]))
                    # print(accX[i])
                    accY.append((arr[5]))
                    accZ.append((arr[6]))
                    gyroX.append((arr[7]))
                    gyroY.append((arr[8]))
                    gyroZ.append((arr[9]))
                    Temp.append((arr[10]))
                    Pres.append((arr[11]))
                    Yaw.append((arr[12]))
                    Pitch.append((arr[13]))
                    Roll.append((arr[14]))
                    DCM1.append((arr[15]))
                    DCM2.append((arr[16]))
                    DCM3.append((arr[17]))
                    DCM4.append((arr[18]))
                    DCM5.append((arr[19]))
                    DCM6.append((arr[20]))
                    DCM7.append((arr[21]))
                    DCM8.append((arr[22]))
                    DCM9.append((arr[23]))
                    MagNED1.append((arr[24]))
                    MagNED2.append((arr[25]))
                    MagNED3.append((arr[26]))
                    AccNED1.append((arr[27]))
                    AccNED2.append((arr[28]))
                    ACCNED3.append((arr[29]))
        #print(magX)

def reversefourier():
    global magX, magY, magZ, accX, accY, accZ, gyroX, gyroY, gyroZ, Temp, Pres, Yaw, Pitch, Roll, DCM1, DCM2, DCM3, DCM4, DCM5, DCM6, DCM7, DCM8, DCM9, MagNED1, MagNED2, MagNED3, AccNED1, AccNED2, ACCNED3
    #print(magX)
    #timeArr = invfourier(timeArr)
    magX = invfourier(magX)
    magY = invfourier(magY)
    magZ = invfourier(magZ)
    accX = invfourier(accX)
    accY = invfourier(accY)
    accZ = invfourier(accZ)
    gyroX = invfourier(gyroX)
    gyroY = invfourier(gyroY)
    gyroZ = invfourier(gyroZ)
    Temp = invfourier(Temp)
    Pres = invfourier(Pres)
    Yaw = invfourier(Yaw)
    Pitch = invfourier(Pitch)
    Roll = invfourier(Roll)
    DCM1 = invfourier(DCM1)
    DCM2 = invfourier(DCM2)
    DCM3 = invfourier(DCM3)
    DCM4 = invfourier(DCM4)
    DCM5 = invfourier(DCM5)
    DCM6 = invfourier(DCM6)
    DCM7 = invfourier(DCM7)
    DCM8 = invfourier(DCM8)
    DCM9 = invfourier(DCM9)
    MagNED1 = invfourier(MagNED1)
    MagNED2 = invfourier(MagNED2)
    MagNED3 = invfourier(MagNED3)
    AccNED1 = invfourier(AccNED1)
    AccNED2 = invfourier(AccNED2)
    ACCNED3 = invfourier(ACCNED3)



def writeout():
    global header,rows
    with open(os.path.join(os.path.dirname(__file__), 'unfourieredoutputs.csv'), mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        print(magX)
        for i in range(0, len(magX) - 1):
            #print(magX[i])
            writer.writerow(
                [timeArr[i], (magX[i]), (magY[i]), (magZ[i]), (accX[i]), (accY[i]), (accZ[i]), (gyroX[i]), (gyroY[i]),
                 (gyroZ[i]), (Temp[i]), (Pres[i]), (Yaw[i]), (Pitch[i]), (Roll[i]), (DCM1[i]), (DCM2[i]), (DCM3[i]),
                 (DCM4[i]), (DCM5[i]), (DCM6[i]), (DCM7[i]), (DCM8[i]), (DCM9[i]), MagNED1[i], MagNED2[i], MagNED3[i],
                 AccNED1[i], AccNED2[i], ACCNED3[i]])


if __name__ == '__main__':
    decomp()
    decrypt()
    writefour()
    reversefourier()
    writeout()
