clc; clear;
folder = [pwd '\comparisonData\'];
files = dir([folder '*.csv']);

lbl_list = {'WhiteMatter','GreyMatter','Hippocampus','Amygdala','Thalamus'};
for lbl_idx = 1:length(lbl_list)
    data = [];
    for fileIdx = 1:length(files)
        csv = files(fileIdx);
        table = readtable([folder csv.name]);
%         t_org= table(~contains(table.ID,'-PP'),:);
%         t_org= t_org(contains(t_org.LABEL,lbl_list{lbl}),:);
        t_pp = table(contains(table.ID,'-PP'),:);
        t_pp = t_pp(contains(t_pp.LABEL,lbl_list{lbl_idx}),:);
        
        % Fill table content
        data(:,fileIdx) = t_pp.HDRFDST;
        noCC{fileIdx} = csv.name(9:end-4);
        
    end

    figure(lbl_idx);
    boxplot(data,noCC);
    title(lbl_list{lbl_idx});
    xlabel('Processing type');
    ylabel('HDRFDST');
       
end