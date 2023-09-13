# updated: 23-08-2023
#XARRAY - biblioteka
# error:      @ToDo
#   File "C:\Users\pbednarczyk\Pawel_Bednarczyk_materialy\matlab_python\_Python_projekty\venv\Lib\site-packages\gribapi\gribapi.py", line 2228, in <module>
#     __version__ = grib_get_api_version()
#                   ^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\pbednarczyk\Pawel_Bednarczyk_materialy\matlab_python\_Python_projekty\venv\Lib\site-packages\gribapi\gribapi.py", line 2218, in grib_get_api_version
#     raise RuntimeError("Could not load the ecCodes library!")
# RuntimeError: Could not load the ecCodes library!
# ###########################################################################################

import numpy as np
import pandas as pd
import xarray as xr
import eccodes
import pyeccodes

import matplotlib.pyplot as plt

#path: str = 'C:/Users/pbednarczyk/Pawel_Bednarczyk_materialy/Copernicus/'
#fname: str = 'download.grib'
#ds = xr.open_dataset(path+fname,engine='cfgrib', backend_kwargs={'indexpath': ''})

ds = xr.tutorial.load_dataset("download.grib", enigne="cfgrib")
#ds = ds
print(ds)
