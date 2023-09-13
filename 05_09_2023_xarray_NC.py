# import xarray as xr
#
# path = 'C:\\Users\pbednarczyk\Pawel_Bednarczyk_materialy\Copernicus\_wykresy_Copernicus_25_08_2023_MagalenaSkrzynska\Copernicus_Projekt_pythona_skrypty'
#
# climate_xr = xr.open_dataset('mean_Tmax_Yearly_rcp85_mean_v1_0_pobr_05_09_2023.nc')
##################################################################################################

# godz 15:20 - nie dziala
##############################################################################################
# https://www.earthinversion.com/utilities/reading-NetCDF4-data-in-python/?utm_content=cmp-true#google_vignette
from netCDF4 import Dataset, num2date
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


## Reading data
## Data at particular time snapshot (particular day)
ncfile = "C:\Users\pbednarczyk\Pawel_Bednarczyk_materialy\Copernicus\_wykresy_Copernicus_25_08_2023_MagalenaSkrzynska\Copernicus_Projekt_pythona_skrypty\mean_Tmax_Yearly_rcp85_mean_v1_0_pobr_05_09_2023.nc"
f1 = Dataset(ncfile)
# print(f1.variables.keys())


## Assigning variables
lats = f1.variables["lat"][:]
lons = f1.variables["lon"][:]
time = f1.variables["time"]

## Data for only one day
dates = num2date(time[:], time.units)
time_of_data = dates[0].strftime("%Y-%m-%d %H:%M:%S")
print(time_of_data)


Calprcp = f1.variables["precipitationCal"][:]
HQprcp = f1.variables["HQprecipitation"]

hqprc_dimensions = f1.variables["HQprecipitation"].dimensions  # ('time', 'lon', 'lat')

SelHQprc = HQprcp[0, :, :]  # remove the time dimension

ds = xr.Dataset(
    {
        "HQprcp": (("lon", "lat"), SelHQprc),
    },
    {
        "lon": lons,
        "lat": lats,
    },
)

df = ds.to_dataframe()

## Visualize the variations with longitude
plt.figure()
ds.mean(dim="lat").to_dataframe().plot(marker="o")
plt.savefig("variation_with_longitude.png", bbox_inches="tight")

## Visualize the variations with latitude
plt.figure()
ds.mean(dim="lon").to_dataframe().plot(marker="o")
plt.savefig("variation_with_latitude.png", bbox_inches="tight")