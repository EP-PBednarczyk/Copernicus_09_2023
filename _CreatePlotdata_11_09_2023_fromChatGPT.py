# example 11-09-2023
# Here's a simplified example of how to create
# a Python script to plot temperature data. You'll need to adapt
# it to your specific data and requirements:
import json

import pandas as pd
import matplotlib.pyplot as plt
import json
import netCDF4
import numpy as np
import matplotlib.pyplot as plt

# Load temperature data from a CSV file (replace with your data source)
# data = pd.read_csv('temperature_data_11_09_2023.csv')

# -------------JSON configuration file with configuration open - for information --------------------------
directory_path='C:/Users/pbednarczyk/Pawel_Bednarczyk_materialy/Copernicus/_wykresy_Copernicus_25_08_2023_MagdalenaSkrzynska/Copernicus_Projekt_pythona_skrypty/_dane_to_2100_Gliwice_11_09_2023/adaptor.esgf_wps.retrieve-1694440875.5479217_11_09_2023/'
with open(directory_path+"adaptor.esgf_wps.retrieve-1694440875.5479217-3250-6-24159b53-7125-44d0-99f3-c3519d93f588_provenance.json", "r") as json_file:
    json_data = json.load(json_file)

print(f"Setup for data: %s",json_data)

# --------------------------------------------------------

# ----------open and readNC file - meteorological data
NC_file_name = 'ta_Amon_AWI-CM-1-1-MR_ssp245_r1i1p1f1_gn_20150116-21001216_v20190529.nc'  # your file name with the eventual path
nc_file = netCDF4.Dataset(directory_path+NC_file_name)  # reading the nc file and creating Dataset
print(f"nc_file.variables: {nc_file.variables}")
print(f"nc_file['ta'] variables: {nc_file['ta']}")
# <class 'netCDF4._netCDF4.Variable'>
# float32 ta(time, plev, lat, lon)
#     _FillValue: 1e+20
#     standard_name: air_temperature
#     long_name: Air Temperature
#     comment: Air Temperature
#     units: K
#     original_name: st
#     cell_methods: time: mean
#     cell_measures: area: areacella
#     history: 2019-06-09T22:57:16Z altered by CMOR: Reordered dimensions, original order: time lat lon plev. 2019-06-09T22:57:16Z altered by CMOR: replaced missing value flag (-9e+33) with standard missing value (1e+20). 2019-06-09T22:57:16Z altered by CMOR: Inverted axis: lat.
#     missing_value: 1e+20
# unlimited dimensions:
# current shape = (1032, 1, 54, 20)
# filling on



#@ToDo    12-09-2023

# from chat GPT 12-09-2023------------------------------------
# Assuming 'time' is a dimension in the NetCDF file
time_values = nc_file.variables['time'][:]  # Get the time value
# masked_array(data=[1.55000e+01, 4.50000e+01, 7.45000e+01, ...,
#                    3.13345e+04, 3.13650e+04, 3.13955e+04],
#              mask=False,
#        fill_value=1e+20)


# Define the years from now to 2100
start_year = 2016  # Replace with the current year
end_year = 2100

# Filter time values for the desired time range
start_index = np.where(time_values >= start_year)[0][0]
end_index = np.where(time_values <= end_year)[0][-1]

temperature_values = nc_file.variables['ta'][:]
print(f"temperature values: {temperature_values}")
#get temperature values
# masked_array(
#   data=[[[[300.41473, 300.42056, 300.34244, ..., 299.2983 , 299.29248,
#            299.8513 ],
#           [300.74158, 300.73993, 300.74625, ..., 299.439  , 299.2476 ,
#            299.2836 ],
#           [300.80392, 300.9545 , 301.033  , ..., 299.38983, 299.11096,
#            298.9159 ],
#           ...,
#           [279.67133, 279.3868 , 279.19482, ..., 275.9449 , 275.39206,
#            274.91656],
#           [279.6026 , 279.02917, 278.52634, ..., 275.32147, 274.97684,
#            274.695  ],
#           [279.63782, 279.0608 , 278.41486, ..., 274.6128 , 274.55917,
#            274.5539 ]]],
#         [[[301.04898, 301.01477, 300.95786, ..., 301.21194, 301.26483,
#            302.6211 ],
#           [300.97253, 300.8808 , 300.895  , ..., 302.50635, 302.52313,
#            303.13757],
#           [301.34885, 301.29623, 301.01218, ..., 303.20587, 303.35788,
#            303.57373],
#           ...,
#           [280.86954, 280.6975 , 280.5128 , ..., 277.7405 , 277.46417,
#            277.26117],
#           [280.86877, 280.4941 , 280.15863, ..., 276.79663, 276.84006,
#            276.9699 ],
#           [281.06512, 280.6347 , 280.2292 , ..., 276.28952, 276.61597,
#            276.98608]]],
#         [[[301.52655, 301.60242, 301.6756 , ..., 301.97192, 301.68967,
#            303.08902],
#           [301.60486, 301.64972, 301.58893, ..., 303.92212, 303.73636,
#            304.1832 ],
#           [301.82367, 301.99576, 301.73795, ..., 304.9955 , 305.2536 ,
#            305.30524],
#           ...,
#           [278.47446, 278.33218, 278.23178, ..., 277.77625, 277.9293 ,
#            277.67697],
#           [278.47842, 278.28674, 278.06073, ..., 277.14392, 277.13895,
#            276.9402 ],
#           [278.32007, 278.21088, 278.0262 , ..., 276.54   , 276.57462,
#            276.51584]]],
#         ...,
#         [[[300.54886, 300.59265, 300.50098, ..., 300.19174, 300.09442,
#            300.26733],
#           [300.52765, 300.44943, 300.35486, ..., 300.24814, 300.22025,
#            300.49176],
#           [300.53537, 300.53156, 300.33496, ..., 300.44443, 300.42844,
#            300.67163],
#           ...,
#           [291.0302 , 291.37314, 291.54605, ..., 289.8389 , 289.69907,
#            289.50174],
#           [290.17947, 290.48517, 290.68515, ..., 289.2874 , 289.15414,
#            288.9303 ],
#           [289.46924, 289.85907, 290.1699 , ..., 288.77524, 288.78397,
#            288.7377 ]]],
#         [[[300.74854, 300.82278, 300.75006, ..., 300.5553 , 300.55823,
#            300.65994],
#           [300.88617, 300.74387, 300.76263, ..., 300.69437, 300.75412,
#            300.96625],
#           [301.34366, 301.0657 , 300.87106, ..., 300.79395, 300.7936 ,
#            301.06326],
#           ...,
#           [284.71664, 284.7665 , 284.84094, ..., 282.9638 , 282.6344 ,
#            282.104  ],
#           [284.9966 , 284.7883 , 284.6116 , ..., 282.2804 , 282.1762 ,
#            281.89352],
#           [285.41623, 285.18402, 284.8564 , ..., 281.78064, 281.96442,
#            282.02527]]],
#         [[[301.32596, 301.26413, 301.1144 , ..., 300.20813, 300.2715 ,
#            300.52676],
#           [301.55704, 301.3607 , 301.28827, ..., 300.55066, 300.6494 ,
#            300.79645],
#           [301.96906, 301.73593, 301.58487, ..., 300.7123 , 300.70303,
#            300.82855],
#           ...,
#           [282.0797 , 281.6896 , 281.24417, ..., 277.30124, 276.23413,
#            275.27902],
#           [282.2704 , 281.65814, 281.01813, ..., 276.7053 , 276.17123,
#            275.79803],
#           [283.2245 , 282.55634, 281.8039 , ..., 276.55273, 276.61224,
#            276.83563]]]],
#   mask=False,
#   fill_value=1e+20,
#   dtype=float32)

# Filter time values for the desired time range
start_index = np.where(time_values >= start_year)[0][0]
end_index = np.where(time_values <= end_year)[0][-1]
print(f"start index: {start_index} for year {start_year}")
print(f"end index: {end_index} for year {end_year}")

#12-09-2023
# received: start_
# start_index: 66
# end_index: 68

# Extract temperature data for the specified time range
temperature_data = nc_file.variables['ta'][start_index:end_index + 1, 0, :, :]  # Assuming 'ta' is the temperature variable
# masked_array(
#   data=[[[298.9806 , 299.0212 , 299.01978, ..., 298.7464 , 298.9816 ,
#           300.7845 ],
#          [298.79526, 298.85773, 298.86368, ..., 298.83392, 299.06552,
#           300.02408],
#          [298.57993, 298.7608 , 298.81012, ..., 298.93015, 298.9649 ,
#           299.18857],
#          ...,
#          [294.0339 , 294.70605, 295.445  , ..., 300.91064, 301.76566,
#           302.1992 ],
#          [292.53256, 293.4759 , 294.52014, ..., 299.67636, 300.1532 ,
#           300.3671 ],
#          [292.04208, 292.87683, 293.82794, ..., 297.60446, 298.08618,
#           298.47824]],
#         [[298.75647, 298.8153 , 298.78452, ..., 298.96643, 299.1311 ,
#           299.85068],
#          [298.69025, 298.6433 , 298.60995, ..., 298.89957, 299.18753,
#           299.6929 ],
#          [298.57953, 298.69086, 298.70956, ..., 298.88748, 298.96298,
#           299.1792 ],
#          ...,
#          [293.45822, 293.9963 , 294.51837, ..., 300.56818, 301.75684,
#           302.7057 ],
#          [292.11676, 292.80103, 293.54813, ..., 299.92236, 300.8209 ,
#           301.4221 ],
#          [291.739  , 292.31937, 293.0011 , ..., 298.7871 , 299.54745,
#           300.05304]],
#         [[298.96704, 299.12366, 299.0911 , ..., 298.8118 , 298.76965,
#           298.8198 ],
#          [298.9944 , 298.94577, 298.8728 , ..., 298.7966 , 298.83694,
#           298.91574],
#          [298.9343 , 298.93304, 298.84497, ..., 298.721  , 298.64404,
#           298.80112],
#          ...,
#          [295.73627, 295.9542 , 296.1076 , ..., 297.86108, 298.08597,
#           298.17377],
#          [294.7984 , 295.27774, 295.77457, ..., 297.56693, 297.56412,
#           297.34818],
#          [294.34073, 294.8918 , 295.51874, ..., 296.34552, 296.4007 ,
#           296.30118]]],
#   mask=False,
#   fill_value=1e+20,
#   dtype=float32)




# Close the NetCDF file
nc_file.close()

# Create a time array for plotting
years = np.arange(start_year, end_year + 1)
print(f"years: {years}")

# array([2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026,
#        2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037,
#        2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048,
#        2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059,
#        2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070,
#        2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081,
#        2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092,
#        2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100])

# Plot the temperature data
plt.figure(figsize=(10, 6))
plt.contourf(years, nc_file.variables['lat'][:], temperature_data.mean(axis=(1, 2)), cmap='coolwarm')
plt.colorbar(label='Temperature (°C)')
plt.xlabel('Year')
plt.ylabel('Latitude')
plt.title('Average Temperature Over Time')
plt.grid(True)

# Show the plot
plt.show()

# ...
# ...

# # Assuming your data has columns 'Year', 'RCP2.6_Temperature', and 'RCP6.0_Temperature'
# # Replace these column names with your actual column names
# years = data['Year']
# rcp2_6_temp = data['RCP2.6_Temperature']
# rcp6_0_temp = data['RCP6.0_Temperature']
#
# # Create a line plot
# plt.figure(figsize=(10, 6))
# plt.plot(years, rcp2_6_temp, label='RCP2.6 Temperature', color='blue')
# plt.plot(years, rcp6_0_temp, label='RCP6.0 Temperature', color='red')
#
# # Add labels and a legend
# plt.xlabel('Year')
# plt.ylabel('Temperature (°C)')
# plt.title('Temperature Projection Comparison')
# plt.legend()
#
# # Show or save the plot
# plt.show()