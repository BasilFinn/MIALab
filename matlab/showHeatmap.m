clc; clear;
folder = [pwd '\heatmapData\'];
files = dir([folder '*.csv']);

lbl_list = {'WhiteMatter','GreyMatter','Hippocampus','Amygdala','Thalamus'};
lbl_nbr = 1;
for lbl = 1:length(lbl_list)
    for idx = 1:length(files)
        csv = files(idx);
        table = readtable([folder csv.name]);
        t_org= table(~contains(table.ID,'-PP'),:);
        t_org= t_org(contains(t_org.LABEL,lbl_list{lbl}),:);
        t_pp = table(contains(table.ID,'-PP'),:);
        t_pp = t_pp(contains(t_pp.LABEL,lbl_list{lbl}),:);
        
        % Fill table content
        diffHDRFDST(idx) = median(t_pp.HDRFDST)-median(t_org.HDRFDST);
%         diffHDRFDST(idx) = median(t_pp.DICE)-median(t_org.DICE);
        csvSize{idx}  = csv.name(9:10);
        csvDepth{idx} = csv.name(12:13);
        
    end
     c = [csvSize; csvDepth; num2cell(diffHDRFDST)]';
     T = cell2table(c);
    
    x = str2double(csvSize);
    y = str2double(csvDepth);
    z = diffHDRFDST;
    img = zeros(40);
    for i=1:length(x)
        img(x(i)-9:x(i), y(i)-9:y(i)) = z(i);
    end
    figure(lbl+100);
    imagesc(img);
    title(lbl_list{lbl});
    xlabel('Tree Size');
    ylabel('Tree Depth');
    cb = colorbar;
    title(cb,'HDRFDST')
%     title(cb,'DICE')
    
end