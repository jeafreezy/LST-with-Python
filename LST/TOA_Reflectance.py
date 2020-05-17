"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Thu May  7 21:52:55 2020
**
"""
from metadatainfo import metadataInformation
from NewFileLocation import newFilesLocation
from clip import clip_bands
import rasterio
import os
import math


def topOfAtmReflectance(path):
    """
       |Formular= (((Lmax-Lmin)/QCALmax) * QCAL)+ Lmin
       |where: Lmin:spectral radiance at the minimum quantized and calibrated data digital number
       |Lmax= spectral radiance at the maximum quantized and calibrated data digital number
       |QCAL=Digital Number
       |QCALmax=255
       returns: Top of Radiance in the specified directory
    """

    values = metadataInformation(path)
    Sun_Elev = float(values[0])
    B4_Mult = float(values[3])
    B5_Mult = float(values[4])
    B4_Add = float(values[5])
    B5_Add = float(values[6])

    Band_4 = newFilesLocation(path)[0]
    Band_5 = newFilesLocation(path)[1]
    plot_dir = newFilesLocation(path)[4]

    new_directory = os.path.join(plot_dir, 'Analysis_Result')

    try:

        band_4 = rasterio.open(Band_4)
        band_5 = rasterio.open(Band_5)

        b4 = band_4.read(1).astype('float64')
        b5 = band_5.read(1).astype('float64')

        print('File is a raster file')
        print('*_' * 50)
        print('Running TOA Radiance Algorithm')

        if not os.path.exists(new_directory):
            os.mkdir(new_directory)

        output_b4 = os.path.join(new_directory, 'B4_TOA_REFLECTANCE.tif')
        output_b5 = os.path.join(new_directory, 'B5_TOA_REFLECTANCE.tif')

        # running calculation
        output_b4_calc = ((B4_Mult * b4) + B4_Add) / math.sin(Sun_Elev)
        output_b5_calc = ((B5_Mult * b5) + B5_Add) / math.sin(Sun_Elev)

        ToAImage_4 = rasterio.open(output_b4, 'w', driver='Gtiff',
                                   width=band_4.width,
                                   height=band_4.height,
                                   count=1, crs=band_4.crs,
                                   transform=band_4.transform,
                                   dtype='float64')
        ToAImage_5 = rasterio.open(output_b5, 'w', driver='Gtiff',
                                   width=band_5.width,
                                   height=band_5.height,
                                   count=1, crs=band_5.crs,
                                   transform=band_5.transform,
                                   dtype='float64')

        ToAImage_4.write(output_b4_calc, 1)
        ToAImage_5.write(output_b5_calc, 1)
        ToAImage_4.close()
        ToAImage_5.close()

        print('TOA REFLECTANCE COMPLETED!')

    except Exception as e:

        print('Error Message: ', e)

        raise e

    return output_b4, output_b5


def topOfAtmReflectance_CLIP(path,shp):

    values = metadataInformation(path)
    Band_4 =clip_bands(path,shp)[0]
    Band_5 = clip_bands(path, shp)[1]


    Sun_Elev = float(values[0])
    B4_Mult = float(values[3])
    B5_Mult = float(values[4])
    B4_Add = float(values[5])
    B5_Add = float(values[6])

    plot_dir = newFilesLocation(path)[4]
    new_directory = os.path.join(plot_dir, 'Analysis_Result')

    try:

        band_4 = rasterio.open(Band_4)
        band_5 = rasterio.open(Band_5)

        b4 = band_4.read(1).astype('float64')
        b5 = band_5.read(1).astype('float64')

        print('File is a raster file')
        print('*_' * 50)
        print('Running TOA Radiance Algorithm')

        if not os.path.exists(new_directory):
            os.mkdir(new_directory)

        output_b4 = os.path.join(new_directory, 'B4_TOA_REFLECTANCE.tif')
        output_b5 = os.path.join(new_directory, 'B5_TOA_REFLECTANCE.tif')

        # running calculation
        output_b4_calc = ((B4_Mult * b4) + B4_Add) / math.sin(Sun_Elev)
        output_b5_calc = ((B5_Mult * b5) + B5_Add) / math.sin(Sun_Elev)

        ToAImage_4 = rasterio.open(output_b4, 'w', driver='Gtiff',
                                   width=band_4.width,
                                   height=band_4.height,
                                   count=1, crs=band_4.crs,
                                   transform=band_4.transform,
                                   dtype='float64')
        ToAImage_5 = rasterio.open(output_b5, 'w', driver='Gtiff',
                                   width=band_5.width,
                                   height=band_5.height,
                                   count=1, crs=band_5.crs,
                                   transform=band_5.transform,
                                   dtype='float64')

        ToAImage_4.write(output_b4_calc, 1)
        ToAImage_5.write(output_b5_calc, 1)
        ToAImage_4.close()
        ToAImage_5.close()

        print('TOA REFLECTANCE COMPLETED!')

    except Exception as e:

        print('Error Message: ', e)

        raise e

    return output_b4, output_b5
