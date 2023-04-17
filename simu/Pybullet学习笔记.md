# Pybullet学习笔记

[toc] 

## Introduction

### SaveWorld

好像是说把现有的文件直接储存？目前还没用过不知道作用是什么

### SaveState 

saveworld好像是存储整个仿真世界的信息，而savestate还可以把机器人的关节位置，速度等更细节的信息给存储下来

### creatVisualShape / creatMutipleBody

就是说pybullet也支持直接在里面创建可视化的，有物理参数的几何体，但是一般还是直接导入urdf文件比较方便

### StepSimulation  / setRealTimeSimulation

stepSimulation将在一个前向动力学模拟步骤中执行所有动作，如碰撞检测、约束求解和集成。

翻译是这么说，我感觉就是仿真的一个周期

setRealTimeSimulation 是 StepSimulation  的进阶版，是根绝实时的时钟进行仿真的





## Control Robot

## Joint 相关函数

* getNumJoints : 返回关节个数

* getJointInfo：返回关节信息，传入参数包括机器人变量，关节的ID，返回一堆参数，具体见手册

* setJointMotorControl2/Array： 控制电机的函数，可以有位置、速度、力矩三种控制模式

  需要的参数：机器人变量、关节ID、控制模式、还有一些选填的参数来设置最大速度、力矩、位置

* setJointMotorControlArray：和上面差不多，但是关节ID可以直接输入数组

* getJointState(s)：上面getIfon返回的信息偏标签，而这个函数则是返回一些物理参数，包括速度，位置，6维力，电机力矩

## Base相关函数

* getBaseVelocity：传入self就能得到速度相关信息
* 

### Initial





### Run





### Step







## Camera

