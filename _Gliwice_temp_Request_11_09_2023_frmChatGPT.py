import cdsapi

# Create a CDS API client and authenticate with your API key
# key_CDS = "247777:09e736b1-cc34-48ed-9143-01ba17a40866"
#         # Gliwice (Energopomiar):
#         # szerokość geograficzna: 50°17'43.5"N
#         # długość geograficzna: 18°38'17.5"E
#         # 50.295410, 18.638200
c = cdsapi.Client() #apikey="247777:09e736b1-cc34-48ed-9143-01ba17a40866")

# Define the parameters for the data request
request = {
    'product_type': 'reanalysis',
    'variable': '2m_temperature',
    'year': ['2040'],  # Historical and future years
    'month': ['01','02','03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],     # Monthly data
    'area': [50.3, 18.6, 50.1, 18.3],  # Define a bounding box for your location
    'format': 'netcdf',   # Data format
    'experiment' : ['rcp_2_6'],
}

# Send the request and retrieve the data
c.retrieve('reanalysis-era5-single-levels', request, 'temperature_data_11_09_2023.nc')

# Now you can use libraries like xarray or netCDF4 to process the data and plot it