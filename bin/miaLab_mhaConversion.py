import os
import SimpleITK as sitk
import numpy as np
import miaLab_sliceViewer as sv
import matplotlib.pyplot as plt

directory = "mia-result\\2019-12-09-13-00-39_CC_replace"

for filename in os.listdir(directory):
    if filename.endswith("117122_SEG.mha"):
        print(os.path.join(directory, filename))
        imgBad = sitk.ReadImage(os.path.join(directory, filename))
        imgNoPP = sitk.ReadImage(os.path.join(directory, filename[0:10] + '.mha'))

        sitk.WriteImage(imgBad, os.path.join(directory, filename + '_test.mha'), True)




        continue
    else:
        continue



