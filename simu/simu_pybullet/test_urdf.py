import pybullet as p
import time
import pybullet_data
import numpy as np

class TestUrdf(object):
    def __init__(self,set_sliders=False, set_cameras=True):
        self.physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
        p.resetDebugVisualizerCamera(cameraDistance=1, cameraYaw=0,
                                     cameraPitch=220, cameraTargetPosition=[0, 0, 0.2])
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
        self.ground = p.loadURDF("plane.urdf")
        urdfFlags = p.URDF_USE_SELF_COLLISION
        self.cubeStartOrientation = p.getQuaternionFromEuler([1.57,0,1.57])
        self.robot = p.loadURDF("actuator2/actuator2.urdf",[0, 0, 0.024], self.cubeStartOrientation,
                       flags=urdfFlags,
                       useFixedBase=True)

        self.simu_f = 50
        self.motion_f = 2  # Controlled motion frequency, Hz



if __name__ == '__main__':
    test_urdf = TestUrdf()
    for i in range(int(5e3)):
        t = i / test_urdf.simu_f
        p_target = 0.1 * np.sin(t) + 0.3
        p.setJointMotorControl2(test_urdf.robot, 0, p.POSITION_CONTROL, p_target)
        p.stepSimulation()
        time.sleep(1 / test_urdf.simu_f)
    p.disconnect()

