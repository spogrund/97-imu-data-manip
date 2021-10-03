import csv
import numpy as np

if __name__ == '__main__':
    with open('2018-09-19-03_57_11_VN100.csv') as file:
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

    print(len(rows))
    for record in rows[1:len(rows)-1]:
        arr = record.split()

        timeArr.append(arr[0])

        magX.append(arr[1])
        magY.append(arr[2])
        magZ.append(arr[3])
        accX.append(arr[4])
        # print(accX[i])
        accY.append(arr[5])
        accZ.append(arr[6])
        gyroX.append(arr[7])
        gyroY.append(arr[8])
        gyroZ.append(arr[9])
        Temp.append(arr[10])
        Pres.append(arr[11])
        Yaw.append(arr[12])
        Pitch.append(arr[13])
        Roll.append(arr[14])
        DCM1.append(arr[15])
        DCM2.append(arr[16])
        DCM3.append(arr[17])
        DCM4.append(arr[18])
        DCM5.append(arr[19])
        DCM6.append(arr[20])
        DCM7.append(arr[21])
        DCM8.append(arr[22])
        DCM9.append(arr[23])
        MagNED1.append(arr[24])
        MagNED2.append(arr[25])
        MagNED3.append(arr[26])
        AccNED1.append(arr[27])
        AccNED2.append(arr[28])
        ACCNED3.append(arr[29])



