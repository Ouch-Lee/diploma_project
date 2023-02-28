## DH建模方法复习：

* 坐标系配置需要满足条件：
  * 坐标轴 $x_{i+1}$ 垂直于坐标轴$z_i$
  * 坐标轴 $x_{i+1}$ 与坐标轴$z_i$相交
* 四个主要参数
  *  **a** 是轴 $z_i$ 与 $z_{i+1}$之间沿轴线 $x_{i+1}$ 之间的距离
  *  **$\alpha$** 是垂直于 $x_{i+1}$ 平面测得两个z轴之间的夹角，正向从 i 到 i+1
  *  **d** 是从坐标系i原点o到轴线 $x_{i+1}$与$z_i$交点 o' 之间的距离
  *  **$\theta$** 是垂直于$z_i$平面从两个x轴之间的夹角，同样遵循从低到高为＋


| link | $a_i$ | $\alpha_i$ |    $d_i$    |    $\theta_i$    |
| :--: | :---: | :--------: | :---------: | :--------------: |
|  1   |   0   |     90     | **$d_1^*$** |        90        |
|  2   |  a2   |     0      |     d2      | $90+\theta_2^*$  |
|  t2  |   0   |     90     |     dt2     |   $\theta_3^*$   |
|  3   |   0   |     0      |     d3      |        90        |
|  t3  |  at3  |    -90     |      0      | $-90+\theta_4^*$ |
|  4   |  a4   |     90     |      0      |        90        |
|  5   |   0   |     0      |     -d5     |   $\theta_5^*$   |

**$d_1^*$** : 0-130mm

a2 = 218.55mm  ;  d2 = 60.1mm

dt2 = 165mm

d3 = 155

at3 = 145 //为什么这两个不相等？

a4 = 155

d5 = 15



借助matlab计算得到二连杆部分（控制主要朝向）的齐次变换矩阵如下：
$$
\begin{bmatrix} -sin(3),& -cos(3)*sin(4), & cos(3)*cos(4),&  -a4*sin(3) + d3*sin(3) + at3*cos(3)*cos(4)\\
cos(3),&  -sin(3)*sin(4),& cos(4)*sin(3),&  at3*cos(4)*sin(3) - d3*cos(3) + a4*cos(3)\\
         0,&   cos(4),&      sin(4),&                           dt2 + at3*sin(4) \\
        0,&                      0,&                       0,&                                                             1\end{bmatrix}
$$
$$
[-sin(theta3), -cos(theta3)*sin(theta4), cos(theta3)*cos(theta4), d3*sin(theta3) - a4*sin(theta3) + at3*cos(theta3)*cos(theta4)] \\
[ cos(theta3), -sin(theta3)*sin(theta4), cos(theta4)*sin(theta3), a4*cos(theta3) - d3*cos(theta3) + at3*cos(theta4)*sin(theta3)] \\
[           0,              cos(theta4),             sin(theta4),                                         dt2 + at3*sin(theta4)]\\
[           0,                        0,                       0,                                                             1]
$$



二连杆+小臂偏转部分（整体控制朝向）的齐次变换矩阵：
$$
[cos(2 + 3), -sin(2 + 3)*sin(4), -sin(2 + 3)*cos(4), a4*cos(2 + 3) + d3*cos(2 + 3) - a2*sin(2) - at3*sin(2 + 3)*cos(4)] \\
[sin(2 + 3),  cos(2 + 3)*sin(4),  cos(2 + 3)*cos(4), a4*sin(2 + 3) + d3*sin(2 + 3) + a2*cos(2) + at3*cos(2 + 3)*cos(4)] \\
[                   0,                      -cos(4),                       sin(4),                                                                                d2 + dt2 + at3*sin(4)] \\
[                   0,                                 0,                                  0, 1]
$$

$$
\begin{bmatrix}   c_4*s_5,&  c_4*c_5,   &    s_4,&    d2 + dt2 + at3*s_4 + d5*s_4 \\
s_{2 +3}*s_4*s_5 - c_{2 +3}*c_5,&  c_{2 + 3}*s_5 + s_{2 + 3}*c_5*s_4, & -s_{2 + 3}*c_4, &     d3*c_{2 + 3} - a4*c_{2 + 3} - a2*s_2 - at3*s_{2 + 3}*c_4 - d5*s_{2 +3}*c_4\\
- s_{2 + 3}*c_5 - c_{2 + 3}*s_4*s_5, & s_{2 + 3}*s_5 - c_{2 + 3}*c_5*s_4,&  c_{2 + 3}*c_4,& d1 - a4*s_{2 + 3} + d3*s_{2 + 3} + a2*c_2 + at3*c_{2 + 3}*c_4 + d5*c_{2 + 3}*c_4\\
 0,& 0, & 0, &1\end{bmatrix}
$$



由于两边旋转矩阵所得结果不同，因此尝试另外一种坐标系配备，并计算出对应的齐次变化矩阵如下：
$$
[-cos(3),  sin(3)*sin(4),  cos(4)*sin(3), a1*cos(3) - a3*cos(3) + at2*cos(4)*sin(3)] \\
[-sin(3), -cos(3)*sin(4), -cos(3)*cos(4), a1*sin(3) - a3*sin(3) - at2*cos(3)*cos(4)]\\
[           0,             -cos(4),              sin(4),                                               at2*sin(4)]\\
[           0,                        0,                        0,                                                             1]
$$



## 连续体

DH-table 

| link | $a_i$ | $\alpha_i$ |  $d_i$  |  $\theta_i$   |
| :--: | :---: | :--------: | :-----: | :-----------: |
|  1   |   0   |     90     |    0    | $\theta_1 ^*$ |
|  2   |   0   |    -90     |    0    | $\theta_2^*$  |
|  3   |   0   |     90     | $d_3^*$ |       0       |
|  4   |   0   |    -90     |    0    | $\theta_4^*$  |
|  5   |   0   |     0      |   -0    | $\theta_5^*$  |

$$
\theta_1 = -\theta_5 = \phi \\
\theta_2 = \theta_4 = \frac{ks}{2} \\
d_3 = \frac{2}{k} sin(\frac{ks}{2})
$$



## 控制策略

目前，通过齐次变化矩阵和编码器测量得到的数，我可以计算得到末端手指的位置和朝向，并实时检测其变化；那么现在我要如何将这个变化映射到末端呢

为了构造起始和初始相同的坐标系，配置了新的坐标系，写出对应的DH表：

| link | $a_i$ | $\alpha_i$ | $d_i$ |    $\theta_i$    |
| :--: | :---: | :--------: | :---: | :--------------: |
|  e1  |   0   |    -90     |   0   |       -90        |
|  2   |   0   |    -90     |   0   |       -90        |
|  t2  |   0   |     90     |  dt2  |   $\theta_3^*$   |
|  3   |   0   |     0      |  d3   |        90        |
|  t3  |  at3  |    -90     |   0   | $-90+\theta_4^*$ |
|  4   |  a4   |     90     |   0   |       -90        |

$$
\begin{bmatrix}cos(t3), & sin(t3)*sin(t4), & cos(t4)*sin(t3), &a4*cos(t3) + d3*cos(t3) - at3*cos(t4)*sin(t3) \\
    0,   &      -cos(t4),      &    sin(t4),            &               - dt2 - at3*sin(t4) \\
sin(t3),& -cos(t3)*sin(t4), &-cos(t3)*cos(t4), &a4*sin(t3) + d3*sin(t3) + at3*cos(t3)*cos(t4) \\
0,    &            0,         &       0,      &                                       1\end{bmatrix}
$$

