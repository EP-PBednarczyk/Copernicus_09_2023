import cdstoolbox as ct


variables = {
    'Near-Surface Air Temperature': '2m_temperature',
   # 'Eastward Near-Surface Wind': '10m_u_component_of_wind',
   # 'Northward Near-Surface Wind': '10m_v_component_of_wind',
   # 'Sea Level Pressure': 'mean_sea_level_pressure',
   # 'Sea Surface Temperature': 'sea_surface_temperature',
}


@ct.application(title='Plot Map')
@ct.input.dropdown('variable', label='Variable', values=variables.keys())
@ct.output.figure()
def plot_map(variable):
    """
    Application main steps:

    - set the application layout with output at the bottom
    - select a variable name from a list in the dropdown menu
    - retrieve the selected variable
    - compose a title
    - show the result on a map using the chosen title

    """

    data = ct.catalogue.retrieve(
        'reanalysis-era5-single-levels',
        {
            'variable': variables[variable],
            'product_type': 'reanalysis',
            'year': '2022',
            'month': '08',
            'day': '15',
            'time': '12:00',
        }
    )

    title = '{}'.format(' '.join([text.capitalize() for text in variable.split('_')]))
  
    # Create a Magics map with a custom title
    fig = ct.map.plot(data, title=title)
    # To learn how to create simple Magics map consult the beginer's How to guide:      https://cds.climate.copernicus.eu/toolbox/doc/how-to/21_how_to_make_a_map_with_magics_part1/21_how_to_make_a_map_with_magics_part1.html

    return fig
