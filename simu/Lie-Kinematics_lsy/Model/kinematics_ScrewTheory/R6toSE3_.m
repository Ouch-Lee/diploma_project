function [SE3e] = R6toSE3_(R6e,s)
% R6toSE3_
% Author: Lin Siyuan
% Date : 2023/02/09
% purpose: transfer the element in R6 to the element in SE3
% Input: 
%   R6e: an element in R6 [v,u(omega)]
% Output:
%   se3e: an element in SE3


u=R6e(4:6);
v=R6e(1:3);
if abs(u(1))+abs(u(2))+abs(u(3))==0
    SE3e=[eye(3),v*s;...
    0,0,0,1];
else
    SO3e=R3toSO3_(u,s);
    SE3e=[SO3e,((eye(3)-SO3e)*cross(u,v))/((norm(u))^2)+(u*u'*v*s)/((norm(u))^2);...
    0,0,0,1];
end

end

