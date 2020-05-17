"""
**
 * author :   	Emmanuel Jolaiya
 * created : 	Sat May 16 20:01:17 2020
**
"""
from output_viz import NDVI
from output_viz import TOA
from output_viz import TOR
from output_viz import FVC
from output_viz import emmissivity
from output_viz import LSEN


def lst(path):

    print('Currently computing NDVI...')

    step1=NDVI(path)

    print('Currently computing Top of Atmosphere Radiance for Band 10...')

    step2=TOA(step1)

    print('Currently computing Top of Atmosphere Reflectance for Band 4 and 5')

    step3=TOR(step2)

    print('Currently computing Fractional Vegetation Cover (FVC)')

    step4=FVC(step3)

    print('Currently computing the Emmissivity...')

    step5=emmissivity(step4)

    print('Currently computing the Thermal Radiance at Sensor Level File')

    step6=LSEN(step5)

    print('Currently computing the LST....Almost done')

    lst=LST(step6)

  return f'Completed! Check {} for the analysis results!'


