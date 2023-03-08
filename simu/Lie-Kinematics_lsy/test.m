% clc;
% clear;
% close all;
% 
% % add path to main.m
addpath('Model/kinematics_ScrewTheory/');
addpath('Model/common/');
addpath('Parameter/');
addpath('Visulization\');
% 
% % import the parameters
% parameter;

for i=1:3
	%打开的fig文件酌情修改路径
    hf(i)=open(['.\fig1-',num2str(i),'.fig']);%打开fig
    fig(i)=get(hf(i), 'CurrentAxes');%获取绘制的图像
end
%新建一个图窗
figure

for i=1:3
	%看要绘制多少行多少列酌情改变
    subplot(1,3,i);%第i个子图
    axChildren = get(fig(i),'Children');%获取绘制的图像
    copyobj(axChildren, gca);%复制到当前图窗里
    close(hf(i));%关掉已经复制的图像

    %下面是对图片进行设置，请酌情修改
    %title(['fig1-',num2str(i),'次测试']);%绘制子图标题
    %xlabel('Angle(\circ)');%绘制子图x标签
    %ylabel('Center WaveLength Change(nm)');%绘制子图y标签
    %yaxis([-0.05,0.2])%绘制子图y的范围
    %xticks([0 20 40 60 80 100]);%绘制子图刻度
end

%% verify the algorithmn two segment 

% for i=1:1
%     f0=[0;0;1;0;1.256637061435917;0;...
%         0;0;1;0;0;0;...
%         0;0;1;-0.628318530717959;1.088279618540531;0]
%     [H{i},~,p{i},f] = FK_n_segments_twist(f0,number_arc_interval,number_segments,disk_interval);
%     for j=1:number_segments
%         % the j th segment and the i th deformmation shape()t
%         arc{i,j}=p{i}(number_arc_interval_cumsum(j)+1:number_arc_interval_cumsum(j+1)+1,:);
%     end
%     
%     
% end

t=rand(30,1);
x=round(5*t+90)

%% visualization
% fig1=figure(1);
% fig_setting;
% 
% 
% for i=1:1
% %     hold on;
%     for j=1:number_segments
%         text=['plot3(arc{',num2str(i),',',num2str(j),...
%             '}(:,1),arc{',num2str(i),',',num2str(j),...
%             '}(:,2),arc{',num2str(i),',',num2str(j),'}(:,3));'];
%         eval(text);
%         hold on;
%     end
%     line_setting;
%     axes_setting;
%     drawnow();
%     pause(0.2)
%     generate_gif;
% end
% 
% label_setting;





