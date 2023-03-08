function [Ad_mat] = Calculate_Ad_mat_(x1,x2)
% Calculate_Ad_mat_
% Author: Lin Siyuan
% Date : 2023/02/25
% Purpose: Compute the Adjoint matrix(Ad)

%% Input: 
%   x1: if nargin=1: it is a 4\times 4 homogenous matrix, which is [R,p;0,1]
%      if nargin=2: it is a 3\times 3 rotation matrix, which is R
%   x2: if nargin=1: you don't need to input it
%      if nargin=2: it is a 3\times 1 position vector, which is p
%% Output:
%   Ad_mat: the Adjoint matrix(Ad)
if nargin==1
    R=x1(1:3,1:3);
    p_=R3toso3(x1(1:3,4)); 
elseif nargin==2
    R=x1;
    p_=R3toso3(x2);% p_ is in the so3
end
Ad_mat=[R,p_*R;...
    zeros(3),R];
end

