import os
import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

directory = "mia-result\\2019-10-21-12-03-21"

for filename in os.listdir(directory):
    if filename.endswith("G.mha"):
        print(os.path.join(directory, filename))
        img = sitk.ReadImage(os.path.join(directory, filename))

        ccfilt = sitk.ConnectedComponentImageFilter()
        ccImg = ccfilt.Execute(img)

        arrCC = np.transpose(sitk.GetArrayFromImage(ccImg), [2, 1, 0])

        continue
    else:
        continue



