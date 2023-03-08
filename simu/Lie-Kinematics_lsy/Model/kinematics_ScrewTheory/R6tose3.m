function [se3e] = R6tose3(R6e)
% R6tose3
% Author: Lin Siyuan
% Date : 2023/02/09
% purpose: transfer the element in R6 to the element in se3
% Input: 
%   R6e: an element in R6 [v,u(omega)]
% Output:
%   se3e: an element in se3

so3e=R3toso3(R6e(4:6));
se3e=[so3e,R6e(1:3);...
    0,0,0,1];

end

