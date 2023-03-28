$$
\begin{cases}
x_k = x_{k-1}  \\
y_k = x_k
\end{cases}
$$

$$
\begin{cases}
\hat{x}_{k|k-1} = F_{k-1} \hat{x}_{k-1}  + G_{k-1} \hat{u}_{k-1} \\
P_{k|k-1} =F_{k-1}P_{k-1} F_{k-1}^T + Q_{k-1} \\
K_k = P_{k|k-1}H_k^T(H_k P_{k|k-1} H_k^T + R_k)^{-1} \\
\hat{x}_{k} = \hat{x}_{k|k-1} + K(y_k - H\hat{x}_{k|k-1}) \\
P_k = (I - K_k H_k)P_{k|k-1}
\end{cases}
$$

$F_{k} = 1; H_k = 1; G_{k}=0; u_k = 0; $
$$
\begin{bmatrix}   c_4*s_5,&  c_4*c_5,   &    s_4,&   d_{14}  \\
s_{2 +3}*s_4*s_5 - c_{2 +3}*c_5,&  c_{2 + 3}*s_5 + s_{2 + 3}*c_5*s_4, & -s_{2 + 3}*c_4, &  d_{24}   \\
- s_{2 + 3}*c_5 - c_{2 + 3}*s_4*s_5, & s_{2 + 3}*s_5 - c_{2 + 3}*c_5*s_4,&  c_{2 + 3}*c_4,& d_{34}\\
 0,& 0, & 0, &1\end{bmatrix}
$$

$$
\begin{cases} d_{14} =d_2 + d_{t2} + a_{t3}*s_4 + d_5*s_4 \\
d_{24} =d_3*c_{2 + 3} - a_4*c_{2 + 3} - a_2*s_2 - a_{t3}*s_{2 + 3}*c_4 - d_5*s_{2 +3}*c_4\\ 
d_{34} =d_1 - a_4*s_{2 + 3} + d_3*s_{2 + 3} + a_2*c_2 + a_{t3}*c_{2 + 3}*c_4 + d_5*c_{2 + 3}*c_4 \end{cases}
$$

