import serial
import re
import time


ser = serial.Serial('COM6', 9600, timeout=1)
aa = open('D:\桌面\datas_serial.txt', 'w', encoding='utf-8')
ser.write("testing".encode())
try:
    for i in range(10000):
        wind = ser.readline()   # 读取
        print(wind)
        st = str(wind)  # 列表转换字符串
        sst = re.findall(r'\-?\d+\.?\d+', st)   # 字符串提取数字

        if sst == []:
            sst = 0
        else:
            a = sst[3]
            print(float(a))
            # print(str(sst[0]), str(sst[1]),str(sst[2]),str(sst[3]),str(sst[4]) )

            aa.write(str(sst[0])+ " " +sst[1] +'\n')


except KeyboardInterrupt:
    ser.close()
    aa.close()
