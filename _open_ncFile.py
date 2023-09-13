import netCDF4
from netCDF4 import Dataset
from netCDF4 import MFDataset
from netCDF4 import MFTime, num2date, date2num, date2index
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt



#########tree navigation###############################
def walktree(top_input):
    # method - rekurencja ?
    yield top_input.groups.values()
    for value in top_input.groups.values():
        yield from walktree(value)
######################################################


# f = Dataset('caafc139-0722-45a8-8936-afe48a56092a_28_08_2023.nc')
# ########### .nc file is opening
# 'p1_Tmax_Summer_rcp85_mean_v1.0.nc'
# 'mean_Tmax_Summer_rcp85_stdev_v1.0.nc'
# 'p1_Tmax_Summer_rcp85_mean_v1.0.nc'
# caafc139-0722-45a8-8936-afe48a56092a_28_08_2023
# f_root_grp = Dataset('caafc139-0722-45a8-8936-afe48a56092a_28_08_2023.nc', mode='w', format='NETCDF4')

# mean_Tmax_Yearly_rcp85_meanv1.0409203.nc  # 04092023
# mean_Tmax_Yearly_rcp85_mean_v1.0_04092023_1338 # 04092023 1338
# f_root_grp = Dataset('mean_Tmax_Yearly_rcp85_stdev_v1.0_04092023_1338.nc', mode='r', format='HDF5')

# 05-09-2023
f_root_grp = Dataset('/dataset-sis-temperature-statistics_05_09_2023/mean_Tmax_Yearly_rcp85_mean_v1.0.nc', mode='r')


print(f_root_grp.data_model)

##############################
# Groups in a netCDF file  -------!!!! I can not --->
#   File "<input>", line 6, in <module>
#   File "src\netCDF4\_netCDF4.pyx", line 2464, in netCDF4._netCDF4.Dataset.__init__
#   File "src\netCDF4\_netCDF4.pyx", line 2027, in netCDF4._netCDF4._ensure_nc_success
# PermissionError: [Errno 13] Permission denied: 'p1_Tmax_Summer_rcp85_mean_v1.0.nc' -->read only
f_root_grp = Dataset("p1_Tmax_Summer_rcp85_mean_v1.0.nc","a")
fcst_grp = f_root_grp.createGroup("forecasts")
anal_grp = f_root_grp.createGroup("analyses")
print(f_root_grp.groups)

# Groups can exist within groups in a Dataset, just as directories exist within directories in
# a unix filesystem. Each Group instance has a groups attribute dictionary containing
# all of the group instances contained within that group. Each Group instance also has a path
# attribute that contains a simulated unix directory path to that group. To simplify the creation of nested
# groups, you can use a unix-like path as an argument to Dataset.createGroup().

fcst_grp1 = f_root_grp.createGroup("/forecast/model1")
fcst_grp2 = f_root_grp.createGroup("/forecast/model2")

# -----------------------------------------------------------
# result:
# {'forecasts': <class 'netCDF4._netCDF4.Group'>
# group /forecasts:
#     dimensions(sizes):
#     variables(dimensions):
#     groups: , 'analyses': <class 'netCDF4._netCDF4.Group'>
# group /analyses:
#     dimensions(sizes):
#     variables(dimensions):
#     groups: }
###################################
# PermissionError: [Errno 13] Permission denied: 'p1_Tmax_Summer_rcp85_mean_v1.0.nc'
# resolution: computer restart
####################################
# <class 'netCDF4._netCDF4.Dataset'>
# root group (NETCDF4 data model, file format HDF5):
#     dimensions(sizes):
#     variables(dimensions):
#     groups: forecast, analyses

for children in walktree(f_root_grp):
    for child in children:
        print(child)

# --------------- results:
#<class 'netCDF4._netCDF4.Group'>
# group /forecasts:
#     dimensions(sizes):
#     variables(dimensions):
#     groups:
# <class 'netCDF4._netCDF4.Group'>
# group /analyses:
#     dimensions(sizes):
#     variables(dimensions):
#     groups:
# <class 'netCDF4._netCDF4.Group'>
# group /forecast:
#     dimensions(sizes):
#     variables(dimensions):
#     groups: model1, model2
# <class 'netCDF4._netCDF4.Group'>
# group /forecast/model1:
#     dimensions(sizes):
#     variables(dimensions):
#     groups:
# <class 'netCDF4._netCDF4.Group'>
# group /forecast/model2:
#     dimensions(sizes):
#     variables(dimensions):
#     groups:
# -------------------------------------------------

level = f_root_grp.createDimension('level', None)
# results: <class 'netCDF4._netCDF4.Dimension'> (unlimited): name = 'level', size = 0

time = f_root_grp.createDimension('time', None)
# results: <class 'netCDF4._netCDF4.Dimension'> (unlimited): name = 'time', size = 0

# Energopomiar Gliwice   50.29547 N, 18.63829 E
szerokosc_geograficzna = f_root_grp.createDimension('lat', 50.29547)
dlugosc_geograficzna = f_root_grp.createDimension('lon', 18.63829)

print(f_root_grp.dimensions)

# Printing the Dimension  object provides useful summary info, including the name and length of the dimension, and whether it is unlimited.
for dimobj in f_root_grp.dimensions.values():
    print(dimobj)

#-------------------------------------------------------
times = f_root_grp.createVariable("time", "f8",("time",))
levels = f_root_grp.createVariable("level", "i4",("level",))
latitudes = f_root_grp.createVariable("lat", "f4",("lat",))
longitudes = f_root_grp.createVariable("lon", "f4",("lon",))
temp = f_root_grp.createVariable("temp", "f4",("time","level", "lat", "lon"))

temp.units = "K"
# print(temp)
# <class 'netCDF4._netCDF4.Variable'>
# float32 temp(time, level, lat, lon)
#     units: K
# unlimited dimensions: time, level
# current shape = (0, 0, 50, 18)
# filling on, default _FillValue of 9.969209968386869e+36 used

# Using the python len function with a Dimension instance returns current size of that dimension. Dimension.isunlimited() method of a Dimension instance be used to determine if the dimensions is unlimited, or appendable.
print(time.isunlimited())  #result: True
print(dlugosc_geograficzna.isunlimited())  #result: False
print(time.isunlimited())  #result: True

# a path to create a Variable inside a hierarchy of groups
f_root_grp.createVariable("/forecasts/model1/temp", "f4",("time", "level", "lat", "lon",))

# ...
# str. 11
for name in f_root_grp.ncattrs():
    print("Global attr {} = {}".format(name, getattr(f_root_grp,name)))



# explore the variables
print(f_root_grp.variables.keys())  # dict_keys(['time', 'level', 'lat', 'lon', 'temp'])

# explore temp variable
print(f_root_grp['temp'])
# <class 'netCDF4._netCDF4.Variable'>
# float32 temp(time, level, lat, lon)
#     units: K
# unlimited dimensions: time, level
# current shape = (0, 0, 50, 18)
# filling on, default _FillValue of 9.969209968386869e+36 used

# ploting data using matplotlib
plt.contourf(f_root_grp['temp'][0,:,:])
plt.colorbar()

# 01-09-2023 dziala
# -------------------------
# nc file is closing
f_root_grp.close()
# -------------------------


#------------------------------------------------------
#---------------------------------------------------
#----------------------str 65 ?   obsluga wielu plikow ??? nie ddziala
f1 = Dataset("p1_Tmax_Summer_rcp85_mean_v1.0.nc","w", format="NETCDF4_CLASSIC")
f2 = Dataset("p25_Tmax_Summer_rcp85_mean_v1.0.nc","w", format="NETCDF4_CLASSIC")
f1.createDimension("time",None)
f2.createDimension("time",None)
t1 = f1.createVariable("time","i",("time",))
t2 = f2.createVariable("time","i",("time",))
t1.units = "days since 2000-01-01"
t2.units = "days since 2000-02-01"
t1.calendar = "standard"
t2.calendar = "standard"
t1[:] = np.arange(31)
t2[:] = np.arange(30)
f1.close()
f2.close()
# Read the two files in at once, in one Dataset.
f = MFDataset("mftest_*nc")
t = f.variables["time"]
print(t.units)
#days since 2000-01-01
print(t[32])  # The value written in the file, inconsistent with the MF time units.
#1
T = MFTime(t)
