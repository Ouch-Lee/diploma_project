import pybullet as p
import time
import pybullet_data
import numpy as np
import matplotlib.pyplot as plt
import serial
import re
import keyboard


class MasterRobot(object):
    def __init__(self,set_sliders=False, set_cameras=True):
        self.physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
        p.setGravity(0,0,-0.981)
        p.resetDebugVisualizerCamera(cameraDistance=1, cameraYaw=0,
                                     cameraPitch=220, cameraTargetPosition=[0, 0.3, 0.2])
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
        self.ground = p.loadURDF("plane.urdf")
        urdfFlags = p.URDF_USE_SELF_COLLISION
        self.cubeStartOrientation = p.getQuaternionFromEuler([1.57,0,1.57])
        self.cubeStartOrientation_platform = p.getQuaternionFromEuler([1.57, 0, 0])
        self.cubeStartOrientation_circle = p.getQuaternionFromEuler([0, 0, 0])
        self.robot = p.loadURDF("master_robot_2/master_robot_2.urdf",[0, 0, 0], self.cubeStartOrientation,
                       flags=urdfFlags,
                       useFixedBase=True)
        self.SlaveRobot =  p.loadURDF("actuator2/actuator2.urdf", [-0.08, -0.15, 0.2], [0,0.5,0.5,0],
                                flags=urdfFlags,
                                useFixedBase=True)
        self.platform = p.loadURDF("platform_tmp9/platform_tmp9.urdf", [-0.08, 0.6, 0], self.cubeStartOrientation_platform,
                                   flags=urdfFlags,
                                   useFixedBase=True)
        # self.circle = p.loadURDF("circle_platform/circle_platform.urdf", [-0.08, 0.7, 0.2], self.cubeStartOrientation_circle,
        #                            flags=urdfFlags,
        #                            useFixedBase=True)
        self.mr_joints, self.sr_joints = self.get_joints()
        self.num_mr_joints = len(self.mr_joints)
        self.num_sr_joints = len(self.sr_joints)
        self.sr_arm_id = [1, 2, 3, 4, 5, 6]
        self.sr_yaw_id = [7, 9, 11, 13, 15, 17, 19, 21]
        self.sr_pitch_id = [8, 10, 12, 14, 16, 18, 20]  #
        self.sr_roll_shear = [22, 23, 24]


        self.simu_f = 75
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
        angles_data = self.openreadtxt("fromA2B.txt")
        angles_data_exchange = self.re_arrange(angles_data)
        p.stepSimulation()
        # time.sleep(5)
        for i in range(int(5e5)):
            t = i / self.simu_f
            self.update_camera_vision()
            # about serial
            # angls_from_Arduino = self.get_real_time_angle()
            # p_joints = self.get_target_P(angls_from_Arduino)
            p_joints =self.get_target_P(angles_data_exchange[i,:])
            # self.step(p_joints)
            self.step_master(p_joints)
            self.step_slave(p_joints)
            time.sleep(1/self.simu_f)
        p.disconnect()

    def run_key(self):
        p.stepSimulation()
        angles = np.zeros(self.num_mr_joints+1)
        angles[5] = 0.3
        resolution = np.deg2rad(1)
        on_press = self.make_on_press_callback(angles, resolution)
        keyboard.on_press(on_press)
        for i in range(int(5e3)):
            t = i / self.simu_f
            self.update_camera_vision()
            p_joints = angles

            self.step_master(p_joints)
            self.step_slave(p_joints)
            time.sleep(1 / self.simu_f)
        p.disconnect()



    def test_joint(self, joint_id):
        for i in range(10000):
            self.update_camera_vision()
            # if i % 20 == 0:
            #     target_p = np.sin(i) * np.pi / 2
            target_p = np.pi / 4
            p_joints = np.zeros((self.num_mr_joints))
            p_joints[joint_id] = target_p
            self.step(p_joints)
            p.stepSimulation()
            time.sleep(1/self.simu_f)
        p.disconnect()



    def get_joints(self):
        """
        this method is aim to get all joints for both master robot and slave robot
        :return: the information for two robots
        """
        mr_joints = []
        sr_joints = []
        for j in range(p.getNumJoints(self.robot)):
            # Disable motor in order to use direct torque control.
            info = p.getJointInfo(self.robot, j)
            joint_type = info[2]
            if (joint_type == p.JOINT_PRISMATIC or joint_type == p.JOINT_REVOLUTE):
                mr_joints.append(j)
                p.setJointMotorControl2(self.robot, j,
                                        controlMode=p.VELOCITY_CONTROL, force=0)
        mrjoints = mr_joints[0:]
        for a in range(p.getNumJoints(self.SlaveRobot)):
            info = p.getJointInfo(self.SlaveRobot, a)
            joint_type = info[2]
            if (joint_type == p.JOINT_PRISMATIC or joint_type == p.JOINT_REVOLUTE):
                sr_joints.append(a)
                p.setJointMotorControl2(self.SlaveRobot, a,
                                        controlMode=p.VELOCITY_CONTROL, force=0)
        srjoints = sr_joints[0:]
        return mrjoints, srjoints

    def step(self, control_array):
        """

        :param control_array: the target position array for two robot
        :return: null
        """
        if control_array is None:
            control_array = np.zeros(self.num_mr_joints)
        for j in range(self.num_mr_joints):
            p.setJointMotorControl2(self.robot, self.mr_joints[j], p.POSITION_CONTROL, control_array[j])
            if j == 1: # the move of small arm
                for i in self.sr_arm_id:
                    p_sr_arm =2* control_array[1] / len(self.sr_arm_id)
                    p.setJointMotorControl2(self.SlaveRobot, i, p.POSITION_CONTROL, p_sr_arm)
                    # print((control_array[1]))
                    # print(p_sr_arm)
                    # print("------")
            if j == 2: # the move of yaw link
                for i in self.sr_yaw_id:
                    p_sr_yaw = control_array[j] / len(self.sr_yaw_id)
                    p.setJointMotorControl2(self.SlaveRobot, i, p.POSITION_CONTROL, p_sr_yaw)
            if j == 3: # the move of pitch link
                for i in self.sr_pitch_id:
                    p_sr_pitch = control_array[j] / len(self.sr_pitch_id)
                    p.setJointMotorControl2(self.SlaveRobot, i, p.POSITION_CONTROL, p_sr_pitch)
            if j == 4: # the move of roll link
                p.setJointMotorControl2(self.SlaveRobot, self.sr_roll_shear[0], p.POSITION_CONTROL, control_array[j])

        p.setJointMotorControl2(self.SlaveRobot, 23, p.POSITION_CONTROL, 0)
        p.setJointMotorControl2(self.SlaveRobot, 24, p.POSITION_CONTROL, 0)

        p.stepSimulation()

    def step_master(self, control_array):
        if control_array is None:
            control_array = np.zeros(self.num_mr_joints)
        for j in range(self.num_mr_joints):
            p.setJointMotorControl2(self.robot, self.mr_joints[j], p.POSITION_CONTROL, control_array[j])

        p.stepSimulation()

    def step_slave(self, control_array):
        new_control_array = np.zeros(self.num_sr_joints)
        new_control_array[0] = control_array[0]
        for i in self.sr_arm_id:
            new_control_array[i] = control_array[1] / len(self.sr_arm_id)
        for i in self.sr_yaw_id:
            new_control_array[i] = control_array[2] / len(self.sr_yaw_id)
        for i in self.sr_pitch_id:
            new_control_array[i] = control_array[3] / len(self.sr_pitch_id)
        new_control_array[-3] = control_array[4]
        new_control_array[-2] = -0.4
        new_control_array[-1] = 0.4
        # new_control_array[-2] = -control_array[5]
        # new_control_array[-1] = control_array[5]

        for j in range(self.num_sr_joints):
            p.setJointMotorControl2(self.SlaveRobot, self.sr_joints[j], p.POSITION_CONTROL, new_control_array[j])

        p.stepSimulation()


    def get_real_time_angle(self):
        angles_from_Arduino = np.zeros(self.num_mr_joints)
        if ser == None:
            wind = " "
        else:
            wind = ser.readline()
        st = str(wind)  # 列表转换字符串
        sst = re.findall(r'\-?\d+\.?\d*', st)  # 字符串提取数字
        # print(sst)
        if sst == []:
            sst = 0
        else:
            for i in range(self.num_mr_joints):
                angles_from_Arduino[i] = float(sst[i])
        # print(angles_from_Arduino)
        return angles_from_Arduino



    def get_target_P(self, encoder_angles):
        """
        :param encoder_angles: it is a list/array that store the angles received from Arduino/Stm32
        :return: the target Position to robot
        """
        encoder_angles = self.list_deg2rad(encoder_angles)
        encoder_angles[0] = self.rad2distance(0.03, encoder_angles[0])
        return encoder_angles

    def make_on_press_callback(self, angles, resolution):
        def key_control(key):
            """
            this method is used to control robot by keyboard
            :param key: the detected key
            :param resolution: the minimum angle
            :return: target angles that will be sent to robot in simu
            """
            key_actions = {
                'e': (0, resolution),
                'd': (0, -resolution),
                's': (1, resolution),
                'f': (1, -resolution),
                'j': (2, resolution),
                'l': (2, -resolution),
                'i': (3, -resolution),
                'k': (3, resolution),
                'u': (4, resolution),
                'o': (4, -resolution),
                'q': (5, resolution),
                'r': (5, -resolution)
            }

            action = key_actions.get(key.name)
            if action is not None:
                index, value = action
                angles[index] += value

        return key_control

    ### this part is about visual and camera
    # def add_custom_sliders(self):
    #     for _i in range(4):
    #         p.addUserDebugParameter(self.abad_joint_Names[_i], -3.14, 3.14, 0)
    #         p.addUserDebugParameter(self.thigh_joint_Names[_i], -3.14, 3.14, 0)
    #         p.addUserDebugParameter(self.shank_joint_Names[_i], -3.14, 3.14, 0)

    def add_camera_sliders(self):
        self.camera_sliders.append(p.addUserDebugParameter('pitch', 180, 360, 220))
        self.camera_sliders.append(p.addUserDebugParameter('yaw', 0, 360, 130))
        self.camera_sliders.append(p.addUserDebugParameter('distance', 0, 2, 0.75))

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
    # set the Serial
    # ser = serial.Serial('COM6', 9600, timeout=1)
    ser =None
    # aa = open('D:\桌面\datas_serial.txt', 'w', encoding='utf-8')
    # ser.write("testing".encode())

    mr = MasterRobot()
    # pass
    # print("test the num of joint:")
    # print("num of mr:")
    # print(mr.num_mr_joints)
    # print("num of sr:")
    # print(mr.num_sr_joints)
    # mr.run_key()
    mr.run()
    # mr.test_joint(2)