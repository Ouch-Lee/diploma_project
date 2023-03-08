clc;
clear;
close all;

% add path to main_paper.m
addpath('Model/kinematics_ScrewTheory/');
addpath('Model/common/');
addpath('Parameter/');

% import the parameters
parameter_paper;

% verify the algorithm
%% paper reproduction

v=[0;0;1];% the derivative of position vector

% for i=1:length(kappa)% Single-segment [Constant Curvature] and Single-segment [Constant Curvature and Torsion Test-1]
for i=1:length(tau)% Single-segment [Constant Curvature and Torsion Test-2]  

%     u{i}=[-kappa(i)*sin(alpha);kappa(i)*cos(alpha);tau];% Single-segment [Constant Curvature] and Single-segment [Constant Curvature and Torsion Test-1]
    u{i}=[-kappa*sin(alpha);kappa*cos(alpha);tau(i)];% Single-segment [Constant Curvature and Torsion Test-2]  
    
    f{i}=[v;u{i}];% the elment in R6 called twist
    k=1;
    for s=L_seq %the length
        SE3e=R6toSE3_(f{i},s);
        position(k,:)=(SE3e(1:3,4))';%only need position to plot the line
        k=k+1;
    end
    Pos{i}=position;
end

% visualization
figure(1);
axis equal;

% for i=1:length(kappa)% % Single-segment [Constant Curvature] and Single-segment [Constant Curvature and Torsion Test-1]
for i=1:length(tau)% Single-segment [Constant Curvature and Torsion Test-2]  
    
    plot3(Pos{i}(:,1),Pos{i}(:,2),Pos{i}(:,3));
    hold on;
end
axis([-1,1,-1,1]);
grid on;



