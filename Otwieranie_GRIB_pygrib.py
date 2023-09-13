# updated: 23-08-2023   @ToDo

import pygrib  #problem z instalajca 23-08-2023 -->MS C++ Redistri  @ToDo
import matplotlib.pyplot as plt

plt.figure(figsize=(13, 7))

grib = 'download.grib'  # fle GRIB with meteorological data
grbs = pygrib.open(grib)  # file GRIB is opening

# lists of the meteo data
for grb in grbs:
    print(grb)


#przyklad - plot (maps show)----------------------------------------------

# skin_alb = grbs.select(name='Forecast albedo')[0].values
# lats, lons = grbs.select(name='Forecast albedo')[0].latlons()
# albedo_by_year = grbs.select(name = 'Forecast albedo')
# albedo_by_year

# for alb in albedo_by_year:
#   year = alb.dataDate//10**4
#   skin_alb = alb.values
#   lats, lons = alb.latlons()
#   plt.figure(figsize=(10, 5))
#   plt.pcolormesh(lons,lats,skin_alb, cmap=plt.cm.PuBu)
#
#   # Visualize colorbar and title
#   plt.colorbar()
#   plt.title(f"Forecast albedo September{str(year)}")
#
#   # Show the plot
#   plt.show()

