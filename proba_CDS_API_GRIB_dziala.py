# updated: 21-08-2023
# Działa : plik z danymi w formacie GRIB jest odbierany z bazy i zapisywany w folderze PC
# https://ads.atmosphere.copernicus.eu/api-how-to

import urllib3
import cdsapi

# konfiguracja ustawien -----------------------------------------------------------------------------
# plik z roszerzeniem . w folderze: users\Bednarczyk Pawel
# .cdsapirc --->
# CDS () - moje
# url: https://cds.climate.copernicus.eu/api/v2
# key: 247777:09e736b1-cc34-48ed-9143-01ba17a40866

# ADS nie uzywane ? @ToDo
# url: https://ads.atmosphere.copernicus.eu/api/v2
# key: {uid}:{api-key}
# -----------------------------------------------------------------------------------------------

# grib -> ostanie dane
urllib3.disable_warnings()  # disable warnings Adding certificate verification is strongly advised.
# See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings

c = cdsapi.Client()
# c.retrieve("reanalysis-era5-pressure-levels",
#            {
#                "variable": "temperature",
#                "pressure_level": "1000",
#                "product_type": "reanalysis",
#                "year": "2023",
#                "month": "08",
#                "day": "31",
#                "time": "08:00",
#                "format": "grib"
#            }, "download.grib")

c.retrieve("projections-cmip5-monthly-single-levels",
           {
               'ensemble_member':'r1i1p1',
               "variable": "2m_temperature",
               "product_type": "reanalysis",
               'period': '203601-204012',
               #"year": "2023",
               #"month": "08",
               #"day": "29",
               #"time": "08:00",
               "format": "zip",
               "model":"gfdl_cm3",
               "experiment":"rcp_8_5",
           }, "download.zip")




# -----------------------------------------------------
# https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
# TLS Warnings
# urllib3 will issue several different warnings based on the level of certificate verification support. These warnings indicate particular situations and can be resolved in different ways.
#
# InsecureRequestWarning
# This happens when a request is made to an HTTPS URL without certificate verification enabled. Follow the certificate verification guide to resolve this warning.
#
# Making unverified HTTPS requests is strongly discouraged, however, if you understand the risks and wish to disable these warnings, you can use disable_warnings():
#
# import urllib3
#
# urllib3.disable_warnings()
# Alternatively you can capture the warnings with the standard logging module:
#
# logging.captureWarnings(True)
# Finally, you can suppress the warnings at the interpreter level by setting the PYTHONWARNINGS environment variable or by using the -W flag.
#
# Brotli Encoding
# Brotli is a compression algorithm created by Google with better compression than gzip and deflate and is supported by urllib3 if the Brotli package or brotlicffi package is installed. You may also request the package be installed via the urllib3[brotli] extra:
#
# $ python -m pip install urllib3[brotli]
# Here’s an example using brotli encoding via the Accept-Encoding header:
#
# import urllib3
#
# urllib3.request(
#     "GET",
#     "https://www.google.com/",
#     headers={"Accept-Encoding": "br"}
# )
# Zstandard Encoding
# Zstandard is a compression algorithm created by Facebook with better compression than brotli, gzip and deflate (see benchmarks) and is supported by urllib3 if the zstandard package is installed. You may also request the package be installed via the urllib3[zstd] extra:
#
# $ python -m pip install urllib3[zstd]
# Note
#
# Zstandard support in urllib3 requires using v0.18.0 or later of the zstandard package. If the version installed is less than v0.18.0 then Zstandard support won’t be enabled.
#
# Here’s an example using zstd encoding via the Accept-Encoding header:
#
# import urllib3
#
# urllib3.request(
#     "GET",
#     "https://www.facebook.com/",
#     headers={"Accept-Encoding": "zstd"}
# )
# Decrypting Captured TLS Sessions with Wireshark
# Python 3.8 and higher support logging of TLS pre-master secrets. With these secrets tools like Wireshark can decrypt captured network traffic.
#
# To enable this simply define environment variable SSLKEYLOGFILE:
#
# export SSLKEYLOGFILE=/path/to/keylogfile.txt
# Then configure the key logfile in Wireshark, see Wireshark TLS Decryption for instructions.
#
# Custom SSL Contexts
# You can exercise fine-grained control over the urllib3 SSL configuration by providing a ssl.SSLContext object. For purposes of compatibility, we recommend you obtain one from create_urllib3_context().
#
# Once you have a context object, you can mutate it to achieve whatever effect you’d like. For example, the code below loads the default SSL certificates, sets the ssl.OP_ENABLE_MIDDLEBOX_COMPAT flag that isn’t set by default, and then makes a HTTPS request:
#
# import ssl
#
# from urllib3 import PoolManager
# from urllib3.util import create_urllib3_context
#
# ctx = create_urllib3_context()
# ctx.load_default_certs()
# ctx.options |= ssl.OP_ENABLE_MIDDLEBOX_COMPAT
#
# with PoolManager(ssl_context=ctx) as pool:
#     pool.request("GET", "https://www.google.com/")
# Note that this is different from passing an options argument to create_urllib3_context() because we don’t overwrite the default options: we only add a new one.
