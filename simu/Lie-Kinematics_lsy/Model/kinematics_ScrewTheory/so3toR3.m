function [R3e] = so3toR3(so3e)
% so3toR3
% Author: Lin Siyuan
% Date :2023/02/07
% purpose: transfer the element in so3 to the element in R3
% Input: 
%   so3e: an element in so3
% Output:
%   R3e: an element in R3

R3e=[-so3e(2,3);so3e(1,3);-so3e(1,2)];
end

