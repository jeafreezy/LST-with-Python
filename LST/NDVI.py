"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Sun May 17 07:21:21 2020
**
"""
from NewFileLocation import newFilesLocation
from clip import clip_bands
import os
import rasterio
from rasterio import plot
import numpy as np
import matplotlib.pyplot as plt
from TOA_Reflectance import topOfAtmReflectance


def NDVI(path):

    """This function calculates NDVI for the Landsat8 data"""

    #red bands
    Band_4_path =topOfAtmReflectance(path)[0]
    #NIR bands
    Band_5_path =topOfAtmReflectance(path)[1]

    band_4 = rasterio.open(Band_4_path)
    band_5 = rasterio.open(Band_5_path)

    plot_dir=newFilesLocation(path)[4]

    dir=os.path.join(plot_dir,'Plots')

    #CREATING DIRECTORY FOR PLOTS

    if not os.path.exists(dir):

        os.mkdir(dir)

    # NDVI CODE BLOCK
    # generate nir and red objects as arrays in float64 format
    red = band_4.read(1).astype('float64')
    nir = band_5.read(1).astype('float64')

    new_directory = os.path.join(plot_dir, 'Analysis_Result')

    if not os.path.exists(new_directory):

        os.mkdir(new_directory)

    output=os.path.join(new_directory,'NDVI.tif')

    # ndvi calculation, empty cells or nodata cells are reported as 0

    ndvi = np.where(
        (nir + red) == 0.,
        0,
        (nir - red) / (nir + red))

    ndviImage = rasterio.open(output, 'w', driver = 'Gtiff',
                                              width = band_4.width,
                                                      height = band_4.height,
                                                               count = 1, crs = band_4.crs,
                                                                                transform = band_4.transform,
                                                                                          dtype = 'float64')
    ndviImage.write(ndvi, 1)

    ndviImage.close()

    return new_directory , output


######################################################################################

def NDVI_CLIP(path,shp):

    Band_4=topOfAtmReflectance(clip_bands(path,shp)[0])[0]
    Band_5=topOfAtmReflectance(clip_bands(path,shp)[1])[1]
    band_4 = rasterio.open(Band_4)
    band_5 = rasterio.open(Band_5)

    plot_dir=newFilesLocation(path)[4]

    dir=os.path.join(plot_dir,'Plots_clipped')

    #CREATING DIRECTORY FOR PLOTS

    if not os.path.exists(dir):

        os.mkdir(dir)

    # NDVI CODE BLOCK
    # generate nir and red objects as arrays in float64 format
    red = band_4.read(1).astype('float64')
    nir = band_5.read(1).astype('float64')

    new_directory = os.path.join(plot_dir, 'Analysis_Result_Clipped')

    if not os.path.exists(new_directory):

        os.mkdir(new_directory)

    output=os.path.join(new_directory,'NDVI.tif')

    # ndvi calculation, empty cells or nodata cells are reported as 0

    ndvi = np.where(
        (nir + red) == 0.,
        0,
        (nir - red) / (nir + red))

    ndviImage = rasterio.open(output, 'w', driver = 'Gtiff',
                                              width = band_4.width,
                                                      height = band_4.height,
                                                               count = 1, crs = band_4.crs,
                                                                                transform = band_4.transform,
                                                                                          dtype = 'float64')
    ndviImage.write(ndvi, 1)

    ndviImage.close()

    return new_directory , output
