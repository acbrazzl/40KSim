#find stats from the loaded sheets to be used elsewhere...
import logging
import string
from data import data
from model import model

logger = logging.getLogger(__name__)
logger.setLevel('INFO')


#TODO: Turn into class and have functions receive the sheets from their initialization in main (run.py)

#***Changing prints to logger.info here breaks the ability to load from csv :( . INVESTIGATE!

def find_model(model_name):
  found_model = model
  for key in model:
    try:
      model[key] = find_stat(model_name,key)
    except:
      logger.debug(f"No {key} associated with model") #TODO: populate weapons specially

  return found_model

def find_stat(model_name,stat):
  loaded = data.getData()
  logger.debug(f"Finding {stat}")
  df = loaded.sheets['cache/Datasheets_models.csv']
  val = df.iloc[df.loc[df['name'] == model_name].first_valid_index()][stat] #TODO: make this handle model stat types!
  logger.debug(f"Found {stat}:{val}")
  if type(val) is str:
    val = val.strip("+")
   
  return int(val)


 #for row in loaded.sheets['cache/Datasheets_models.csv']:
  #    print(row)

  #    if row[2] == "Guardsmen": 
  #    print(f"Found Guardsmen at row {row[0]}")
  #df.columns=df.loc[0]

  #print(f"Read headers:\n{df.head}") #holyshit, it doesn't print the heads, but some panda term for top of file

  

  #for col in df.columns:
    #print(col)

  # print(f"Read df as: \n{df}")
  # print(df.get('datasheet_id', default=0))
  # print(df.loc[df['name'] == model_name]) # <--This works and returns multiple hits if they exist
  # print(df.loc[df['name'] == model_name].first_valid_index()) #<--returns just the index of the first hit
  # print(df.iloc[519]["WS"].strip("+")) #<-- returns 4 (519 is the first gaurdsman)
  # print(df.iloc[df.loc[df['name'] == model_name].first_valid_index()]["WS"].strip("+")) #<-- returns 4
  
  # print(df.loc[df['name'] == model_name]["Cost"].min()) #<-- find lowest point value for the guardsman!
  #print(df['datasheet_id'] == "2") #<-- This does a boolean but doesn't even print true if they match...
  #df.loc[df['column_name'] == some_value]
  #print(df.loc[df['name'] == "Warbosss"])