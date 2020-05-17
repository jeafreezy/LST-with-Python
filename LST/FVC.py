"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Sun May 17 07:22:55 2020
**
"""
from NDVI import NDVI
from NDVI import NDVI_CLIP
import rasterio


path="C:/LEARNING(2020)/RESEARCH_WORK/data\LANDSAT/New_Study_Area/LC08_L1TP_190055_20200214_20200225_01_T1.tar.gz"
shp = "C:/LEARNING(2020)/RESEARCH_WORK/data/Study_area.shp"

print(NDVI(path))