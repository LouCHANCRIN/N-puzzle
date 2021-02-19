import sys

from read_file import get_data
from taquin import Taquin, print_plat

class ArgsError(Exception):
    desc = "Invalid args"

class FormatError(Exception):
    desc = "Invalid number of values"

# def is_solved(plateau: list, size: int):
#     for 

# def heuristique(plateau: list, size: int) -> int:
#     score = 0
#     for i in range(0, size):
#         for j in range(0, size):
#             score += plateau[i][j].expected_value * plateau[i][j].current_value
#     return score

# def a_star(plateau: list, size: int, empty_pos: list):
#     print(heuristique(plateau, size))
#     return

def main(taquin: object):
    # Check unsolvable
    taquin.a_star()
    # count = 0
    # while not taquin.is_solved():
    #     print(count)
    #     taquin.a_star()
    #     count += 1

if __name__ == "__main__":
    if (len(sys.argv) != 2 or sys.argv[1] == None):
        raise ArgsError
    path = sys.argv[1]
    data = get_data(path)
    size = int(data[0])
    if len(data) != (size * size + 1):
        raise FormatError
    del data[0]
    taquin = Taquin(size, data)
    # plateau = connect_pieces(plateau, size)
    # print_plat(taquin.plateau, size)
    main(taquin)