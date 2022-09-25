
## Defines a unit.  A unit has models with model stats

## Units are loaded in from csv where they have a quantity of each model

import random as rand

# model_stats = {
#     "M":0,
#     "WS":0,
#     "BS":0,
#     "S":0,
#     "T":0,
#     "W":0,
#     "A":0,
#     "Ld":0,
#     "Sv":0,
#     "Base": 25, #MM Diameter
#     "weapon": "lasgun"
# }



#temp
lasgun = {
    "Range": 24, #inch range
    "Type": "Rapid Fire 1",
    "S":"3",
    "AP": 0,
    "D": 1
}

def load_unit(unit_descriptor):
        models = []
        #TODO: Load from csv
        model= {
            "M":6,
            "WS":4,
            "BS":4,
            "S":3,
            "T":3,
            "W":1,
            "A":1,
            "Ld":7,
            "Sv":5,
            "Base": 25, #MM Diameter
            "weapon": "lasgun"}
        models.append(model)
        return models        

# An individual model from the unit can shoot
def model_shoot(model,weapon, target):
    #TODO: Rewrite this trashhhhh
    if weapon == "lasgun":
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
        for model in self.models:
            model_shoot(model,"lasgun", "null target")

    

    
