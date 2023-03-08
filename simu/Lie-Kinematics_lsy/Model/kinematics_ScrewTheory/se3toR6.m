function [R6e] = se3toR6(se3e)
% se3toR6
% Author: Lin Siyuan
% Date :2023/02/08
% purpose: transfer the element in se3 to the element in R6
% Input: 
%   se3e: an element in se3
% Output:
%   R6: an element in R6 [v,u(omega)]
R6e=[se3e(1:3,4);so3toR3(se3e(1:3,1:3))];
end

