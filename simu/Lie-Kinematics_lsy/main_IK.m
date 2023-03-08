clc;
clear;
close all;

% add path to main.m
addpath('Model/kinematics_ScrewTheory/');
addpath('Model/common/');
addpath('Parameter/');
addpath('Visulization\');

% import the parameters
parameter;

%% verify the algorithmn of some shapes

% square
tspan = 0:deg2rad(3):2*pi;

x_tip = 0.25*cos(tspan);
y_tip = 0.25*sin(tspan);
z_tip = 0.9*ones(1,length(tspan));
P_target = [x_tip; y_tip; z_tip];

% P_target=[0.2;0.4;0.6]

err_bound=0.001;
torsion_mode='0';
orientation_mode='0';
for i=1:size(P_target,2)
tic;
if i==1
[P_actual,kappa,tau,alpha,Delta_p,final_twist,iteration_times] = IK_n_segments...
    (P_target(:,i),...
    number_arc_interval,...
    number_segments,...
    length_arc,...
    err_bound,...
    torsion_mode,...
    orientation_mode,...
    disk_interval,[]);
else
    [P_actual,kappa,tau,alpha,Delta_p,final_twist,iteration_times] = IK_n_segments...
    (P_target(:,i),...
    number_arc_interval,...
    number_segments,...
    length_arc,...
    err_bound,...
    torsion_mode,...
    orientation_mode,...
    disk_interval,ft);
end
ft=final_twist;
% P_mat(:,i)=P_actual;
Delta_p;
Err_res(i,:)=Delta_p;
P_res(i,:)=P_actual';

ct(i,:)=toc;%final computation time
iter(i,:)=iteration_times%final iteration times

[H{i},~,p{i},F] = FK_n_segments(kappa(:,1),tau,alpha,number_arc_interval,number_segments,disk_interval);
for j=1:number_segments
        % the j th segment and the i th deformmation shape()t
    arc{i,j}=p{i}(number_arc_interval_cumsum(j)+1:number_arc_interval_cumsum(j+1)+1,:);
end
end

P_target=P_target';
%% visualization



fig1=figure(1);


fig_setting;

len=size(P_target,1);

subplot(4,2,[1,3,5,7]);
for i=1:size(P_target,1)
    
    
    ax_P_target=plot3(P_target(:,1),P_target(:,2),P_target(:,3),'Color','r','LineWidth',2,'LineStyle','-.');
    ax_P_target.Color(4)=1;
    hold on;
    ax_P_res=plot3(P_res(:,1),P_res(:,2),P_res(:,3),'Color','b','LineWidth',1);
    ax_P_res.Color(4)=1  ;
    
    if mod(i,round(len/4))==0
    for j=1:number_segments
        text=['plot3(arc{',num2str(i),',',num2str(j),...
            '}(:,1),arc{',num2str(i),',',num2str(j),...
            '}(:,2),arc{',num2str(i),',',num2str(j),'}(:,3));'];
        eval(text);
        hold on;
    end
    
    

    line_IK_setting;
    end
    axes_setting;
    legend('Desired','Simulated','Location','best')
%     drawnow();
%     pause(0.2)
%     generate_gif;
%     delete(ax);
    
end

label_setting;

% step=
subplot(4,2,2);
plot((P_res(:,1)-P_target(:,1))*1e3,'LineWidth',1,'Color','b');
set(gca,'FontWeight','bold');
ylabel('X(mm)','FontWeight','bold','FontSize', 12);
title('Tip position error','FontWeight','bold','FontSize', 12);
xlim([1,len]);

subplot(4,2,4);
plot((P_res(:,2)-P_target(:,2))*1e3,'LineWidth',1,'Color','b');
set(gca,'FontWeight','bold');
ylabel('Y(mm)','FontWeight','bold','FontSize', 12);
xlim([1,len]);

subplot(4,2,6);
plot((P_res(:,3)-P_target(:,3))*1e3,'LineWidth',1,'Color','b');
set(gca,'FontWeight','bold');
ylabel('Z(mm)','FontWeight','bold','FontSize', 12);
xlim([1,len]);

subplot(4,2,8);
plot(Err_res*1e3,'LineWidth',1,'Color','r');
set(gca,'FontWeight','bold');
ylabel('norm(mm)','FontWeight','bold','FontSize', 12);
xlabel('step','FontWeight','bold','FontSize', 12);
xlim([1,len]);