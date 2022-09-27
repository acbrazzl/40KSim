#this class wraps the wahapedia datasheet by ingesting it at runtime
# ...Initially we will just ingest everything
# ...In the future, could implement a lookup & cache based approach


# A data.sheet is a dict of datasheets
# ...where key is sheet name and val is the sheet

from lib2to3.pgen2.pgen import DFAState
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
        df = pd.read_csv(file_name, sep = '|', engine = 'python')
        df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True) #error_bad_lines=False,
        sheets.update({file_name:df}) 
    print("Data loaded!")
    return sheets

class data:
    sheets = {} # a dict of datasheets
    
    def __init__(self):
        
        self.sheets = load_data()

    
