import argparse
import logging

from update import update
from unit import model_shoot_stats, unit
from data import data

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

def main(args):
  print("Running...")
  logging.basicConfig(level=args.log_level)


  if args.update:
    update()

  loaded = data()

  logger.debug(f"Loaded: {loaded.sheets.keys()}")

  print("Example of early combat")
  print("Loading Units")
  squad_one = unit("Guardsman") #TODO: load units from a unit list
  squad_two = unit("Space Marine")

  print("Shooting!")
  squad_one.shoot(squad_two)

  print("Shoot stats")
  model_shoot_stats(squad_one,"lasgun",squad_two,12)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #parser.add_argument('-s','--string',type=str,help="String to print")
    parser.add_argument('--update', action='store_true', help="Download data from Wahapedia")
    parser.add_argument('-l', '--log_level', type=str, default = 'INFO', help='log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL')
    args = parser.parse_args()
    main(args)
