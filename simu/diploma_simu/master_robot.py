# this file is to build the kinetics model for master robot
import numpy as np
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
from spatialmath import SE3
from spatialmath import base
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk #NavigationToolbar2TkAgg
import imageio
from roboticstoolbox.backends.swift import Swift

from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  #中文显示
mpl.rcParams['axes.unicode_minus']=False      #负号显示

class masterRobot(DHRobot):
    def __init__(self, symbolic=False):
        if symbolic:
            import spatialmath.base.symbolic as sym

            zero = sym.zero()
            pi = sym.pi()
        else:
            from math import  pi
            zero = 0.0

        deg = pi / 180
        inch = 0.0254

        d3 = 0.09
        a_4 = d3
        a_t3 = 0.155


        L = [
            # base link
            RevoluteDH(
                a=0,
                alpha=-pi/2,
                d=0,
                qlim=[-180*deg,180*deg]
            ),

            # the first joint: 1
            PrismaticDH(
                theta=zero,
                a =0,
                alpha=pi/2,
                qlim= [0,0.3]
            ),
            # link e0 1
            RevoluteDH(
                d = 0.06,
                a = 0,
                alpha= -pi/2,
                qlim=[-60 * deg, 60*deg]
            ),
            # link e1, for the fix joint, set a small range 1
            RevoluteDH(
                a= 0,
                alpha= zero,
                d= 0.21855,
                qlim= [0,0.01]
            ),
            # # link2 1
            PrismaticDH(
                a= 0,
                alpha= pi/2,
                theta= zero,
                qlim= [0,0.01]
            ),
            # # link t2 1
            RevoluteDH(
                a= 0,
                alpha= pi/2,
                d= 0.165,
                qlim= [-180 * deg , 180*deg ]
            ),
            # # link 3 1
            PrismaticDH(
                a=0,
                alpha=zero,
                theta= pi/2,
                qlim=[0 + d3, 0.01 + d3]
            ),
            # # link t3 1
            RevoluteDH(
                a= a_t3,
                alpha= -pi/2,
                d= 0,
                qlim= [-180 * deg , 180*deg]
            ),
            # # link 4  1
            PrismaticDH(
                a= -a_4,
                alpha= -pi/2,
                theta= -pi/2,
                qlim=[0,0.01]
            ),
            # # final link
            RevoluteDH(
                a= 0,
                alpha= 0,
                d= -0.015,
                qlim= [-180 * deg , 180*deg]
            )



        ]

        super().__init__(
            L,
            name= " ",
            manufacturer= "Unimation",
            keywords= ("dynamics", "symbolic", "mesh"),
            symbolic=symbolic
        )
        self.num_all_joints = len(L)
        self.qinit = np.array([0, 0, 0, 0, 0, pi/2, d3, -pi/2, 0, 0])
        self.qr = np.array([0, 0.15, pi/4, 0, 0, pi/4+pi/2, d3, -pi/2+pi/4, 0, 0])

        self.addconfiguration("qz", self.qinit)
        self.addconfiguration("qr", self.qr)


class From:
    def __init__(self):
        self.root = tk.Tk()  # 创建主窗体
        self.canvas = tk.Canvas()  # 创建一块显示图形的画布
        self.figure = self.create_matplotlib()  # 返回matplotlib所画图形的figure对象
        self.create_form(self.figure)  # 将figure显示在tkinter窗体上面
        self.root.mainloop()

    def openreadtxt(self, file_name):
        data = np.genfromtxt(file_name)
        return data


    def create_matplotlib(self):
        # 创建绘图对象f
        data = self.openreadtxt('d:\\桌面\\毕业设计\\diploma_project\\EE_control\\angle_data\\R=16\\datas_serial_Q=0.03.txt')

        the_len, the_num = data.shape
        t = range(the_len)
        f = plt.figure(dpi=100, figsize=(12,8),facecolor="gray",edgecolor='green',frameon=True)
        # fig1 = plt.subplot(1, 1, 1)
        for angle_id in range(the_num):
            id_string = "encoder_" + str(angle_id)
            plt.plot(t, data[:, angle_id], linewidth=1, label=id_string)
        plt.legend(fontsize=20)
        plt.title("plot in tkinter", fontsize=30)
        # fig1.set_title("tkinter + matplot", loc='center', pad=20, fontsize='xx-large', color='red')
        return f



    def create_form(self, figure):
        # 把绘制的图形显示到tkinter窗口上
        self.canvas = FigureCanvasTkAgg(figure, self.root)
        self.canvas.draw()  # 以前的版本使用show()方法，matplotlib 2.2之后不再推荐show（）用draw代替，但是用show不会报错，会显示警告
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # 把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
        toolbar = NavigationToolbar2Tk(self.canvas,
                                       self.root)  # matplotlib 2.2版本之后推荐使用NavigationToolbar2Tk，若使用NavigationToolbar2TkAgg会警告
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == "__main__":
    # form = From()
    mR = masterRobot(symbolic= False)
    env = Swift()
    #
    # mR.plot(mR.qinit,backend='pyplot', block= True, jointaxes=False)
    # mR.plot(mR.qr,backend='pyplot', block= True)
    # T = mR.fkine(mR.qr)
    # print(T)

    qt = rtb.jtraj(mR.qinit, mR.qr, 50)
    mR.plot(qt.q, backend='pyplot', movie='panda1.gif',jointaxes=False)

