function norm_u = Calculate_norm_u(x1,x2)
% Calculate_norm_u
% Author: Lin Siyuan
% Date : 2023/02/25
% Purpose: Compute the norm of u related to the orientation

%% Input: 
%   x1: if nargin=1: it is a 3/time3 1 vector, represents the twist
%      if nargin=2: it is a scalar, represents the curvature \kaapa
%   x2: if nargin=1: you don't need to input it
%      if nargin=2: it is a scalar, represents the torsion \tau
%% Output:
%   norm_u: the norm of u related to the orientation

if nargin==1
    norm_u=norm(x1);
elseif nargin==2
    norm_u=sqrt(x1^2+x2^2);
end

end

