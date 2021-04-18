import sys
import os

from read_file import get_data
from taquin import Taquin, print_plat, NotSolvableError, UnknownHeuristic
from read_file import FormatError


class ArgsError(Exception):
    desc = "Invalid args"

def test_errors():
    path = os.listdir(sys.argv[1])
    print(path)
    for dir in path:
        current_path = sys.argv[1] + '/' + dir
        files = os.listdir(current_path)
        for file in files:
            current_file = current_path + '/' + file
            print(current_file)
            a = 0
            try:
                size, data = get_data(current_file)
                print("\n\n???\n\n")
                # size, data = get_data(path)
            except FormatError:
                print("ERROR")
                a = 1

            if a == 0:
                taquin = Taquin(size, data)

def main():
    if (len(sys.argv) != 3 or sys.argv[1] == None):
        print("Invalid arguments")
        return
    # test_errors()

    size, data = get_data(sys.argv[1])
    try:
        taquin = Taquin(size, data, sys.argv[2])
        taquin.a_star()
    except UnknownHeuristic:
        print("This heuristic is not implemented")
    except NotSolvableError:
        print("This puzzle is not solvable")


if __name__ == "__main__":
    main()