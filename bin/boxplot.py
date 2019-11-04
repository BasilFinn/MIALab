import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd


def main():
    # todo: load the "results.csv" file from the mia-results directory
    # todo: read the data into a list
    # todo: plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus) in a boxplot

    # data = list()
    #
    # with open('mia-results/results.csv', newline='') as csvfile:
    #     f = csv.reader(csvfile, delimiter=';')
    #     for i, row in enumerate(f, start=1):
    #         # print(row)
    #         data.append(row)  # list(map(int, row))
    #
    # print(data)

    # alternative: instead of manually loading/reading the csv file you could also use the pandas package
    # but you will need to install it first ('pip install pandas') and import it to this file ('import pandas as pd')

    data_org = pd.read_csv('mia-result/2019-11-04-11-17-42/results.csv', delimiter=';')  # , dtype={'ID': int, 'LABEL': str, 'DICE': float, 'HDRFDST': float}
    data   = data_org.loc[data_org['ID'].str.contains('-PP')==False]
    dataPP = data_org.loc[data_org['ID'].str.contains('-PP')]
    dataPP['LABEL'] = dataPP['LABEL'] + "-PP"

    result = pd.concat([data, dataPP])

    plt.figure(1)
    result.boxplot(by='LABEL', column='DICE')

    plt.figure(2)
    result.boxplot(by='LABEL', column='HDRFDST')

    # data.boxplot(by='LABEL', column='DICE')
    # dataPP.boxplot(by='LABEL', column='DICE')
    plt.show()

    # pass  # pass is just a placeholder if there is no other code


if __name__ == '__main__':
    main()
