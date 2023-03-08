function [ad_mat] = Calculate_ad_mat(x1,x2)
% Calculate_ad_mat
% Author: Lin Siyuan
% Date : 2023/02/25
% Purpose: Compute the adjoint matrix(ad)

%% Input: 
%   x1: if nargin=1: it is a 6\times 1 twist, which is [v;u]
%      if nargin=2: it is a 3\times 1 vector, which is v related to
%      position
%   x2: if nargin=1: you don't need to input it
%      if nargin=2: it is a 3\times 1 vector, which is u related to
%      orientation
%% Output:
%   ad_mat: the adjoint matrix(ad)
if nargin==1
    v=x1(1:3,:);
    u=x1(4:6,:); 
elseif nargin==2
    v=x1;
    u=x2;
end
ad_mat=[R3toso3(u),R3toso3(v);...
    zeros(3),R3toso3(u)];
end

