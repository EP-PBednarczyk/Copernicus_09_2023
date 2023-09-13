# https://cds.climate.copernicus.eu/toolbox/doc/index.html
# updated: 23-08-2023    @ToDo
# 2023-08-23 13:26:44,741 ERROR   Traceback (most recent call last):
# 2023-08-23 13:26:44,741 ERROR     File "/opt/cdstoolbox/cdscompute/cdscompute/cdshandlers/services/handler.py", line 59, in handle_request
# ...
#   File "C:\Users\pbednarczyk\Pawel_Bednarczyk_materialy\matlab_python\_Python_projekty\venv\Lib\site-packages\cdsapi\api.py", line 392, in workflow
#     return self.service("tool.toolbox.orchestrator.run_workflow", params)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\pbednarczyk\Pawel_Bednarczyk_materialy\matlab_python\_Python_projekty\venv\Lib\site-packages\cdsapi\api.py", line 382, in service
#     result = self._api(
#              ^^^^^^^^^^
#   File "C:\Users\pbednarczyk\Pawel_Bednarczyk_materialy\matlab_python\_Python_projekty\venv\Lib\site-packages\cdsapi\api.py", line 519, in _api
#     raise Exception(
# Exception: . Traceback (most recent call last):
#   File "/usr/local/lib/python3.6/dist-packages/jsonrequest/requests.py", line 71, in jsonrequestcall
#     resp = coding.encode(req.callable(*req.args, **req.kwargs), register=encoders, **context)
#   File "/usr/local/lib/python3.6/dist-packages/cdsworkflows/submit_workflow.py", line 55, in submit_workflow
#     results = workflow_bare_func(**kwargs)
# TypeError: application() missing 1 required positional argument: 'year'
# .

import cdstoolbox as ct

@ct.application(title="Mean daily temperature - Europe (0.25° x 0.25°)", description="Choose a year and click the link below to download the gridded data.")
@ct.input.dropdown('year', label='Year', values=[2008, 2009])
@ct.output.download()
#year = 2022
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
                '00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'
            ],
            'grid': [0.25, 0.25],
            'area': [60., -11., 34., 35.], # retrieve data for Europe only
        }
    )

    # Compute the daily mean temperature over Europe
    temperature_daily_mean = ct.cube.resample(temperature, freq='day', how='mean')

    return temperature_daily_mean