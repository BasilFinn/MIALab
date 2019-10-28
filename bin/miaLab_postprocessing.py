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

        ccFilt = sitk.ConnectedComponentImageFilter()
        ccImg = ccFilt.Execute(img)
        arrCC = np.transpose(sitk.GetArrayFromImage(ccImg), [2, 1, 0])

        sFilt = sitk.LabelStatisticsImageFilter()
        sFilt.Execute(img, ccFilt)

        # - 0 (background)
        # - 1 (white matter)
        # - 2 (grey matter)
        # - 3 (Hippocampus)
        # - 4 (Amygdala)
        # - 5 (Thalamus)
        labelNames = ["background", "white matter", "grey matter", "hippocampus", "amygdala", "thalamus"]

        #TODO: imagestatisticsfilter (for sorting labels)
        #TODO: Make loop for all labels
        for idx in range(3, 6):
            imgHy = (img == idx)
            ccFiltHy = sitk.ConnectedComponentImageFilter()
            ccFiltHy.Execute(imgHy)
            print(labelNames[idx])
            print(ccFiltHy.GetObjectCount())



        continue
    else:
        continue



