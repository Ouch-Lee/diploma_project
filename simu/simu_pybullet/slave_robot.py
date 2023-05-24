import pybullet as p
import time
import pybullet_data
import numpy as np

class SlaveRobot(object):
    def __init__(self,set_sliders=False, set_cameras=True):
        self.physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
        p.resetDebugVisualizerCamera(cameraDistance=1, cameraYaw=0,
                                     cameraPitch=220, cameraTargetPosition=[0, 0, 0.2])
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
        self.ground = p.loadURDF("plane.urdf")
        urdfFlags = p.URDF_USE_SELF_COLLISION
        # self.cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
        self.cubeStartOrientation_platform = p.getQuaternionFromEuler([1.57, 0, 0])
        self.robot = p.loadURDF("actuator2/actuator2.urdf", [2, -0.2, 0.05], [0,0.5,0.5,0],
                                flags=urdfFlags,
                                useFixedBase=True)
        # self.platform = p.loadURDF("grip_platform/grip_platform.urdf", [-0.08, 0.6, 0],
        #                            self.cubeStartOrientation_platform,
        #                            flags=urdfFlags,
        #                            useFixedBase=True)
        self.grip_goal = p.loadURDF("circle_platform/circle_platform.urdf", [-0.13, 0.6, 0.06],
                                    self.cubeStartOrientation_platform,
                                    flags=urdfFlags,
                                    useFixedBase=True)
        self.joints = self.get_joints()
        self.num_joints = len(self.joints)
        self.sr_arm_id = [1, 2, 3, 4, 5,6]
        self.sr_yaw_id = [7, 9, 11, 13, 15, 17, 19, 21]
        self.sr_pitch_id = [8, 10, 12, 14, 16, 18, 20] #
        self.sr_roll_shear = [22, 23, 24]

        self.simu_f = 100
        self.motion_f = 2

        if set_sliders: self.add_custom_sliders()
        self.camera_sliders = []
        if set_cameras: self.add_camera_sliders()  # adjust [pitch, yaw] for now

    def run(self):
        taregt_p =np.zeros(self.num_joints)
        p.stepSimulation()
        for i in range(int(5e3)):
            t = i / self.simu_f
            self.update_camera_vision()
            one_position = 0.8/6  * np.sin(t ) #* np.pi / 5)
            print(one_position)
            for j in self.sr_arm_id:
                # taregt_p[0] = one_position
                taregt_p[j] = one_position
                taregt_p[-3] = one_position
            # print(taregt_p)
            taregt_p[-1] = 0.5
            taregt_p[-2] = -0.5
            t = i / self.simu_f
            # self.step(taregt_p)
            time.sleep(1 / self.simu_f)
        p.disconnect()

    def step(self, control_array):
        if control_array is None:
            control_array = np.zeros(self.num_joints)
        for j in range(self.num_joints):
            p.setJointMotorControl2(self.robot, self.joints[j], p.POSITION_CONTROL, control_array[j])
        p.stepSimulation()

    def get_joints(self):
        all_joints = []
        for j in range(p.getNumJoints(self.robot)):
            # Disable motor in order to use direct torque control.
            info = p.getJointInfo(self.robot, j)
            joint_type = info[2]
            if (joint_type == p.JOINT_PRISMATIC or joint_type == p.JOINT_REVOLUTE):
                all_joints.append(j)
                p.setJointMotorControl2(self.robot, j,
                                        controlMode=p.VELOCITY_CONTROL, force=0)
        joints = all_joints[0:]
        return joints

    def add_camera_sliders(self):
        self.camera_sliders.append(p.addUserDebugParameter('pitch', 180, 360, 230))
        self.camera_sliders.append(p.addUserDebugParameter('yaw', 180, 360, 130))
        self.camera_sliders.append(p.addUserDebugParameter('distance', 0, 1, 0.3))

    def update_camera_vision(self):
        p.resetDebugVisualizerCamera(cameraDistance=p.readUserDebugParameter(self.camera_sliders[2]),
                                     cameraYaw=p.readUserDebugParameter(self.camera_sliders[1]),
                                     cameraPitch=p.readUserDebugParameter(self.camera_sliders[0]),
                                     cameraTargetPosition=[0, 0, 0.2])

if __name__ == '__main__':
    sr = SlaveRobot()
    sr.run()

