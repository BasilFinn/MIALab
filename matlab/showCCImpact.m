clc; clear;
folder = [pwd '\ccImpactData\'];
files = dir([folder '*.csv']);

lbl_list = {'WhiteMatter','GreyMatter','Hippocampus','Amygdala','Thalamus'};
for lbl_idx = 1:length(lbl_list)
    bp_data = [];
    bp_noCC = [];
    for idx = 1:length(files)
        csv = files(idx);
        table = readtable([folder csv.name]);
%         t_org= table(~contains(table.ID,'-PP'),:);
%         t_org= t_org(contains(t_org.LABEL,lbl_list{lbl}),:);
        t_pp = table(contains(table.ID,'-PP'),:);
        t_pp = t_pp(contains(t_pp.LABEL,lbl_list{lbl_idx}),:);
        
        % Fill table content
        bp_data(:,idx) = t_pp.HDRFDST;
        bp_noCC{idx} = csv.name(12:end-4);

        diffHDRFDST(idx) = median(t_pp.HDRFDST);
        noCC(idx) = str2double(csv.name(12:13));       
    end
    
    % Append no PP data
    t_org= table(~contains(table.ID,'-PP'),:);
    t_org= t_org(contains(t_org.LABEL,lbl_list{lbl_idx}),:);
    bp_data(:,size(bp_data,2)+1) = t_org.HDRFDST;
    bp_noCC{size(bp_noCC,2)+1} = 'all';
   

    figure(lbl_idx);
    boxplot(bp_data,bp_noCC)
    title(lbl_list{lbl_idx});
    xlabel('Number connected components');
    ylabel('HDRFDST');

%     figure(1);
%     plot(noCC,diffHDRFDST,'o-'); hold on;
%        
end
%     xlabel('Number connected components');
%     ylabel('HDRFDST');  
%     legend(lbl_list);