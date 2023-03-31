import roboticstoolbox as rtb
import matplotlib.pyplot as plt
# take the puma robot as the example the learn the process

# first get/build the DH table for the robot
puma = rtb.models.DH.Puma560()
# print(puma)
q = [0.1   ,0.2   ,  0.3, - 2.7416, - 0.5, - 2.5416]
# plt.figure()
puma.plot(q,backend='pyplot', block= True)
# plt.show()


