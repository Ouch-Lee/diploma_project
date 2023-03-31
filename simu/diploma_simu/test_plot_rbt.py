import roboticstoolbox as rtb
robot = rtb.models.Panda()
from spatialmath import SE3

Tep = SE3.Trans(0.6, -0.3, 0.1) * SE3.OA([0, 1, 0], [0, 0, -1])
sol = robot.ik_lm_chan(Tep)
print(sol)
q_pickup = sol[0]
print(robot.fkine(q_pickup))
qt = rtb.jtraj(robot.qr, q_pickup, 50)

robot.plot(qt.q, backend='pyplot', block= True)