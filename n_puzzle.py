import sys

from read_file import get_data
from taquin import Taquin, print_plat

class ArgsError(Exception):
    desc = "Invalid args"

class FormatError(Exception):
    desc = "Invalid number of values"


def main(taquin: object, which: int):
    # Check unsolvable
    taquin.a_star()

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
    # main(taquin, 1)