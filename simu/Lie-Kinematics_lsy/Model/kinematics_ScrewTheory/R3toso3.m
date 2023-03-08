function [so3e] = R3toso3(R3e)
% R3toso3
% Author: Lin Siyuan
% Date : 2023/02/07
% purpose: transfer the element in R3 to the element in so3
% Input: 
%   R3e: an element in R3
% Output:
%   so3e: an element in so3
so3e=[0,      -R3e(3), R3e(2);...
      R3e(3), 0,      -R3e(1);...
     -R3e(2), R3e(1),  0];
end

