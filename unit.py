
## Defines a unit.  A unit has models with model stats

## Units are loaded in from csv where they have a quantity of each model

import random as rand
from find import find_model
from model import model


# from whapedia datasheet_models.csv:
#datasheet_id|line|name|M|WS|BS|S|T|W|A|Ld|Sv|Cost|cost_description|models_per_unit|cost_including_wargear|base_size|base_size_descr|
 #000000684|1|Guardsman|6"|4+|4+|3|3|1|1|6|5+|||9|true|25mm||

#temp
lasgun = {
    "Range": 24, #inch range
    "Type": "Rapid Fire 1",
    "S":"3",
    "AP": 0,
    "D": 1
}

def load_unit(unit_descriptor): #TODO: handle multipe models in a unit duhhh
        models = []
        #TODO: Load from csv
        model = find_model(unit_descriptor)

        #model= {
            # "M":6,
            # "WS":4,
            # "BS":4,
            # "S":3,
            # "T":3,
            # "W":1,
            # "A":1,
            # "Ld":7,
            # "Sv":5,
            # "Base": 25, #MM Diameter
            #"weapon": "lasgun"}
        model["weapon"] = "lasgun"
        models.append(model)
        return models        

# An individual model from the unit can shoot
def model_shoot(models,weapon, target):
    #TODO: Rewrite this trashhhhh
    for model in models: 
        if model["weapon"] == "lasgun":
            #roll to hit
            roll  = rand.randint(1,6)
            if roll >= model["BS"]:
                print("Hit!")
            else: print("Miss!")
            #roll to wound

            #target rolls save

            #


class unit:
    models = []

    def __init__(self,unit_descriptor):
        self.models = load_unit(unit_descriptor)

    def shoot(self, target):

            model_shoot(self.models,"lasgun", target)

    

    
