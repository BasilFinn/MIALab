import os
import sys
import SimpleITK as sitk
import numpy as np
import miaLab_sliceViewer as sv
import matplotlib.pyplot as plt

# load  atlas
# atlas = sitk.Image()
atlas = sitk.ReadImage(os.path.normpath(os.path.join(os.path.dirname(sys.argv[0]),
                                                     '../data/atlas/additional/atlas_label.nii.gz')))

directory = "mia-result\\2019-11-04-11-17-42"
# TODO: confusion matrix to compare predtictions with ground truth
# TODO: usefullness of postprocessing when improved segmentation
for filename in os.listdir(directory):
    if filename.endswith("G.mha"):
        print(os.path.join(directory, filename))
        img = sitk.ReadImage(os.path.join(directory, filename))

        imgNew = sitk.Image(img)
        imgNew.CopyInformation(img)
        imgNew = imgNew * 0

        componentList = [1, 1, 2, 1, 1]

        for labelIdx in range(1, 6):
            ccFilt = sitk.ConnectedComponentImageFilter()       # generate multiple labels
            ccImg = ccFilt.Execute(img == labelIdx)
            rFilt = sitk.RelabelComponentImageFilter()          # sort labels by size
            rImg = rFilt.Execute(ccImg)

            for i in range(0, componentList[labelIdx-1]):       # take n biggest components
                print(i+1)
                bImg = (rImg == i+1) * labelIdx
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



