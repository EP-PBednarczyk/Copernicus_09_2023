
### script to run ->for Copernicus website: historical temperature for Europe, future to 2030 year and to 2080 year

import cdstoolbox as ct

scenarios = {'RCP4.5': {'colour': '127,201,127'},  # '#7fc97f'},
             'RCP8.5': {'colour': '190,174,212'},  # '#beaed4'}
             'RCP6.0': {'colour':  '50,200,50'},   # chce Pani Magdalena S. 08-09-2023
             'RCP2.6': {'colour':  '200,50,200'},  # chce Pani Magdalena S. 08-09-2023
             }

options = {'Minimum temperature': 'minimum_temperature',
           'Mean temperature': 'average_temperature',
           'Maximum temperature': 'maximum_temperature'}

statistics = {'Mean': 'time_average',
              '10th percentile': '10th_percentile',
              '50th percentile': '50th_percentile',
              '90th percentile': '90th_percentile'}

seasons = ['Annual', 'Summer', 'Winter']

middleyear = {'Near future 2031-2060': '2045-01-01',
              'Far future 2071-2100': '2085-01-01'}
middleyear_summer = {'Near future 2031-2060': '2045-06-01',
                     'Far future 2071-2100': '2085-06-01'}


map_plot_options = [
    'Historical',
    'Near future 2031-2060 with RCP4.5',
    'Near future 2031-2060 with RCP8.5',
    'Far future 2071-2100 with RCP4.5',
    'Far future 2071-2100 with RCP8.5'
]


# --------------------------------------------------------------------------
# CHILD APPLICATION:
map_layout = ct.Layout(rows=1)
map_layout.add_widget(row=0, content='output-0')

child_layout = ct.Layout(rows=1)
child_layout.add_widget(row=0, content='output-1', sm=12, md=7, lg=8)
child_layout.add_widget(row=0, content=map_layout, sm=12, md=5, lg=4)


@ct.child(title='', layout=child_layout)
@ct.output.carousel()
@ct.output.livefigure()
def region_timeseries(params,
                      Variable, Statistic, Season):

    nuts_code = params['properties']['NUTS_ID']
    nuts_level = params['properties']['LEVL_CODE']

    mask = ct.shapes.catalogue.nuts(nuts_code=nuts_code, level=nuts_level)
    datas = {'mean': [], 'stdev': []}

    for i, Scenario in enumerate(scenarios):
        cat_entry_data = [
            'sis-temperature-statistics',
            {
                'variable': options[Variable],
                'period':Season.replace('ly', '').lower(),
                'statistic':statistics[Statistic],
                'experiment':Scenario.lower().replace('.', '_'),
                'ensemble_statistic': 'ensemble_members_average',
            }
        ]
        mean = ct.catalogue.retrieve(*cat_entry_data)
        cat_entry_stdev = [
            'sis-temperature-statistics',
            {
                'variable': options[Variable],
                'period':Season.replace('ly', '').lower(),
                'statistic':statistics[Statistic],
                'experiment':Scenario.lower().replace('.', '_'),
                'ensemble_statistic': 'ensemble_members_standard_deviation',
                'recache': '1',
            }
        ]
        stdev = ct.catalogue.retrieve(*cat_entry_stdev)

        region_select_allyrs_mean = ct.shapes.mask(mean, mask)
        datas['mean'].append(region_select_allyrs_mean)

        region_select_allyrs_stdev = ct.shapes.mask(stdev, mask)
        datas['stdev'].append(region_select_allyrs_stdev)

    return region_map_plot(datas['mean'], Season), region_xy_plot(datas)


#############################################################################
# PARENT APPLICATION
layout = ct.Layout(rows=3)
layout.add_widget(row=0, content='Season', sm=4)
layout.add_widget(row=0, content='Variable', sm=4)
layout.add_widget(row=0, content='Statistic', sm=4)

layout.add_widget(row=1, content='output-0')

layout.add_widget(row=2, content='[child]', height='40vh')


@ct.application(title='', layout=layout)
@ct.input.dropdown('Season', values=seasons)
@ct.input.dropdown(
    'Variable', values=options,
    default='Mean temperature', label='Daily temperature statistic'
)
@ct.input.dropdown('Statistic', values=statistics)
#@ct.output.livemap(click_on_feature=region_timeseries, height=50)   #comment 06-09-2023
def retrieve_app(Variable, Statistic, Season):
    # load data
    if Season == "Annual":
        Season = "Yearly"

    datas = []
    for Scenario in scenarios:
        cat_entry_data = [
            'sis-temperature-statistics',
            {
                'variable': options[Variable],
                'period':Season.replace('ly', '').lower(),
                'statistic':statistics[Statistic],
                'experiment':Scenario.lower().replace('.', '_'),
                'ensemble_statistic': 'ensemble_members_average'
            }
        ]
        datas.append(ct.catalogue.retrieve(*cat_entry_data))

    # plot mean of historial period 1976-2005 = the year 1990
    if Season == "Summer":
        hist = ct.cube.select(datas[0], time='1990-06-01')
    else:
        hist = ct.cube.select(datas[0], time='1990-01-01')
    hist = ct.cdm.update_attributes(hist, {
        "magics_style_name": "sis-temperature-exposure",
        'long_name': 'Near-Surface Air Temperature (°C)',
    })
    hist = ct.units.convert_units(hist, 'celsius')
    fut1s, fut2s = [], []
    label1s, label2s = [], []
    for data, Scenario in zip(datas, scenarios):
        fut1_period = 'Near future 2031-2060'
        fut2_period = 'Far future 2071-2100'
        # plot mean of future period
        if Season == "Summer":
            fut1 = ct.cube.select(data, time=middleyear_summer[fut1_period])
            fut2 = ct.cube.select(data, time=middleyear_summer[fut2_period])
        else:
            fut1 = ct.cube.select(data, time=middleyear[fut1_period])
            fut2 = ct.cube.select(data, time=middleyear[fut2_period])
        fut1 = ct.cdm.update_attributes(fut1, {
            "magics_style_name": "sis-temperature-exposure",
            'long_name': 'Near-Surface Air Temperature (°C)',
        })
        fut1 = ct.units.convert_units(fut1, 'celsius')
        fut2 = ct.cdm.update_attributes(fut2, {
            "magics_style_name": "sis-temperature-exposure",
            'long_name': 'Near-Surface Air Temperature (°C)',
        })
        fut2 = ct.units.convert_units(fut2, 'celsius')
        fut1s.append(fut1)
        label1s.append(fut1_period+' with '+Scenario)
        fut2s.append(fut2)
        label2s.append(fut2_period+' with '+Scenario)

    click_kwargs = {'Variable': Variable,
                    'Statistic': Statistic,
                    'Season': Season}

    datas = [hist]+fut1s+fut2s
    labels = ["Historical period 1976-2005"]+label1s+label2s
    data_layers = [{'data': dat, 'type': 'radio', 'label': label}
                   for dat, label in zip(datas, labels)]
    nuts_regions_layers = create_nuts_layers(click_kwargs)
    ocean_colour_scene = ct.shapes.catalogue.ocean()

    fig1 = ct.livemap.plot(
        data_layers + nuts_regions_layers + [ocean_colour_scene],
        show_legend=True, view='Europe',
        click_foreground_layer=True,
    )

    return fig1


############################################################################
# Functions

def create_nuts_layers(click_kwargs):

    #     nuts_table = ct.eurostat.nuts_table()
    #     countries = [ite for ite in nuts_table]
    level_0 = ct.shapes.catalogue.nuts(level=0)  # nuts_id=countries)

    # Also add the NUTS level 1 and 2 regions for selected countries
    NUTS_L3_countries = ['EE', 'HU', 'LT', 'LV']

    # , CNTR_CODE=NUTS_L1_countries)
    level_1 = ct.shapes.catalogue.nuts(level=1)
    # , CNTR_CODE=NUTS_L2_countries)
    level_2 = ct.shapes.catalogue.nuts(level=2)
    level_3 = ct.shapes.catalogue.nuts(level=3, CNTR_CODE=NUTS_L3_countries)

    nuts_regions_layers = [
        {
            'data': level_0, 'click_kwargs': click_kwargs,
            'zoom_to_selected': False, 'style': {'weight': 2.}
        },
        {
            'data': level_1, 'click_kwargs': click_kwargs,
            'label_template': '%{name}',
            'zoom_range': [4, 10], 'zoom_to_selected':False,
        },
        {
            'data': level_2, 'click_kwargs': click_kwargs,
            'label_template': '%{name}',
            'zoom_range': [5, 10], 'zoom_to_selected':False,
        },
        {
            'data': level_3, 'click_kwargs': click_kwargs,
            'label_template': '%{name}',
            'zoom_range': [6, 10], 'zoom_to_selected':False,
        },
    ]

    return nuts_regions_layers

# --------------------------------------------------------------------------


def region_xy_plot(datas):
    years = [str(w) for w in range(1986, 2085)]

    layout_dict = {
        'title': '',
        'xaxis': {
            'title': "Year",
            'automargin': True,
        },
        'yaxis': {
            'title': "Near surface air temperature (°C)",
            'automargin': True,
        },
        'legend': {
            'orientation': 'h',
            'y': 1.0,
            'x': 0.1,
        },
        'hovermode': 'x'
    }

    for i, Scenario in enumerate(scenarios):
        region_avg_mean = ct.cube.average(datas['mean'][i], dim=['lat', 'lon'])
        region_avg_stdev = ct.cube.average(
            datas['stdev'][i], dim=['lat', 'lon'])
        selected_nantimes_mean = ct.cube.select(
            region_avg_mean, time=['1986', '2085'])
        selected_nantimes_stdev = ct.cube.select(
            region_avg_stdev, time=['1986', '2085'])

        selected_nantimes_stdev = ct.operator.div(
            ct.operator.mul(selected_nantimes_stdev, 1.96), 2.83)

        low = ct.operator.sub(selected_nantimes_mean, selected_nantimes_stdev)
        low = ct.cdm.update_attributes(
            low, ct.cdm.get_attributes(selected_nantimes_mean)
        )

        high = ct.operator.add(selected_nantimes_mean, selected_nantimes_stdev)
        high = ct.cdm.update_attributes(
            high, ct.cdm.get_attributes(selected_nantimes_mean)
        )

        scatter_dict = {
            'line': {'color': 'rgba('+scenarios[Scenario]['colour']+',0.75)'},
            'name': 'lower', 'mode': 'lines',
            'hovertemplate': '%{y:.1f}°C<extra>lower limit</extra>',
            'showlegend': False, 'legendgroup': Scenario, 'x': years,
        }

        if i == 0:
            fig3 = ct.chart.line(low, scatter_dict=scatter_dict)
        else:
            fig3 = ct.chart.line(low, fig=fig3, scatter_dict=scatter_dict)

        scatter_dict.update({
            'fill': 'tonexty',
            'fillcolor': 'rgba('+scenarios[Scenario]['colour']+',0.5)',
            'hovertemplate': '%{y:.1f}°C<extra>upper limit</extra>',
            'name': 'upper', 'legendgroup': Scenario
        })
        fig3 = ct.chart.line(high, fig=fig3, scatter_dict=scatter_dict)

        scatter_dict = {
            'line': {'color': 'rgba('+scenarios[Scenario]['colour']+',0.75)'},
            'name': Scenario, 'mode': 'lines',
            'hovertemplate': '%{y:.1f}°C<extra>mean</extra>',
            'showlegend': True, 'legendgroup': Scenario, 'x': years
        }
        fig3 = ct.chart.line(
            selected_nantimes_mean, fig=fig3,
            scatter_dict=scatter_dict, layout_dict=layout_dict
        )

    return fig3


def region_map_plot(datas, season):
    fig2 = []
    for map_plot_option in map_plot_options:
        if map_plot_option == 'Historical':
            map_period = '1990-01-01'
            map_iRCP = 0
        else:
            map_period, map_RCP = map_plot_option.split(' with ')
            map_period = middleyear[map_period]
            if map_RCP == 'RCP4.5':
                map_iRCP = 0
            elif map_RCP == 'RCP8.5':
                map_iRCP = 1

        if season == 'Summer':
            map_period = map_period.replace('-01-01', '-06-01')

        map_plot_data = ct.cube.select(datas[map_iRCP], time=map_period)
        map_plot_data = ct.units.convert_units(map_plot_data, 'celsius')

        coords = ct.cdm.get_coordinates(map_plot_data)
        #-----------------------06-09-2023-----------------------------
        # wybieranie lokalizacji z mapy
        # min_lat = ct.math.min(coords['lat']['data'])-0.5
        # max_lat = ct.math.max(coords['lat']['data'])+0.5
        # min_lon = ct.math.min(coords['lon']['data'])-0.5
        # max_lon = ct.math.max(coords['lon']['data'])+0.5
        # Gliwice (Energopomiar) : 50.2833 -> (latitude) szerokość geograficzna 50st, 16minut 59 sekund N
        # 18.6667 -> (longitude) długość geograficzna 18st, 40minut, 0 sekund E
        # Gliwice (Energopomiar):
        # szerokość geograficzna: 50°17'43.5"N
        # długość geograficzna: 18°38'17.5"E
        # 50.295410, 18.638200
        # Gliwice
        Energopomiar_localization = [50.2833 - 0.000025, 50.2833 + 0.000025, 18.6667 - 0.000025, 18.6667 + 0.000025],
        coords['lat']['data'] = Energopomiar_localization[0]
        max_lat = Energopomiar_localization[1]
        min_lon = Energopomiar_localization[2]
        max_lon = Energopomiar_localization[3]
        min_lat = ct.math.min(coords['lat']['data'])-0.5
        max_lat = ct.math.max(coords['lat']['data'])+0.5
        min_lon = ct.math.min(coords['lon']['data'])-0.5
        max_lon = ct.math.max(coords['lon']['data'])+0.5
        # ------------------------------------------------------------------------------------------
        y_plot_size = 3+(x_plot_size*(max_lat-min_lat)/((max_lon-min_lon)))

        MAP_CONFIG['projection'].update(
            {'subpage_upper_right_longitude': max_lon,
             'subpage_upper_right_latitude': max_lat,
             'subpage_lower_left_longitude': min_lon,
             'subpage_lower_left_latitude': min_lat,
             'super_page_x_length': x_plot_size+3,
             'super_page_y_length': y_plot_size+3,
             'subpage_y_length': y_plot_size,
             'subpage_x_length': x_plot_size,
             'subpage_x_position': 1.5,
             'subpage_y_position': 1,
             }
        )
        MAP_CONFIG['title'] = {
            'text_lines': [
                '<font size="2">'+map_plot_option+'</font>',
                '<font size="1.2">Near surface air temperature (°C)</font>',
            ],
        }
        fig2.append(ct.map.plot(map_plot_data, **MAP_CONFIG))

    return ct.cdsplot.carousel(fig2)


x_plot_size = 20
MAP_CONFIG = {
    'contour': {
        'contour_automatic_setting': 'style_name',
        'contour_style_name': 'turbo_-20_40_continuous_grid',
        'legend': 'on',
    },
    'legend': {
        'legend_text_font_size': 0.6,
    },
    'projection': {
        'map_grid': "off",
        'subpage_align_vertical': "bottom",
        'subpage_map_area_definition': "corners",
        'map_label_height': .6
    },
    'background': {
        'map_coastline_sea_shade_colour': "#dddddd",
        'map_coastline_resolution': "high",
        'map_coastline_sea_shade': "on",
        'map_coastline_land_shade': 'on',
        'map_coastline_land_shade_colour': '#ffffff'
    },
    'foreground': {
        'map_coastline_resolution': "high",
        'map_coastline_colour': "#000000",
        'map_rivers': "on"
    },
}
