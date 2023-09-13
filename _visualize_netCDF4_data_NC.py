import netCDF4
import matplotlib.pyplot as plt


# My_path = 'p50_Tmax_Summer_rcp85_mean_v1.0.nc'
nc = netCDF4.Dataset(filename='p25_Tmax_Summer_rcp85_mean_v1.0.nc', mode='r')    #p50_Tmax_Summer_rcp85_mean_v1.0.n

print(nc)

# Check the data type
print(type(nc))  # <class 'netCDF4._netCDF4.Dataset'>

# Explore the variables
print(nc.variables.keys())  # dict_keys(['time'])