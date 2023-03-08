H0=eye(4);% initial homogenous matrix at s=0

% k1=4*pi/10:-pi/10:0;
k1=0:pi/10:6*pi/10;
k2=0:pi/10:6*pi/10;
k3=2*pi/10:pi/10:8*pi/10;
kappa=[k1',k2',k3'];% curvature of arc1 and arc2 m^{-1}


% tau=[0;0;0];% torsion m^{-1}
% tau=[pi/6;pi/6;pi/6];% torsion m^{-1}

% tau=[pi/2;pi/2;pi/2];% torsion m^{-1}
% tau=[pi;pi;pi];% torsion m^{-1}

tau=[0,0,0;...
    %pi/2,pi/2,pi/2;...
    pi,pi,pi];
% alpha=[0;pi/3;pi/6];
alpha=[4*pi/3;pi/3;pi/6];%the angle between bending plane and +X axis

number_arc_interval=[50;30;30];
number_arc_interval_cumsum=cumsum([0;number_arc_interval]);
number_segments=3;
disk_interval=0.01;

length_arc=number_arc_interval*disk_interval;% the length of each arc 
length_arc_cumsum=cumsum([[0;length_arc]]);

all_segments_number=number_segments*size(kappa,1);