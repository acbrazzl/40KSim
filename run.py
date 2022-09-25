import argparse

from unit import unit



def main(args):
  print("Running...")


  print("Example of early combat")
  print("Loading Units")
  squad_one = unit("TODO Add File Handle Here!")
  squad_two = unit("TODO Add File Handle Here!")

  print("Shooting!")
  squad_one.shoot(squad_two)

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    #my_parser.add_argument('-s','--string',type=str,help="String to print")
    args = my_parser.parse_args()
    main(args)
