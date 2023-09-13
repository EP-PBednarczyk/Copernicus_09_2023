# https://www.google.com/search?sca_esv=563044254&rlz=1C1GCEU_plPL1032PL1032&q=cdstoolbox+change+localization+copernicus+python&tbm=vid&source=lnms&sa=X&ved=2ahUKEwiK9Pqr5pWBAxWNhP0HHVwqD24Q0pQJegQIDBAB&biw=1422&bih=635&dpr=1.35#fpstate=ive&vld=cid:1f6d85ed,vid:U8iN9qN1fNU
# C3S User Learning Services - Downloading data with the API

import cdsapi

c = cdsapi.Client()

c.retrieve(
    'projections-cmip5-monthly-single-levels',
    {
        'esembly_member':'r1i1p1',
        'format':'zip',
        'variable':['2m_temperature', 'evaporation'],
        'model':'gfdl_cm3',
        'experiment':'rcp_8_5',
        'period':'203601-204012'
    },
    'download.zip'
)
