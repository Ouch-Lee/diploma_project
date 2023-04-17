# this file is to build the kinetics model for master robot
import numpy as np
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
from spatialmath import SE3
from spatialmath import base

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
            name= "master robot",
            manufacturer= "Unimation",
            keywords= ("dynamics", "symbolic", "mesh"),
            symbolic=symbolic
        )
        self.num_all_joints = len(L)
        self.qinit = np.array([0, 0, 0, 0, 0, pi/2, d3, -pi/2, 0, 0])
        self.qr = np.array([0, 0.15, pi/4, 0, 0, pi/4+pi/2, d3, -pi/2+pi/4, 0, 0])

        self.addconfiguration("qz", self.qinit)
        self.addconfiguration("qr", self.qr)

if __name__ == "__main__":
    mR = masterRobot(symbolic= False)
    print(mR)
    # mR.plot(mR.qr,backend='pyplot', block= True, jointaxes=False)
    # mR.plot(mR.qr,backend='pyplot', block= True)
    # T = mR.fkine(mR.qr)
    # print(T)
    qt = rtb.jtraj(mR.qinit, mR.qr, 50)
    mR.plot(qt.q, backend='pyplot', block= True)