"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Sat May 16 12:55:41 2020
**
"""
import rasterio


class LST:

    # Instruction on how to use
    print \
            (
            """
                ######################## * INSTRUCTIONS, READ CAREFULLY * #######################################
                ###########################################################################################
                |This tool calculates the Top of Atmosphere Radiance for a Landsat 8 band using the formular
                |(((Lmax-Lmin)/QCALmax) * QCAL)+ Lmin
                |where: Lmin:spectral radiance at the minimum quantized and calibrated data digital number for band
                |Lmax= spectral radiance at the maximum quantized and calibrated data digital number for band
                |QCAL=Digital Number
                |QCALmax=255
                |See how to run below in the Command Line->
                |python3 TOA_Radiance.py <path to landsat band> <Lmax> <Lmin>|
                |python TOA_Radiance.py <path to landsat band> <Lmax> <Lmin> |
                ############################################################################################
            """
        )

        # importing required modules

        import arcpy

        # import os
        # import sys

        # setting workspace

        arcpy.env.workspace = "C:/LEARNING(2020)/RESEARCH_WORK/Codes/An-Improved-Methodology-for-Locating-and-Ranking-Public-Landfill-Sites-at-a-Regional-Scale/LST/Analysis_Outputs"
        # overwriting existing output file

        arcpy.env.overwriteOutput = True


        # Checking if the Spatial Analyst tool is available

        if arcpy.CheckOutExtension('Spatial'):

            print('Spatial Analysts is available')

        else:

            print('Can\'t find Arcpy module \n Ensure you are running script with ArcGIS python interpreter or \n'
                  'you are running script in ArcGIS environment')

        # Main function

        def top_of_atm(landsat_band, l_max, l_min, output):

            """
            |parameters: Landsat band,l_max,lmin,output directory
            |Formular= (((Lmax-Lmin)/QCALmax) * QCAL)+ Lmin
            |where: Lmin:spectral radiance at the minimum quantized and calibrated data digital number
            |Lmax= spectral radiance at the maximum quantized and calibrated data digital number
            |QCAL=Digital Number
            |QCALmax=255
            returns: Top of Radiance in the specified directory

            """
            try:

                if arcpy.Exists(landsat_band):

                    print('File is a raster file')
                    print('*_' * 50)
                    print('Running algorithm')

                    try:
                        # creating a raster object
                        band_raster = arcpy.Raster(landsat_band)

                        # running calculation

                        output_raster = (((l_max - l_min) / 255) * band_raster) + l_min

                        # saving outputfile in the workspace

                        output_raster.save(output)

                        # deleting raster object

                        del (output_raster)

                    except RuntimeError as f:

                        raise f

            except RuntimeError as e:

                print('Error Message: ', e)

                raise e

        band = "C:/LEARNING(2020)/RESEARCH_WORK/data/LANDSAT/New_Study_Area/LC08_L1TP_190055_20200214_20200225_01_T1_B4.TIF"

        output = 'B4_TOA_Radiance.TIF'

        lmax = 620.32391

        lmin = -51.22655
        # top_of_atm(band, lmax, lmin, output)

        print('Completed')

        arcpy.AddMessage('Completed!')

        # import geopandas as gpd

        import rasterio
