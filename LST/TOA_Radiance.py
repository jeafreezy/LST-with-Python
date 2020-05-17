"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Thu May  7 09:31:48 2020
**
"""
from metadatainfo import metadataInformation
from NewFileLocation import newFilesLocation
import rasterio
import os
from clip import clip_bands

def topOfAtmRadiance(path):
    """
       |Formular= (((Lmax-Lmin)/QCALmax) * QCAL)+ Lmin
       |where: Lmin:spectral radiance at the minimum quantized and calibrated data digital number
       |Lmax= spectral radiance at the maximum quantized and calibrated data digital number
       |QCAL=Digital Number
       |QCALmax=255
       returns: Top of Radiance in the specified directory
    """

    values = metadataInformation(path)
    # format==B10_MULT,B10_ADD
    Mult = float(values[1])
    AL = float(values[2])

    Band_10 = newFilesLocation(path)[2]

    plot_dir = newFilesLocation(path)[4]

    new_directory = os.path.join(plot_dir, 'Analysis_Result')

    dir = os.path.join(plot_dir, 'Plots')

    try:

        band_10 = rasterio.open(Band_10)

        thermal = band_10.read(1).astype('float64')

        print('File is a raster file')
        print('*_' * 50)
        print('Running TOA Radiance Algorithm')

        if not os.path.exists(new_directory):

            os.mkdir(new_directory)

        output = os.path.join(new_directory, 'TOA_RADIANCE.tif')

        # running calculation
        output_raster_b10 = (Mult * thermal) + AL

        ToAImage = rasterio.open(output, 'w', driver='Gtiff',
                                  width=band_10.width,
                                  height=band_10.height,
                                  count=1, crs=band_10.crs,
                                  transform=band_10.transform,
                                  dtype='float64')

        ToAImage.write(output_raster_b10, 1)

        ToAImage.close()

        print('TOA RADIANCE COMPLETED!')


        #Would export plots later
        """# TOA PLOTS
        toa=rasterio.open(output)
        toa=toa.read(1).astype('float64')

        plt.figure(figsize=(12, 6))
        plt.title('TOA RADIANCE Band 10')
        plt.imshow(toa, cmap='Greys')
        plt.colorbar(labels='Values')
        plt.grid()
        #plt.imsave(os.path.join(dir, 'BAND_10_TOA_RADIANCE.jpg'),toa)"""

    except Exception as e:

        print('Error Message: ', e)

        raise e

    return output

#############################################################################
def topOfAtmRadiance_CLIP(path,shp):

    values = metadataInformation(path)
    # format==B10_MULT,B10_ADD
    Mult = float(values[1])
    AL = float(values[2])

    Band_10 =clip_bands(path,shp)[2]

    plot_dir = newFilesLocation(path)[4]

    new_directory = os.path.join(plot_dir, 'Analysis_Result')

    try:

        band_10 = rasterio.open(Band_10)

        thermal = band_10.read(1).astype('float64')

        print('File is a raster file')
        print('*_' * 50)
        print('Running TOA Radiance Algorithm')

        if not os.path.exists(new_directory):
            os.mkdir(new_directory)

        output = os.path.join(new_directory, 'TOA_RADIANCE.tif')

        # running calculation
        output_raster_b10 = (Mult * thermal) + AL

        ToAImage = rasterio.open(output, 'w', driver='Gtiff',
                                 width=band_10.width,
                                 height=band_10.height,
                                 count=1, crs=band_10.crs,
                                 transform=band_10.transform,
                                 dtype='float64')

        ToAImage.write(output_raster_b10, 1)

        ToAImage.close()

        print('TOA RADIANCE COMPLETED!')

    except Exception as e:

        print('Error Message: ', e)

        raise e

    return output