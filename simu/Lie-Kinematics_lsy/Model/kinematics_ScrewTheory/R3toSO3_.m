function [SO3e] = R3toSO3_(R3e,s)
% R3toSO3_
% Author: Lin Siyuan
% Date : 2023/02/09
% purpose: transfer the element in R3 to the element in SO3
% Input: 
%   R3e: an element in R3
%   s: a scalar 
% Output:
%   SO3e: an element in SO3 
so3e=[0,      -R3e(3), R3e(2);...
      R3e(3), 0,      -R3e(1);...
     -R3e(2), R3e(1),  0];
normR3=norm(R3e);
if normR3==0
    error("the omega can't be zero vector!");
else
    SO3e=eye(3)+so3e/(normR3)*sin(normR3*s)+(so3e^2/((normR3)^2))*(1-cos(normR3*s));
end
end

