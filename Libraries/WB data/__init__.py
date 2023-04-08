from pathlib import Path
from zipfile import ZipFile

print(Path())

with ZipFile(r"C:\Users\Eddy.di\Downloads\API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_5358428.zip") as wbzip:
        wbzip.extractall("wbcsv")