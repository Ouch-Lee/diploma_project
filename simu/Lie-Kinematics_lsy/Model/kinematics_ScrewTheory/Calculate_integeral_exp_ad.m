function [T] = Calculate_integeral_exp_ad(length_arc,norm_u,ad_mat)
% Integral_exp_ad
% Author: Lin Siyuan
% Date : 2023/02/25
% Purpose: Integral of the exponential of the adjoint matrix

%% Input: 
%   length_arc: the length of each arc, it doesn't means the length from
%   orign, scalar
%   norm_u: the norm of u, norm_w = sqrt(u1^2 + u2^2 + u3^2), scalar
%   ad_mat: the adjoint matrix, 6×6 matrix
%% Output:
%   T: the result of integral of the expointial of the adjoint matrix

ln=length_arc*norm_u;

if norm_u~=0
    T=length_arc*eye(6)+...
        (4-4*cos(ln)-ln*sin(ln))/(2*norm_u^2)*ad_mat+...
        (4*ln-5*sin(ln)+ln*cos(ln))/(2*norm_u^3)*ad_mat^2+...
        (2-2*cos(ln)-ln*sin(ln))/(2*norm_u^4)*ad_mat^3+...
        (2*ln-3*sin(ln)+ln*cos(ln))/(2*norm_u^5)*ad_mat^4;
elseif norm_u==0
    T=length_arc*eye(6)+0.5*length_arc^2*ad_mat;
end
end

