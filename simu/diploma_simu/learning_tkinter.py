from tkinter import *



# 进入消息循环
window= Tk()  # 创建窗口对象的背景色
# 创建两个列表
# window.
window.title("title API")
lbl = Label(window, text="Hello",font = ("Arial Bold", 20))

def just_click():
    lbl.configure(text="the ass was clicked")

butt = Button(window, text= "ass", command=just_click)
lbl.grid(column=5, row=0)
butt.grid(column= 5, row = 10)
window.geometry("350x200")
# angles = [["theta1",60],["theta2",90],["theta3",120],["theta4",30],["theta5",45]]
# li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# movie = ['CSS', 'jQuery', 'Bootstrap']
# listb = Listbox(root)  # 创建两个列表组件
# listb2 = Listbox(root)
# list_angles = Listbox(root)
# for item in li:  # 第一个小部件插入数据
#     listb.insert(0, item)
#
# for item in movie:  # 第二个小部件插入数据
#     listb2.insert(0, item)
#
# for item in angles:
#     list_angles.insert(0,item)
#
# listb.pack()  # 将小部件放置到主窗口中
# listb2.pack()
# list_angles.pack()
window.mainloop()  # 进入消息循环