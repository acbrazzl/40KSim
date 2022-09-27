#find stats from the loaded sheets to be used elsewhere...
from unit import unit
from data import data


#TODO: Turn into class and have functions receive the sheets from their initialization in main (run.py)

#below was just cut from main() and would not work here until refactor
df = loaded.sheets['cache/Datasheets_models.csv']
  #for row in loaded.sheets['cache/Datasheets_models.csv']:
  #    print(row)

  #    if row[2] == "Guardsmen": 
  #    print(f"Found Guardsmen at row {row[0]}")
  #df.columns=df.loc[0]

  #print(f"Read headers:\n{df.head}") #holyshit, it doesn't print the heads, but some panda term for top of file

  

  #for col in df.columns:
    #print(col)
    #TODO: delete the "unamed 18" 
    #TODO: root cause pandas inability to read data or ditch it

  print(f"Read df as: \n{df}")
  print(df.get('datasheet_id', default=0))
  print(df.loc[df['name'] == "Guardsman"]) # <--This works and returns multiple hits if they exist
  print(df.loc[df['name'] == "Guardsman"].first_valid_index()) #<--returns just the index of the first hit
  print(df.iloc[519]["WS"].strip("+")) #<-- returns 4
  print(df.iloc[df.loc[df['name'] == "Guardsman"].first_valid_index()]["WS"].strip("+")) #<-- returns 4
  
  print(df.loc[df['name'] == "Guardsman"]["Cost"].min()) #<-- find lowest point value for the guardsman!
  #print(df['datasheet_id'] == "2") #<-- This does a boolean but doesn't even print true if they match...
  #df.loc[df['column_name'] == some_value]
  #print(df.loc[df['name'] == "Warbosss"])
