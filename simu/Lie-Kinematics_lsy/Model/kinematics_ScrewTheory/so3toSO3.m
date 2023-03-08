function [SO3e] = so3toSO3(so3e,s)
% so3toSO3
% Author: Lin Siyuan
% Date :2023/02/07
% purpose: transfer the element in so3 to the element in SO3
% Input: 
%   so3e: an element in so3
% Output:
%   SO3e: an element in SO3
normR3=norm(so3toR3(so3e));
if normR3==0
    error("the omega can't be zero vector!");
else
SO3e=eye(3)+so3e/(normR3)*sin(normR3*s)+(so3e^2/((normR3)^2))*(1-cos(normR3*s));
end
end

