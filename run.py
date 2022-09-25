import argparse

from update import update
from unit import unit



def main(args):
  print("Running...")
  if args.update:
    print("Updating...")
    update()
    print("Update Complete!")

  print("Example of early combat")
  print("Loading Units")
  squad_one = unit("TODO Add File Handle Here!")
  squad_two = unit("TODO Add File Handle Here!")

  print("Shooting!")
  squad_one.shoot(squad_two)

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    #my_parser.add_argument('-s','--string',type=str,help="String to print")
    my_parser.add_argument('--update', action='store_true', help="Download data from Wahapedia")
    args = my_parser.parse_args()
    main(args)
