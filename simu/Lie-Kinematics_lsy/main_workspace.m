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
kappa=pi/2*rand(10000,3);
alpha=2*pi*rand(10000,3);
tau=zeros(10000,3);
for i=1:size(kappa,1)
    [~,~,p,~] = FK_n_segments(kappa(i,:),tau(i,:),alpha(i,:),number_arc_interval,number_segments,disk_interval);
    p_res(i,:)=(p(end,:))';
end
scatter3(p_res(:,1),p_res(:,2),p_res(:,3),'.');