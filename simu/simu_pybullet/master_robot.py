import pybullet as p
import time
import pybullet_data
import numpy as np
import matplotlib.pyplot as plt

class MasterRobot(object):
    def __init__(self,set_sliders=False, set_cameras=True):
        self.physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
        p.resetDebugVisualizerCamera(cameraDistance=1, cameraYaw=0,
                                     cameraPitch=220, cameraTargetPosition=[0, 0, 0.2])
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
        self.ground = p.loadURDF("plane.urdf")
        urdfFlags = p.URDF_USE_SELF_COLLISION
        self.robot = p.loadURDF("master_robot_2/master_robot_2.urdf",[0, 0, 0], [0, 0.5, 0.5, 0],
                       flags=urdfFlags,
                       useFixedBase=True)
        self.joints = self.get_joints()
        self.num_joints = len(self.joints)
        self.simu_f = 50
        self.motion_f = 2  # Controlled motion frequency, Hz

        if set_sliders: self.add_custom_sliders()
        self.camera_sliders = []
        if set_cameras: self.add_camera_sliders()  # adjust [pitch, yaw] for now
        # self.q_vec = np.zeros(self.n_j)
        # self.dq_vec = np.zeros(self.n_j)
        # self.q_mat = np.zeros((self.simu_f * 3, self.n_j))
        # self.q_d_mat = np.zeros((self.simu_f * 3, self.n_j))
        # self.init_plot()

    def run(self):
        angles_data = self.openreadtxt("circling-2.txt")
        angles_data_exchange = self.re_arrange(angles_data)
        p.stepSimulation()
        # time.sleep(5)
        for i in range(int(5e3)):
            t = i / self.simu_f
            self.update_camera_vision()
            p_joints =self.get_target_P(angles_data_exchange[i,:])
            self.step(p_joints)
            time.sleep(1/self.simu_f)
        p.disconnect()

    def test_joint(self, joint_id):
        for i in range(10000):
            self.update_camera_vision()
            # if i % 20 == 0:
            #     target_p = np.sin(i) * np.pi / 2
            target_p = np.pi / 4
            p_joints = np.zeros((self.num_joints))
            p_joints[joint_id] = target_p
            self.step(p_joints)
            p.stepSimulation()
            time.sleep(1/self.simu_f)
        p.disconnect()



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

    def step(self, control_array):
        if control_array is None:
            control_array = np.zeros(self.num_joints)
        for j in range(self.num_joints):
            p.setJointMotorControl2(self.robot, self.joints[j], p.POSITION_CONTROL, control_array[j])
        p.stepSimulation()

    def get_target_P(self, encoder_angles):
        """

        :param encoder_angles: it is a list/array that store the angles received from Arduino/Stm32
        :return: the target Position to robot
        """
        encoder_angles = self.list_deg2rad(encoder_angles)
        encoder_angles[0] = self.rad2distance(0.03, encoder_angles[0])
        return encoder_angles

    ### this part is about visual and camera
    # def add_custom_sliders(self):
    #     for _i in range(4):
    #         p.addUserDebugParameter(self.abad_joint_Names[_i], -3.14, 3.14, 0)
    #         p.addUserDebugParameter(self.thigh_joint_Names[_i], -3.14, 3.14, 0)
    #         p.addUserDebugParameter(self.shank_joint_Names[_i], -3.14, 3.14, 0)

    def add_camera_sliders(self):
        self.camera_sliders.append(p.addUserDebugParameter('pitch', 180, 360, 220))
        self.camera_sliders.append(p.addUserDebugParameter('yaw', 0, 360, 180))
        self.camera_sliders.append(p.addUserDebugParameter('distance', 0, 2, 0.5))

    def update_camera_vision(self):
        p.resetDebugVisualizerCamera(cameraDistance=p.readUserDebugParameter(self.camera_sliders[2]),
                                     cameraYaw=p.readUserDebugParameter(self.camera_sliders[1]),
                                     cameraPitch=p.readUserDebugParameter(self.camera_sliders[0]),
                                     cameraTargetPosition=[0, 0, 0.2])

    def list_deg2rad(self, angles):
        len1 = len(angles)
        for i in range(len1):
            angles[i] = angles[i] * np.pi / 180
        return angles

    def rad2distance(self, D, rad_joint0):
        """
        beacuse the joint0 is a prismatic joint, so we have to transform the angle of encoder0 to the prismatic distance
        :param D: the diameter of synchronizing wheel
        :param rad_joint0:
        :return:
        """
        S = np.pi * D
        circles = rad_joint0 / (2 * np.pi)
        distance = S * circles
        return distance

    def openreadtxt(self, file_name):
        data = np.genfromtxt(file_name)
        return data

    def re_arrange(self, datas):
        rows, cols = datas.shape
        tmp_datas = np.zeros([rows, cols])
        tmp_datas[:,0:cols-1] = datas[:, 1:cols]
        tmp_datas[:,cols-1] = datas[:,0]
        return tmp_datas




if __name__ == '__main__':
    mr = MasterRobot()
    mr.run()
    # mr.test_joint(2)