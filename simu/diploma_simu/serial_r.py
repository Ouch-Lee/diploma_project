import time
import serial
import re
# import chardet


def ser_get():
    '''串口连接'''

    portx = 'COM6'  # 端口号

    bps = 9600  # 波特率

    timeout = None  # 超时时间设置，None代表永远等待操作

    ser = serial.Serial(portx, bps, timeout=1)  # 打开串口，并得到串口对象
    # print('串口详情参数：',ser)

    return ser


def ser_read():
    '''串口读取'''
    print('正在读取串口内容!')
    data = ''
    while True:
        data = ser_get().readline()  # 获取串口内容
        print('***********')
        time1 = time.time()
        t = time.ctime()
        print(t, ':')
        data_st = str(data)  # 列表转换字符串
        sst = re.findall(r'\b\d+\b', data_st)  # 字符串提取数字
        print(sst)
        # with open('D:/test.txt', 'a') as f:
        #     f.writelines(t)
        #     f.writelines(':\n')
        #     try:
        #         f.writelines(data.decode(encofing='utf-8'))
        #     except Exception as e:
        #         print(e)

if __name__ == '__main__':
    ser_read()