clc; clear;
folder = [pwd '\ccImpactData\'];
files = dir([folder '*.csv']);

lbl_list = {'WhiteMatter','GreyMatter','Hippocampus','Amygdala','Thalamus'};
for lbl_idx = 1:length(lbl_list)
    for idx = 1:length(files)
        csv = files(idx);
        table = readtable([folder csv.name]);
%         t_org= table(~contains(table.ID,'-PP'),:);
%         t_org= t_org(contains(t_org.LABEL,lbl_list{lbl}),:);
        t_pp = table(contains(table.ID,'-PP'),:);
        t_pp = t_pp(contains(t_pp.LABEL,lbl_list{lbl_idx}),:);
        
        % Fill table content
        diffHDRFDST(idx) = median(t_pp.HDRFDST);
        noCC(idx) = str2double(csv.name(12:13));
        
    end
   
% 
%     figure(lbl_idx);
%     plot(noCC,diffHDRFDST,'o-');
%     title(lbl_list{lbl_idx});
%     xlabel('Number connected components');
%     ylabel('HDRFDST');
    figure(1);
    plot(noCC,diffHDRFDST,'o-'); hold on;
       
end
    xlabel('Number connected components');
    ylabel('HDRFDST');  
    legend(lbl_list);