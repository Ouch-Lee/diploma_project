import keyboard
import numpy as np
import time





    # print(angles)



def make_on_press_callback(angles, resolution):
    def key_control(key):
        """
        this method is used to control robot by keyboard
        :param key: the detected key
        :param resolution: the minimum angle
        :return: target angles that will be sent to robot in simu
        """
        key_actions = {
            'w': (0, resolution),
            's': (0, -resolution),
            'a': (1, resolution),
            'd': (1, -resolution),
            'j': (2, resolution),
            'l': (2, -resolution),
            'i': (3, resolution),
            'k': (3, -resolution),
            'u': (4, resolution),
            'o': (4, -resolution)
        }

        action = key_actions.get(key.name)
        if action is not None:
            index, value = action
            angles[index] += value
    return key_control


# def on_space_pressed(event):
#     global number
#     number += 1
#     print("当前数字为:", number)


# keyboard.on_press(control_task)
# keyboard.on_press_key("space", on_space_pressed)

if __name__ == '__main__':
    # time.sleep()
    angles = np.zeros(5)
    resolution = 0.5
    on_press = make_on_press_callback(angles, resolution)
    keyboard.on_press(on_press)
    for i in range(int(5e3)):
        print(angles)
        print("-----------")
        time.sleep(0.5)
