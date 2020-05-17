"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Sun May 17 07:15:59 2020
**
"""
import tarfile
import os



def decompressRequiredBands(members):
    """
    This function decompresses the needed bands(B1,B2,B3,B4 and metadata file) from the given compressed Landsat8 data

    """
    for tarinfo in members:

        if tarinfo.name.endswith(tuple(["_B4.TIF", "_B5.TIF", "_B10.TIF","_MTL.txt"])):
            yield tarinfo


def extract(path):
    """
    This function extracts the bands and save them in a new folder

    """
    print('Running..........Please wait for few more minutes...')

    tar = tarfile.open(path)

    # getting the parent directory i.e the directory where the compressed Landsat 8 file is

    parent_directory = os.path.dirname(path)

    # creating a new folder to story the extracted bands

    extraction_path = os.path.join(parent_directory, 'Extracted_Bands')

    if not os.path.exists(extraction_path):

        os.mkdir(extraction_path)

    tar.extractall(path=extraction_path, members=decompressRequiredBands(tar))

    tar.close()
    return extraction_path  # returning the file path so I could work with it in subsequent functions




