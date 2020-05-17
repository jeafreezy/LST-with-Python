"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Sat May 16 16:59:40 2020
**
"""
from NewFileLocation import newFilesLocation
def metadataInformation(path):
    """This function looks in the metadata file to extract the needed information"""

    metadata = newFilesLocation(path)[3]

    # The needed values for the LST Calculation

    #################### ***BAND 4*** #################
    REFLECTANCE_MULT_BAND_4 = "REFLECTANCE_MULT_BAND_4"
    REFLECTANCE_ADD_BAND_4 = "REFLECTANCE_ADD_BAND_4"

    #################### ***BAND 5*** #################
    REFLECTANCE_MULT_BAND_5 = "REFLECTANCE_MULT_BAND_5"
    REFLECTANCE_ADD_BAND_5 = "REFLECTANCE_ADD_BAND_5"

    #################### ***BAND 10*** #################
    RADIANCE_ADD_BAND_10 = "RADIANCE_ADD_BAND_10"
    RADIANCE_MULT_BAND_10 = "RADIANCE_MULT_BAND_10"
    # K1_CONSTANT_BAND_10 = "K1_CONSTANT_BAND_10"
    # K2_CONSTANT_BAND_10 = "K2_CONSTANT_BAND_10"


    #################### ***SOLAR ANGLE*** #################
    SUN_ELEVATION = "SUN_ELEVATION"

    values = []
    with open(metadata) as MT:

        for file in MT.readlines():

            # Band 4 values
            data=file.split('=')

            keys = data[0].strip()

            value=data[-1].strip()

            if keys == REFLECTANCE_MULT_BAND_4 :

                band_4_mult = value

                values.append(band_4_mult)

            elif keys ==  REFLECTANCE_ADD_BAND_4:

                band_4_add = value

                values.append(band_4_add)

            # band 5 values

            elif keys == REFLECTANCE_MULT_BAND_5 :

                band_5_mult = value

                values.append(band_5_mult)

            elif keys == REFLECTANCE_ADD_BAND_5:

                band_5_add = value

                values.append(band_5_add)

            # band 10 values

            elif keys ==  RADIANCE_MULT_BAND_10:

                band_10_mult = value

                values.append(band_10_mult)

            elif keys ==  RADIANCE_ADD_BAND_10 :

                band_10_add = value

                values.append(band_10_add)


            elif keys ==  SUN_ELEVATION :

                sun_elev = value

                values.append(sun_elev)

        #format== SOLAR_ELEV,B10_MULT,B10_ADD,B4_MULT,B5_MULT,B4_ADD,B5_ADD

        return values
