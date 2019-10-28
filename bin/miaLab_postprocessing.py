import os
import SimpleITK as sitk
import numpy as np
import miaLab_sliceViewer as sv
import matplotlib.pyplot as plt

directory = "mia-result\\2019-10-21-12-03-21"

for filename in os.listdir(directory):
    if filename.endswith("G.mha"):
        print(os.path.join(directory, filename))
        img = sitk.ReadImage(os.path.join(directory, filename))


        imgNew = sitk.Image(img)
        imgNew.CopyInformation(img)
        imgNew = imgNew * 0

        for labelIdx in range(1, 6):
            ccFilt = sitk.ConnectedComponentImageFilter()       # generate multiple labels
            ccImg = ccFilt.Execute(img == labelIdx)
            rFilt = sitk.RelabelComponentImageFilter()          # sort labels by size
            rImg = rFilt.Execute(ccImg)
            bImg = (rImg == 1) * labelIdx                       # Take biggest connected component
            imgNew = imgNew + bImg


        # - 0 (background)
        # - 1 (white matter)
        # - 2 (grey matter)
        # - 3 (Hippocampus)
        # - 4 (Amygdala)
        # - 5 (Thalamus)
        labelNames = ["background", "white matter", "grey matter", "hippocampus", "amygdala", "thalamus"]

        # BinaryThresholt(img, 4, 4 ,1 ,0) 4--> wished label, 1-->goal label, 0-->background
        #TODO: imagestatisticsfilter (for sorting labels)




        continue
    else:
        continue



