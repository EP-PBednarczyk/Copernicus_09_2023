import cdstoolbox as ct

@ct.application(title='Download data')
@ct.output.download()
def download_application():
    data = ct.catalogue.retrieve(
        'sis-temperature-statistics',
        {
            'variable': 'average_temperature', # '2m_temperature', 'average_temperature',
            'period': 'year',
            'experiment': [
                'rcp4_5',  # 'rcp8_5',
            ],
            'statistic': [
                '10th_percentile', '1st_percentile', '25th_percentile',
                '50th_percentile', '5th_percentile', '75th_percentile',
                '90th_percentile', '95th_percentile', '97th_percentile',
                # '99th_percentile',
                'time_average',
            ],
            'ensemble_statistic': [
                'ensemble_members_average',
                # 'ensemble_members_standard_deviation',
            ],
            # 'grid': [0.25, 0.25],
            # 'area': [50.2833 - 0.000025, 50.2833 + 0.000025, 18.6667 - 0.000025, 18.6667 + 0.000025],
        }
    )

    return data
