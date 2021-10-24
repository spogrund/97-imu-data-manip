import csv
import numpy as np
import datetime
import encrypt
import os
import sys
from fourierclass import invfourier, fourier
from compression import  compressgz , uncompress
import os
def mainfunction():
    with open('IMUOutputs.csv') as file:
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
    Roll = []
    Pitch = []
#    Temp = []
#    Pres = []
    Yaw = []
    Temp = []
    Hum = []
#    Pitch = []
 #   Roll = []
#    DCM1 = []
#    DCM2 = []
#    DCM3 = []
#    DCM4 = []
#    DCM5 = []
#    DCM6 = []
#    DCM7 = []
#    DCM8 = []
#    DCM9 = []
#    MagNED1 = []
#    MagNED2 = []
#    MagNED3 = []
#    AccNED1 = []
#    AccNED2 = []
#    ACCNED3 = []
    record = rows[1]

    arr = record.split(',')
    
    startTime = datetime.datetime.strptime(arr[0], '%Y-%m-%d-%H:%M:%S.%f')

    for record in rows[1:len(rows)-1]:
        arr = record.split(',')
 
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
#        Temp.append(float(arr[10]))
#        Pres.append(float(arr[11]))
        Roll.append(float(arr[10]))
        Pitch.append(float(arr[11]))
        Yaw.append(float(arr[12]))
        Temp.append(float(arr[13]))
        Hum.append(float(arr[14]))
#        Pitch.append(float(arr[13]))
#        Roll.append(float(arr[14]))
#        DCM1.append(float(arr[15]))
#        DCM2.append(float(arr[16]))
#        DCM3.append(float(arr[17]))
#        DCM4.append(float(arr[18]))
#        DCM5.append(float(arr[19]))
#        DCM6.append(float(arr[20]))
#        DCM7.append(float(arr[21]))
#        DCM8.append(float(arr[22]))
#        DCM9.append(float(arr[23]))
#        MagNED1.append(float(arr[24]))
#        MagNED2.append(float(arr[25]))
#        MagNED3.append(float(arr[26]))
#        AccNED1.append(float(arr[27]))
#        AccNED2.append(float(arr[28]))
#        ACCNED3.append(float(arr[29]))
    dataTime = datetime.datetime.now()
#    print("data collected and it took: " + str((dataTime-runtimeStart).total_seconds()) + "s")
    

    timeArr = fourier(timeArr)
    magX = fourier(magX)
    magY = fourier(magY)
    magZ = fourier(magZ)
    accX = fourier(accX)
    accY = fourier(accY)
    accZ = fourier(accZ)
    gyroX = fourier(gyroX)
    gyroY = fourier(gyroY)
    gyroZ = fourier(gyroZ)

#    Temp = fourier(Temp)
#    Pres = fourier(Pres)
    Yaw = fourier(Yaw)
    Pitch = fourier(Pitch)
    Roll = fourier(Roll)
    Temp = fourier(Temp)
    Hum = fourier(Hum)
#    DCM1 = fourier(DCM1)
#    DCM2 = fourier(DCM2)
#    DCM3 = fourier(DCM3)
#    DCM4 = fourier(DCM4)
#    DCM5 = fourier(DCM5)
#    DCM6 = fourier(DCM6)
#    DCM7 = fourier(DCM7)
#    DCM8 = fourier(DCM8)
#    DCM9 = fourier(DCM9)
#    MagNED1 = fourier(MagNED1)
#    MagNED2 = fourier(MagNED2)
#    MagNED3 = fourier(MagNED3)
#    AccNED1 = fourier(AccNED1)
#    AccNED2 = fourier(AccNED2)
#    ACCNED3 = fourier(ACCNED3)
    fourierTime = datetime.datetime.now()
#    print("fourier done and it took: "  + str((fourierTime-dataTime).total_seconds()) + "s") 
   
    with open(os.path.join(os.path.dirname(__file__), 'fourieroutputs.csv'), mode= 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(0,len(rows)-2):
            writer.writerow([timeArr[i],(magX[i]),(magY[i]),(magZ[i]),(accX[i]),(accY[i]),(accZ[i]),(gyroX[i]),(gyroY[i]),(gyroZ[i]),(Roll[i]),(Pitch[i]),(Yaw[i]),(Temp[i]),(Hum[i])]) #,(Pitch[i]), (Roll[i]), (DCM1[i]),  (DCM2[i]), (DCM3[i]),(DCM4[i]),(DCM5[i]),(DCM6[i]),(DCM7[i]),(DCM8[i]), (DCM9[i]), MagNED1[i], MagNED2[i],MagNED3[i],AccNED1[i],AccNED2[i],ACCNED3[i]])

    encrypt.encryptfile()
    encryptTime = datetime.datetime.now()
#    infofile= open("infoFile.txt","a+")
#    infofile.write("encrypted and it took: " + str((encryptTime-fourierTime).total_seconds()) + "s")
    #print("encrypted and it took: " + str((encryptTime-fourierTime).total_seconds()) + "s")
#    file2 = round(os.path.getsize("fourieroutputsencrypted.csv") / (1024 * 1000), 2)
    compressgz('fourieroutputsencrypted.csv')
#    compressTime = datetime.datetime.now()
#    infofile.write("compressed and it took: " + str((compressTime-encryptTime).total_seconds()) + "s")
     #print("compressed and it took: " + str((compressTime-encryptTime).total_seconds()) + "s")
#    runtimeEnd = datetime.datetime.now()
#    file1 = round(os.path.getsize("fourieroutputsencrypted.csv.gz") / (1024 * 1000), 2)
    
   # print(str(round((runtimeEnd-runtimeStart).total_seconds(), 2) )+"\n")
    #print("original file size:  " + str(file2)+ " MB\n")
    #print("compressed file size:  " + str(file1) + " MB\n")
    #print(str(round((file1/file2)*100,2)) + "%")
#    infofile.write(str(round((runtimeEnd-runtimeStart).total_seconds(), 2) )+"\n")
#    infofile.write("original file size:  " + str(file2)+ " MB\n")
#    infofile.write("compressed file size:  " + str(file1) + " MB\n")
#    infofile.write(str(round((file1/file2)*100,2)) + "%")
