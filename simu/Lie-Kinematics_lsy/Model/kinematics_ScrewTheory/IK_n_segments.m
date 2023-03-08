function [P_actual,kappa,tau,alpha,Delta_p,final_twist,iteration_times] = IK_n_segments...
    (P_target,...
    number_arc_interval,...
    number_segments,...
    length_arc,...
    err_bound,...
    torsion_mode,...
    orientation_mode,...
    disk_interval, ...
    initial_twist)
% forward_n_segments
% Author: Lin Siyuan
% Date : 2023/02/26
% Purpose: compute the inverse kinematic model of n-segments continuum robot with
% the given position (or add orientation)

%% Input: 
%   P_target: the target position
%   number_arc_interval: the number of the interval in every arc, the first arc has k(1)+1，
%           the second has k(2), ... the whole continuum robot has sum(k)+1, you
%          must set it as a n*1 vector 
%   number_segments: the number of continuum robot segments, it is a scalar
%   length_arc: the length of each arc
%   err_bound: error bound for computation
%   torsion_mode: choose if torsion has an effect on the shape
%   orientation_mode: choose only position and any orientation: 0
%                     choose only position and given orientation: 1
%   disk_interval: the distance interval between the discs of continuum robot,
%            it is a scalar
%   initial_twist: initial twist 6n*1 vector
% 
%% Output:
%   kappa: all the arc curvature, you'd better set it as a n*1 vector
%   tau: all the arc torsion, you can set it as zero, you'd better set it
%        as a n*1 vector 
%   alpha: the angle between the bending plane and the local +X axis, you
%          must set it as a n*1 vector
%   final_twist: final twist 6n*1 vector
%   iteration_times: the iteration times 


if isempty(initial_twist)
    initial_twist=reshape(repmat([0;0;1;0;0;0],1,number_segments),[],1);
end
% f=[0;0;1;0;0;0;...
%     0;0;1;-1.088279618540531;0.628318530717959;0;
%     0;0;1;-1.256637061435917;1.176559237081062;0];
% f=[0;0;1;0;0;0;...
%     0;0;1;-1.1;0.628318530717959;0;
%     0;0;1;-1.256637061435917;2.2;0];
d=min(length_arc)/50;
[~,~,p,~]=FK_n_segments_twist(initial_twist,number_arc_interval,number_segments,disk_interval);
p_end=p(end,:);
P_actual=p_end';


delta_p=P_target-P_actual;
if norm(delta_p)>10*d
    delta_p_mv=10*d*delta_p/norm(delta_p);
elseif norm(delta_p)>5*d
    delta_p_mv=5*d*delta_p/norm(delta_p);
elseif norm(delta_p)>2*d
    delta_p_mv=2*d*delta_p/norm(delta_p);
else
    delta_p_mv=delta_p;
end
Delat_p=norm(delta_p);
err=Delat_p(1);
if orientation_mode=='0'
    err_creteria=err > err_bound;
elseif orientation_mode=='1'
    err_creteria=err > err_bound;
end
i=1;
maxiteration=1000;


while err_creteria && i < maxiteration
    
    [~,~,~,~,~,J_final]=Calculate_all_Hmat(initial_twist,length_arc,torsion_mode,orientation_mode);
%     M=J_final*J_final';
    M=J_final'*J_final;
    A=diag(diag(M));
% Levenberg-Marquardt-Mathod can convege
    delta_u=inv(J_final'*J_final+0.8*A)*J_final'*delta_p_mv;

% Levenberg-Marquardt-Mathod can convege
%   delta_u=inv(J_final'*J_final)*J_final'*delta_p_mv;

%   Moore–Penrose inverse: converge but slow
%     delta_u=J_final'*inv(J_final*J_final')*delta_p_mv;

%   Jacobian transpose method: converge but slow
%       delta_u=J_final'*delta_p_mv;

%   matlab M-P inverse method: not always converge
%       delta_u=pinv (J_final)*delta_p_mv;

%     fun=@(delta_u)J_final*delta_u-delta_p_mv;
%     options=optimoptions('fsolve',...
%         'Display','off','Algorithm', 'levenberg-marquardt');

    f_mat=reshape(initial_twist,6,[]);% f's form of matrix
    if torsion_mode=='1'
%         delta_u0=ones(3*number_segments,1);
%         delta_u=fsolve(fun,delta_u0,options);

        u_mat=f_mat(4:6,:);
        delta_u_mat=reshape(delta_u,3,[]);
        u_mat=u_mat-delta_u_mat;
        f_mat(4:6,:)=u_mat;
    elseif torsion_mode=='0'
%         delta_u0=ones(2*number_segments,1);
%         delta_u=fsolve(fun,delta_u0,options);

        u_mat=f_mat(4:5,:);
        delta_u_mat=reshape(delta_u,2,[]);
        u_mat=u_mat-delta_u_mat;
        f_mat(4:5,:)=u_mat;
    end
    initial_twist=reshape(f_mat,[],1);
    [~,~,p,~]=FK_n_segments_twist(initial_twist,number_arc_interval,number_segments,disk_interval);
    i=i+1;
    p_end=p(end,:);
    P_actual=p_end';
    delta_p=P_target-P_actual;
    if norm(delta_p)>10*d
        delta_p_mv=10*d*delta_p/norm(delta_p);
    elseif norm(delta_p)>5*d
        delta_p_mv=5*d*delta_p/norm(delta_p);
    elseif norm(delta_p)>2*d
        delta_p_mv=2*d*delta_p/norm(delta_p);
    else
        delta_p_mv=delta_p;
    end
    Delta_p=norm(delta_p);
    err=Delta_p;
%     disp(err);
    err_creteria=err > err_bound;
    
end
iteration_times=i
if i==1
    f_mat=reshape(initial_twist,6,[]);% f's form of matrix
    if torsion_mode=='1'
%         delta_u0=ones(3*number_segments,1);
%         delta_u=fsolve(fun,delta_u0,options);

        u_mat=f_mat(4:6,:);
    elseif torsion_mode=='0'
%         delta_u0=ones(2*number_segments,1);
%         delta_u=fsolve(fun,delta_u0,options);

        u_mat=f_mat(4:5,:);

    end
    Delta_p=norm(P_actual-P_target);
end
if err_creteria
    disp('it does not converge!')
else
    
    
end

final_twist=initial_twist;

if torsion_mode=='1'
    tau=(u_mat(3,:))';
else
    tau=zeros(number_segments,1);
end
for i=1:number_segments
    kappa(i,:)=sqrt((u_mat(1,i))^2+(u_mat(2,i))^2);
    
    alpha(i,:)=-atan2(u_mat(1,i),u_mat(2,i));
end

end

