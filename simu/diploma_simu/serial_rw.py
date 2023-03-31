import serial
import re
import time


ser = serial.Serial('COM6', 115200, timeout=1)
aa = open('D:\桌面\datas_serial.txt', 'w', encoding='utf-8')
ser.write("testing".encode())
try:
    while 1:

        wind = ser.readline()   # 读取
        print(wind)
        st = str(wind)  # 列表转换字符串

        sst = re.findall(r'\d+\.?\d+', st)   # 字符串提取数字

        if sst == []:
            sst = 0
        else:
            print(str(sst[0]), str(sst[1]) )

            aa.write(str(sst[0])+ " " +sst[1] +'\n')


except KeyboardInterrupt:
    ser.close()
    aa.close()
