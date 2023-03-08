% hXLabel=xlabel('x (m)');
% hYLabel=ylabel('y (m)');
% hZLabel=zlabel('z (m)');
% set([hXLabel, hYLabel, hZLabel]  ,...
%     'FontSize'   , 12);
hXLabel=get(gca,'XLabel')
hYLabel=get(gca,'YLabel');
hZLabel=get(gca,'ZLabel');

set(hXLabel,        ...
    'String',      'X(m)',...
    'FontSize', 12);

% 'FontWeight','bold'

set(hYLabel,        ...
    'String',      'Y(m)',...
    'FontSize', 12);

set(hZLabel,        ...
    'String',      'Z(m)',...
    'FontSize', 12);