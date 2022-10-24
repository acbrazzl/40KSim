
## Defines a unit.  A unit has models with model stats

## Units are loaded in from csv where they have a quantity of each model
import logging
import random as rand
from find import find_model
from model import model

logger = logging.getLogger(__name__)
logger.setLevel('INFO')


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
                logger.info("Hit!")
            else: logger.info("Miss!")
            #roll to wound (all units have same toughness)

            #target rolls save #TODO: handle disperate saves

            #
#compute stats: 
#print average number of shots, hits, wounds, and deaths
def model_shoot_stats(unit,weapon,target,distance):
    for idx,model in enumerate(unit.models):
        #compute shots
        #TODO: handle pistol, rapid fire, assult, & heavy
        #assume rapid
        shots = num_shots("rapid",12) #TODO: handles this stuff vs mock
        for shot in range(shots):
            hit = 1 -  ((model["BS"] - 1) / 6) #TODO: check this...
            stat = hit
            logger.info(f"Chance to hit: {hit}")
            wound = to_wound(3,target.models[0]["T"]) / 6 #TODO: wound function for comparison of 2-6



def num_shots(weapon_type, distance): #TODO: handle weapon types more accurately (from sheet)
    if distance >=12:
        shots = 2
    else: shots = 1
    return shots

#returns the to-wound roll necessary given a weapon strength and target unit toughness
def to_wound(strength, toughness):
    #double strength wounds on 2+
    #double toughness is wounded on a 6+
    mod = strength / toughness
    if mod >= 2: #ex: 8/4
        return 2
    elif mod > 1: #ex: 5/4
        return 3
    elif mod == 1: #ex 4/4
        return 4
    elif mod > 0.5: #ex 3/4
        return 5
    else: return 6 #ex 2/4


class unit:
    models = []

    def __init__(self,unit_descriptor):
        self.models = load_unit(unit_descriptor)

    def shoot(self, target):

            model_shoot(self.models,"lasgun", target)

    

    
