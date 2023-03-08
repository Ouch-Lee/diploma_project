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

%% verify the algorithmn two segment 


for kt=1:2

for i=1:size(kappa,1)
    [H{i},~,p{i},F] = FK_n_segments(kappa(i,:),tau(kt,:),alpha,number_arc_interval,number_segments,disk_interval);
    for j=1:number_segments
        % the j th segment and the i th deformmation shape()t
%         arc{i,j}=p{i}(number_arc_interval_cumsum(j)+1:number_arc_interval_cumsum(j+1)+1,:);
        arc{kt,i,j}=p{i}(number_arc_interval_cumsum(j)+1:number_arc_interval_cumsum(j+1)+1,:);
    end
end

end
%% visualization
fig1=figure(1);
fig_setting;

for kt=1:2
subplot(1,2,kt);

for i=1:size(kappa,1)
    hold on;
    for j=1:number_segments
%         text=['plot3(arc{',num2str(i),',',num2str(j),...
%             '}(:,1),arc{',num2str(i),',',num2str(j),...
%             '}(:,2),arc{',num2str(i),',',num2str(j),'}(:,3));'];
        text=['plot3(arc{',num2str(kt),',',num2str(i),',',num2str(j),...
            '}(:,1),arc{',num2str(kt),',',num2str(i),',',num2str(j),...
            '}(:,2),arc{',num2str(kt),',',num2str(i),',',num2str(j),'}(:,3));'];
        eval(text);
        hold on;
    end
    line_setting;
    axes_setting;
%     drawnow();
%     pause(0.2)
%     generate_gif;
end

label_setting;
title_setting;
end




