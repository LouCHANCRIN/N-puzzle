import sys

from read_file import get_data
from taquin import Taquin, connect_pieces

class ArgsError(Exception):
    desc = "Invalid args"

class FormatError(Exception):
    desc = "Invalid number of values"

def print_plat(plateau: list):
    print("Plateau :")
    for i in range(0, size):
        try:
            print(plateau[i][0].current_value, plateau[i][1].current_value, plateau[i][2].current_value, plateau[i][3].current_value)
        except:
            print(plateau[i][0].current_value, plateau[i][1].current_value, plateau[i][2].current_value)
    print("Attendu :")
    for i in range(0, size):
        try:
            print(plateau[i][0].expected_value, plateau[i][1].expected_value, plateau[i][2].expected_value, plateau[i][3].expected_value)
        except:
            print(plateau[i][0].expected_value, plateau[i][1].expected_value, plateau[i][2].expected_value)

def heuristique():
    return 1

def a_star(plateau: list, size: int, empty_pos: list):
    print(empty_pos)
    return

def main(plateau: list, size: int, empty_pos: list):
    a_star(plateau, size, empty_pos)

if __name__ == "__main__":
    if (len(sys.argv) != 2 or sys.argv[1] == None):
        raise ArgsError
    path = sys.argv[1]
    data = get_data(path)
    size = int(data[0])
    if len(data) != (size * size + 1):
        raise FormatError
    del data[0]
    plateau = []
    for i in range(0, size):
        plateau.append([])
    empty_pos = None
    for i in range(0, size * size, size):
        for j in range(0, size):
            value = int(data[i+j])
            plateau[int(i / size)].append(Taquin(value, int(i / size), j))
            if int(data[i+j]) == 0:
                empty_pos = [int(i / size), j]
    plateau = connect_pieces(plateau, size)
    print_plat(plateau)
    main(plateau, size, empty_pos)