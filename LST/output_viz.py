"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Sat May 16 19:31:15 2020
**
"""
import rasterio
import matplotlib.pyplot as plt
import os
from NewFileLocation import newFilesLocation
from metadatainfo import metadataInformation

path = "C:/LEARNING(2020)/RESEARCH_WORK/data/LANDSAT/New_Study_Area/LC08_L1TP_190055_20200214_20200225_01_T1.tar.gz"

B10=newFilesLocation(path)[2]
SOLAR_ELEV=metadataInformation(path)[0]
B10_MULT=metadataInformation(path)[1]
B10_ADD=metadataInformation(path)[2]
B4_MULT=metadataInformation(path)[3]
B5_MULT=metadataInformation(path)[4]
B4_ADD=metadataInformation(path)[5]
B5_ADD=metadataInformation(path)[6]


