import argparse

from update import update
from unit import model_shoot_stats, unit
from data import data



def main(args):
  print("Running...")
  if args.update:
    print("Updating...")
    update()
    print("Update Complete!")

  loaded = data()

  print(f"Loaded: {loaded.sheets.keys()}")

  print("Example of early combat")
  print("Loading Units")
  squad_one = unit("Guardsman") #TODO: load units from a unit list
  squad_two = unit("Space Marine")

  print("Shooting!")
  squad_one.shoot(squad_two)

  print("Shoot stats")
  model_shoot_stats(squad_one,"lasgun",squad_two,12)

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    #my_parser.add_argument('-s','--string',type=str,help="String to print")
    my_parser.add_argument('--update', action='store_true', help="Download data from Wahapedia")
    args = my_parser.parse_args()
    main(args)
