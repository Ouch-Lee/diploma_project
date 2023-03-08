function [Hmat_sep,...
        Hmat_cum,...
        Ad_Hmat_cum,...
        Integral_exp_ad,...
        J_origin,...
        J_final] =... 
Calculate_all_Hmat(f,length_arc,torsion_mode,orientation_mode)
% Calculate_Ad_mat_
% Author: Lin Siyuan
% Date : 2023/02/25
% Purpose: Compute Homogenous matrix of two form: 
% seperated and multiplied

%% Input: 
%   f:  a 6n \times 1 vector, containing n twist, each twist has a form of
%       [v,u]
%   length_arc: a n \times 1 vector, containing the length of each segments
%   torsion_mode: mode='0' the torsion is not considered
%         mode='1' the torsion is considered
%% Output:
%   Hmat_sep: homogenous matrix (seperated form)
%   Hmat_cum: homogenous matrix (multiplied form) 
%   Ad_Hmat_cum: Adjoint matrix of homogenous matrix (multiplied form) 
%               we only need to 1:end-1 to calculate Jacobian matrix
%   Integral_exp_ad: integral of exponential of adjoint matrix
%   J_origin: the original Jacobian matrix 6*6n
%   J_final: the final Jacobian matrix 
if nargin==2
    torsion_mode='0';
    orientation_mode='0';
end

number_segments=size(f,1)/6;
f_=reshape(f,6,[]);
Hmat_sep=cell(number_segments+1,1);
Hmat_cum=cell(number_segments+1,1);
Ad_Hmat_cum=cell(number_segments,1);
Integral_exp_ad=cell(number_segments,1);
J_origin=cell(1,number_segments);
J_final=cell(1,number_segments);
Hmat_sep{1}=eye(4);
Hmat_cum{1}=Hmat_sep{1};

for i=2:number_segments+1
    Hmat_sep{i}=R6toSE3_(f_(:,i-1),length_arc(i-1));
    Hmat_cum{i}=Hmat_cum{i-1}*Hmat_sep{i};  
end

for i=1:number_segments
    Ad_Hmat_cum{i}=Calculate_Ad_mat_(Hmat_cum{i});
    u=f_(4:6,i);
    norm_u=Calculate_norm_u(u);
    ad_Hmat_cum=Calculate_ad_mat(f_(:,i));
    Integral_exp_ad{i}=Calculate_integeral_exp_ad(length_arc(i),norm_u,ad_Hmat_cum);
    J_origin{i}=Ad_Hmat_cum{i}*Integral_exp_ad{i};
    
    if torsion_mode=='0' && orientation_mode=='0'
        % the torsion and  is not considered，the orientation is not
        % given
        J_final{i}=J_origin{i}(1:3,4:5);
    elseif torsion_mode=='0' && orientation_mode=='1'
        % the torsion and  is not considered，the orientation is given
        J_final{i}=J_origin{i}(:,4:5);
    elseif torsion_mode=='1'  && orientation_mode=='0'
        % the torsion is considered, the orientation is not considered 
        J_final{i}=J_origin{i}(1:3,4:6);
    elseif torsion_mode=='1'  && orientation_mode=='1'
        % the torsion is considered, the orientation is considered 
        J_final{i}=J_origin{i}(:,4:6);
    end

end
J_origin=cell2mat(J_origin);
J_final=cell2mat(J_final);
end

