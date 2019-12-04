import os
import SimpleITK as sitk
import numpy as np
import miaLab_sliceViewer as sv
import matplotlib.pyplot as plt

directory = "mia-result\\2019-10-21-12-03-21"
directory_probability = "mia-result\\probabilities"

for filename in os.listdir(directory):
    if filename.endswith("SEG.mha"):
        # get corresponding probability file
        for f in os.listdir(directory_probability):
            if f.startswith(filename[0:6]):
                filename_probability = f


        print(os.path.join(directory_probability, filename_probability))
        probability = sitk.ReadImage(os.path.join(directory_probability, filename_probability))
        print(os.path.join(directory, filename))
        img = sitk.ReadImage(os.path.join(directory, filename))

        p = sitk.GetArrayFromImage(probability)
        i = sitk.GetArrayFromImage(img)

        # Delete 1st maximum
        for x in range(p.shape[0]):
            for y in range(p.shape[1]):
                for z in range(p.shape[2]):
                    idx = i[x, y, z]
                    p[x, y, z, idx] = 0

        # Select new maximum in probability
        p2 = np.argmax(p, axis=-1)
        img2 = sitk.GetImageFromArray(p2)


        imgNew = sitk.Image(img)
        imgNew.CopyInformation(img)
        imgNew = imgNew * 0

        componentList = [1, 1, 2, 1, 1]

        for labelIdx in range(1, 6):
            ccFilt = sitk.ConnectedComponentImageFilter()       # generate labels for all cc within anatomy label
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



