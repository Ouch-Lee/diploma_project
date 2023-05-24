import keyboard
import time

def on_key_press(key):
    print(f"Key '{key.name}' pressed.")

# 注册回调函数
keyboard.on_press(on_key_press)

while True:
    print("Program is running...")
    time.sleep(1)
