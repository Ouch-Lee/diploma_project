linewidth=5;
color={'#D9541A','#EDB021','#0073BD','#3E2B6D','#EF6F6C','#9999CC','#FF9090'};
% set(ax1,                ...
%     'LineStyle',    '-',...
%     'Color',        '#9999CC',...
%     'LineWidth',    5);
% set(ax2,                ...
%     'LineStyle',    '-',...
%     'Color',        '#FF9090',...
%     'LineWidth',    5);


ax=get(gca,'Children');
k=1;
t=1;
for j=1:number_segments
    set(ax(j),'LineStyle','-');
    set(ax(j),'LineWidth',5);
    set(ax(j),'Color',color{t});
    k=k+1;

    t=mod(k,number_segments);
    if t==0
        t=number_segments;
    end
    
end



