"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Sun May 17 07:15:19 2020
**
"""

import os
from DecompressAndExtract import extract

def newFilesLocation(path):
    """
    This function look through the new file and returns the paths
    """

    directory = extract(path)
    Band_4=''
    Band_5=''
    Band_10=''
    Metadata=''

    for root,dir,files in os.walk(directory):

        for name in files:

            if name.endswith("_B4.TIF"):

                Band_4 = os.path.join(root,name)

            elif name.endswith("_B5.TIF"):

                Band_5 = os.path.join(root, name)

            elif name.endswith("_B10.TIF"):

                Band_10 = os.path.join(root, name)

            elif name.endswith("_MTL.txt"):

                Metadata = os.path.join(root, name)

        return Band_4, Band_5, Band_10, Metadata, directory
