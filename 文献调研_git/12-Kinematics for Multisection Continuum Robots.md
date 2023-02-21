# Kinematics for Multisection Continuum Robots

本篇文章发表于2006，主要介绍连续体机器人运动学模型的建立



## introduce

* 介绍连续体机器人/柔性机器人相对于刚性机器人的优势（也是一篇较不错对之前连续体研究的总结了）
* 介绍几种之前学者提出求解连续体运动学模型的方法，包括：
  * 将特定数学曲线和高自由度联系起来 - 局限性
  * 传动DH方法（把柔性看成刚性），不能应用于不包含棱柱关节或旋转关节的连续体机器人。

​	对[这篇象鼻机器人文章](https://onlinelibrary.wiley.com/doi/abs/10.1002/rob.10070)文章中提出的模型进行扩展，



# 建模方法

由于连续体机构没有显示的关节，因此不存在 $\theta \ d$ 的说法，文章作者的方法是使用连续体的长度和恒定（假设）的曲率来替代，连续体机器人运动学的一个关键问题是如何修改传统机器人运动学以适应这种情况。

借用上面提到象鼻文章中的结论，建立了  $\theta \ d$  和 曲率、长度、弯曲程度之间的函数关系

$$
[θ– d]^T=f_1(s,κ,ϕ)
$$
这样就可以根据连续体的“曲率、长度、弯曲程度”三参数求解末端位姿了

但是，驱动端能控制的是线缆的长度，因此还需要找到 三参数与长度 $l$ 之间的关系 
$$
(s,k,ϕ)=f_{2a}(l)
$$
整体模型梳理一下就是：
$$
{\underline {x}} ^{\rm D-H} \underline{\theta}, \underline{d}\leftarrow ^{{\underline f}_{1}}\leftarrow s, \kappa, \phi\leftarrow ^{{\underline f}_{2}} \leftarrow\underline{l}
$$
写成数学函数形式：
$$
{\underline x}= {\underline f}_{\rm D-H} \left({{\underline f}_{1} \left({{\underline f}_{2} ({\underline l})} \right)} \right)
$$
对于末端速度：
$$
\eqalignno{{{d} \underline {x} \over {dt}} =&\, {{\partial \underline {x}} \over {\partial \left(\underline {\theta}, \underline {d}\right)}} {{\partial \left(\underline {\theta}, \underline {d} \right)} \over {\partial \left({s,\kappa,\phi } \right)}} {{\partial \left({s,\kappa,\phi } \right)} \over {\partial \left(\underline {l}/ \underline {p}\right)}} {{d(\underline {l}/\underline {p})} \over {dt}}~~ \hbox{or} \cr \underline {\dot x}=&\, {\bf J}_{D - H} {\bf J}_{f_{1}} {\bf J}_{f_{2}} \left({\underline {\dot l}/\underline {\dot p} } \right) &\hbox{(4)}}
$$
其中$J_{D-H}$ 就是正常的雅可比矩阵，J1 是映射关系1求导的结果；J2是映射关系2的求导结果





### 推导第一个映射

将一段柔性连续体看作是四个转动关节+一个平动关节的刚性机构(为什么可以这样子，我现在也没有完全搞明白，似懂非懂)，可以模拟连续体偏转情况，下面这段话是对建模方法的解释：

```
位于躯干部分底部的前两个旋转关节将局部坐标系指向该部分的尖端。接下来，棱柱关节将局部坐标系平移到躯干的尖端。最后两个旋转关节然后将局部框架定向为指向躯干部分尖端的切线，以便后续的躯干部分将正确定向
```

第一对和最后一对变量是耦合的，这是由于概念上的刚性连杆机器人拟合恒定曲率连续主干的约束。因此，该模型仅包含三个自变量，而不是五个。

通过建立DH表格，可以求得齐次变换矩阵

