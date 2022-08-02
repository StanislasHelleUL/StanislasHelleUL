# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:26:34 2022

@author: Stanislas.Helle
"""

import matplotlib
matplotlib.use('Qt5Agg')


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from DictioProt import adductPosDict


class MplPeakMassifCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100, dataSet=((0,0),),
                 accession = "None", charge = 1, adduct = "Proton", modification = "None"):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        x = [dataSet[x][0] for x in range(len(dataSet))]
        y = [dataSet[x][1] for x in range(len(dataSet))]
        
        massif_area = 0
        for i in range(len(y)-1):
            area = y[i]/charge + (y[i+1]-y[i])\
                /(2*charge)
            massif_area += area
        
        self.axes.plot(x,y)
        self.axes.bar(x, y, width = len(x)/(100*charge));
        self.axes.set(xlim=(min(x)-0.5, max(x)+0.5),
               ylim=(0, max(y) + max(y)/10))
        self.axes.set_xlabel('m/z')
        self.axes.set_ylabel('Relative Abundance')
        
        for mz,intensity in zip(x,y):

            label = "{:.3f}".format(mz)
        
            self.axes.annotate(label, # this is the text
                         (mz,intensity), # these are the coordinates to position the label
                         textcoords="offset points", # how to position the text
                         xytext=(0,10), # distance from text to points (x,y)
                         ha='center') 

        indexAdduct = adductPosDict['Name'].index(f'{adduct}')
        adductCode = adductPosDict['Code'][indexAdduct]
        self.axes.set_title(f'{accession}:\nArea = {massif_area}\nCharge = {charge}; Adduct = {adductCode};\nmodification = {modification}')
        super(MplPeakMassifCanvas, self).__init__(fig)

        