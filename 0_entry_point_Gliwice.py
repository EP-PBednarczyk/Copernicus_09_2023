import cdstoolbox as ct
import datetime
years = [(datetime.datetime.today().year-80) + index for index in range(datetime.datetime.today().year-80)]

@ct.application(title = "Mean daily temperature over Europe - area Gliwice [50.2833-0.0025, 50.2833+0.0025, 18.6667-0.0025, 18.6667+0.0025]",
                description="Choose a year to update the time series plot below.")
@ct.input.dropdown('year', label='Range: 100 years (1923-2023), time: every 6 hour', values=years)
@ct.output.livefigure()
def application(year):
    # Retrieve the hourly 2m temperature over Europe for the selected year
    temperature = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels',
        {
            'variable': '2m_temperature',
            'product_type': 'reanalysis',
            'year': year,
            'month': list(range(1, 12 + 1)),
            'day': list(range(1, 31 + 1)),
            'time': [
                '00:00', # '01:00', '02:00', '03:00', '04:00', '05:00',
                '06:00', #'07:00', '08:00', '09:00', '10:00', '11:00',
                '12:00', #'13:00', '14:00', '15:00', '16:00', '17:00',
                '18:00', #'19:00', '20:00', '21:00', '22:00', '23:00'
            ],
            # 'grid': [0.25, 0.25],
            # from example 'area': [60., -11., 34., 35.],  # retrieve data for Europe only
            # 50.2833 -> szerokość geograficzna 50st, 16minut 59 sekund N
            # 18.6667 -> długość geograficzna 18st, 40minut, 0 sekund E
            # Gliwice
            'grid': [0.25, 0.25],
            'area': [50.2833-0.000025, 50.2833+0.000025, 18.6667-0.000025, 18.6667+0.000025],
        }

    )

    # Compute the daily mean temperature for every cell of the retrieved grid
    temperature_daily_mean = ct.cube.resample(temperature, freq='day', how='mean')

    # Perform the spatial average over Europe
    temperature_europe = ct.geo.spatial_average(temperature_daily_mean)

    # Plot the time series
    figure = ct.chart.line(temperature_europe)

    return figure


