from prodict import Prodict
import json
import xmltodict
import requests
import gzip
# from urllib import request
from iteration_utilities import unique_everseen
import pandas as pd
import os


compressed_data_end_point = (
    "https://opendata.ndw.nu/Ongevalideerde_snelheden_en_Intensiteiten.xml.gz"
)


def download_file_from_url():
    url = compressed_data_end_point
    r = requests.get(url, allow_redirects=True)
    open("./raw_ndw_data.xml.gz", "wb").write(r.content)

def decompress_gzip_file():
        with gzip.open("./raw_ndw_data.xml.gz", "rb") as f:
            gzip_file_content = f.read()
            with open("./converted_data/converted_ndw_data.xml", "wb") as xml_file:
                xml_file.write(gzip_file_content)
        delete_gzip_file()

def delete_gzip_file():
    import os
    os.remove("./raw_ndw_data.xml.gz")

download_file_from_url()
decompress_gzip_file()




