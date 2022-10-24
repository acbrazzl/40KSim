#this class wraps the wahapedia datasheet by ingesting it at runtime
# ...Initially we will just ingest everything
# ...In the future, could implement a lookup & cache based approach


# A data.sheet is a dict of datasheets
# ...where key is sheet name and val is the sheet

import logging
import pandas as pd
from update import sources
from update import cache_dir

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

def load_data():
    logger.debug("Loading data")
    sheets = {}
    for source in sources:
        file_name = cache_dir + source.split("/")[-1]
        logger.debug(f"Reading {file_name}")
        #TODO: improve ability to read dirty data
        df = pd.read_csv(file_name, sep = '|', engine = 'python')
        df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True) #error_bad_lines=False,
        sheets.update({file_name:df}) 
    logger.debug("Data loaded!")
    return sheets

class data:
    __instance = None
    sheets = {} # a dict of datasheets
    @staticmethod
    def getData():
        if data.__instance == None:
            data()
        return data.__instance
    def __init__(self):
        if data.__instance != None:
            raise Exception("Yo this is a singleton!")
        else:
            data.__instance = self
            self.sheets = load_data()


    
  

    
