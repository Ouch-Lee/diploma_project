# import xlrd
# import openpyxl
from tkinter import filedialog #路径选择
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import matplotlib.animation as animation


root = Tk()  # 创建tkinter的主窗口
root.title("练习窗口")
root.geometry('320x240+10+10')
#标签
label1=Label(root,text='测试窗口')
label1.place(x=0,y=0)
#文本框
Text = Text(root,width = 50,height=10)#测试文本框
Text.place(x=0,y=30)

#图像及画布
fig = plt.figure(figsize=(6,4),dpi=100)#图像比例
f_plot =fig.add_subplot(111)#划分区域
canvas_spice = FigureCanvasTkAgg(fig,root)
canvas_spice.get_tk_widget().place(x=0,y=200)#放置位置

x = []
y = []

# 创建绘制实时损失的动态窗口
plt.ion()

# 创建循环
# for i in range(100):
# 	x.append(i)	# 添加i到x轴的数据中
# 	y.append(i**2)	# 添加i的平方到y轴的数据中
# 	plt.clf()  # 清除之前画的图
# 	plt.plot(x, y * np.array([-1]))  # 画出当前x列表和y列表中的值的图形
# 	plt.pause(0.001)  # 暂停一段时间，不然画的太快会卡住显示不出来
# 	plt.ioff()  # 关闭画图窗口

# button = Button(root,text='选择文件',bg='lightblue',width=10,command=get_xl)
# button.place(x=400,y=1)
root.mainloop()

# 主循环
