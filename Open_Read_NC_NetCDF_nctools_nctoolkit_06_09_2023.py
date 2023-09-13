# import nctoolkit as nc
#
# # https://nctoolkit.readthedocs.io/en/v0.1.2/basic_usage.html
# nc.deep_clean()
#
# # file = "mean_Tmax_Yearly_rcp85_mean_v1_0_pobr_05_09_2023.nc"
# file = "tas_Amon_GFDL_CM3_rcp85_r1i1p1_203601_204012__06092023.nc"
# sst = nc.open_data(file)
# ############

#########################################################2##########06-09-2023########
# from scipy.io import netcdf
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import wx
print(f"nc variables: %nc.varaibles")

import wxpython
# # file2read = netcdf.NetCDFFile(path+'state.nc','r')
# file2read = netcdf.NetCDFFile("tas_Amon_GFDL_CM3_rcp85_r1i1p1_203601_204012__06092023.nc",'r')
# temp = file2read.variables # ["temp"]  # var can be 'Theta', 'S', 'V', 'U' etc..
# data = temp[:]*1
# file2read.close()
#

#######################06-09-2023--readNC-FILE------------------
#----otwarcie NC dziala
#https://stackoverflow.com/questions/36360469/read-nc-netcdf-files-using-python
import numpy as np
# @ToDo -> nie dziala import ???!? from matplotlib import pyplot as plt  # import libraries
import pandas as pd # import libraries
import netCDF4  # import libraries
# pobrane za pomoca skryptu proba_CDS_API_dziala
path="C:/Users/pbednarczyk/Pawel_Bednarczyk_materialy/Copernicus/_wykresy_Copernicus_25_08_2023_MagdalenaSkrzynska/Copernicus_Projekt_pythona_skrypty/"
fp='tas_Amon_GFDL_CM3_rcp85_r1i1p1_203601_204012__06092023.nc'  # your file name with the eventual path
nc = netCDF4.Dataset(path+fp)  # reading the nc file and creating Dataset
print(f"nc variables: ")
print(nc.variables)
#variables:
# variables(dimensions): float64 time(time), float64 time_bnds(time, bnds),
# float64 lat(lat), float64 lat_bnds(lat, bnds), float64 lon(lon), float64 lon_bnds(lon, bnds),
# float32 tas(time, lat, lon),
# float64 average_T1(time), float64 average_T2(time), float64 average_DT(time), float64 height()
#""" in this dataset each component will be
#in the form nt,nz,ny,nx i.e. all the variables will be flipped. """
nc['tas'][:,50.2833,18.6667]
# masked_array(data=[295.44135, 296.40857, 299.65735, 302.96606, 302.8963 ,
#                    306.8042 , 307.56192, 307.51297, 303.18338, 301.00015,
#                    298.38208, 296.7257 , 295.38913, 296.0968 , 299.1506 ,
#                    302.36362, 303.98383, 305.0583 , 306.8537 , 307.42245,
#                    305.47177, 301.03848, 298.6607 , 296.36163, 295.20428,
#                    295.5032 , 297.84067, 302.523  , 305.2307 , 307.13797,
#                    306.9875 , 307.09857, 304.09607, 299.91922, 298.05954,
#                    296.7654 , 295.3365 , 296.03598, 296.6418 , 301.8733 ,
#                    304.32108, 305.98404, 306.26508, 305.2007 , 302.22708,
#                    300.1741 , 298.5928 , 296.4701 , 295.2346 , 295.2989 ,
#                    299.30316, 300.59372, 303.89026, 306.2088 , 306.64954,
#                    305.83176, 303.18768, 301.9168 , 299.20502, 297.31216],
#              mask=False,
#        fill_value=1e+20,
#             dtype=float32)



# @ToDo
#plt.plot([1,2,3,4],[25,23,24,20])
#plt.plot(nc['air_temperature'])
#plt.show()

#plt.imshow(nc['air_temperature'])
# """ imshow is a 2D plot function
# according to what I have said before this will plot the second
# iteration of the vertical slize with y = 0, one of the vertical
# boundaries of your model. """
# plt.show() # this shows the plot
