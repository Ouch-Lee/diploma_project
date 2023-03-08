function [H,R,p,F] = FK_n_segments_twist(f,number_arc_interval,number_segments,disk_interval)
% forward_n_segments
% Author: Lin Siyuan
% Date : 2023/02/10
% Purpose: compute the kinematic model of n-segments continuum robot with
% the given parameters kappa, tau and alpha

%% Input: 
%   kappa: all the arc curvature, you'd better set it as a n*1 vector
%   tau: all the arc torsion, you can set it as zero, you'd better set it
%        as a n*1 vector 
%   alpha: the angle between the bending plane and the local +X axis, you
%          must set it as a n*1 vector
%   number_arc_interval: the number of the interval in every arc, the first arc has k(1)+1，
%           the second has k(2), ... the whole continuum robot has sum(k)+1, you
%          must set it as a n*1 vector 
%   number_segments: the number of continuum robot segments, it is a scalar
%   disk_interval: the distance interval between the discs of continuum robot,
%            it is a scalar
%   F: the twist vector as a cell n* (6\times 1)
%% Output:
%   H: the homogenous matrix of each center of discs, set by the form of
%      n*16 vector, the i th row means the i th homogenous matrix.
%   R: the rotation matrix of each center of discs, set by the form of
%      n*9 vector, the i th row means the i th rotation matrix.
%   p: the position vector of each center of discs, set by the form of n*3，
%      the i th row mean the i th position vector.

% set the origin's H、R、p
H(1,:)=reshape(eye(4),1,[]);
R(1,:)=reshape(eye(3),1,[]);
p(1,:)=[0,0,0];

t=cumsum([0;number_arc_interval]);

% compute
H0=eye(4);% initial homogenous matrix
% the derivative of position in the local frame
v=[0;0;1];
F=f;f=reshape(f,6,[]);
for i=1:number_segments
    for k=1:number_arc_interval(i)
        H(t(i)+1+k,:)=reshape((H0*R6toSE3_(f(:,i),k*disk_interval))',1,[]);
        R(t(i)+1+k,:)=H(t(i)+1+k,[1:3,5:7,9:11]);
        p(t(i)+1+k,:)=H(t(i)+1+k,[4,8,12]);
    end
    H0=(reshape(H(t(i)+1+k,:),4,4))';
end

end

