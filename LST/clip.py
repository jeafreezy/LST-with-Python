"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Sun May 17 11:30:19 2020
**
"""
import gdal
from NewFileLocation import newFilesLocation
from metadatainfo import metadataInformation
import os


def clip_bands(path, shp):

    """This function clips a portion from a landsat"""

    shapefile = shp

    directory = newFilesLocation(path)[4]

    band_list = [band for band in os.listdir(directory) if band[-4:]=='.TIF']

    clip_dir = os.path.join(directory, 'Clipped_files')

    if not os.path.exists(clip_dir):

        os.mkdir(clip_dir)

        print(f'Clipped Bands can be found here: {clip_dir}')

         # CLIPPING BLOCK

        for band in band_list:

            options=gdal.WarpOptions(cutlineDSName=shp,cropToCutline=True)

            outBand=gdal.Warp(srcDSOrSrcDSTab=os.path.join(directory,band),overwrite=True, destNameOrDestDS=os.path.join(clip_dir,band[:-4]+'_Clipped'+band[-4:]),options=options)

            outBand=None


    else:
            #For development purpose...

        if os.listdir(clip_dir):

            pass

        else:

            for band in band_list:

                options = gdal.WarpOptions(cutlineDSName=shp, cropToCutline=True)

                outBand = gdal.Warp(srcDSOrSrcDSTab=os.path.join(directory,band),overwrite=True, destNameOrDestDS=os.path.join(clip_dir,band[:-4]+'_Clipped'+band[-4:]), options=options)

                outBand = None


    # CLIPPED DIRECTORY

    Band_4_clip = os.path.join(clip_dir, os.listdir(clip_dir)[1])
    Band_5_clip = os.path.join(clip_dir, os.listdir(clip_dir)[2])
    Band_10_clip = os.path.join(clip_dir, os.listdir(clip_dir)[0])

    return Band_4_clip, Band_5_clip, Band_10_clip



