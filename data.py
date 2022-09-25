#this class wraps the wahapedia datasheet by ingesting it at runtime
# ...Initially we will just ingest everything
# ...In the future, could implement a lookup & cache based approach


# A data.sheet is a dict of datasheets
# ...where key is sheet name and val is the sheet

import pandas as pd
from update import sources
from update import cache_dir


def load_data():
    print("Loading data")
    sheets = {}
    for source in sources:
        file_name = cache_dir + source.split("/")[-1]
        print(f"Reading {file_name}")
        #TODO: improve ability to read dirty data
        sheets.update({file_name:pd.read_csv(file_name, error_bad_lines=False)})
    print("Data loaded!")
    return sheets

class data:
    sheets = {} # a dict of datasheets
    
    def __init__(self):
        
        self.sheets = load_data()

    
