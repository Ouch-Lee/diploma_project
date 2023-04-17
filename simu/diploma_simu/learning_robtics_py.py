import roboticstoolbox as rtb
import matplotlib.pyplot as plt
import master_robot as mr
import numpy as np
import time
# take the puma robot as the example the learn the process

d3 = 0.09

def list_deg2rad(angles):
    len1 = len(angles)
    for i in range(len1):
        angles[i] = angles[i] * np.pi / 180

    return angles

def encoder_angles2simu_angles(angles_rad):
    indexes = [0, 3, 4, 6, 8]
    insert_values = [0, 0, 0, d3, 0]
    for i in range(len(indexes)):
        angles_rad.insert(indexes[i], insert_values[i])
    rads = angles_rad[1]
    rev = rads
    angles_rad[1] = rev *  0.01
    return angles_rad

# first get/build the DH table for the robot
MR = mr.masterRobot(symbolic= False)
print(MR)

encoder_angles_1 = [540, -45, 20, 45, 0]
encoder_angles_2 = [600, -30, 30, 30, 0]
angles_rad_1 = list_deg2rad(encoder_angles_1)
angles_rad_2 = list_deg2rad(encoder_angles_2)
simu_angles_1 = encoder_angles2simu_angles(angles_rad_1)
simu_angles_2 = encoder_angles2simu_angles(angles_rad_2)
# print(simu_angles)
simu_angles = [MR.qinit, simu_angles_1, simu_angles_2]
cnt = 0
for i in range(100):
    # print(simu_angles[i%3])
    # plt.clf()
    MR.plot(simu_angles[i%3],dt=0.05, backend='pyplot', clf = True)


# #
# qt = rtb.jtraj(MR.qinit, simu_angles, 50)
# MR.plot(qt.q, backend='pyplot', block= True)






# plt.figure()
# puma.plot(q,backend='pyplot', block= True)
# plt.show()


