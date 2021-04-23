import os
import argparse
from pathlib import Path

from read_file import get_data
from taquin import Taquin, NotSolvableError, UnknownHeuristic
from read_file import FormatError


class ArgsError(Exception):
    desc = "Invalid args"

def test_errors(path):
    errors = os.listdir(path)
    for dir in errors:
        current_path = Path(path, dir)
        files = os.listdir(current_path)
        for file in files:
            current_file = Path(current_path, file)
            try:
                size, data = get_data(current_file)
                taquin = Taquin(size, data)
            except FormatError:
                print("Format error")

def test_unsolvable(path, heuristic):
    unsolvable_path = Path(path, 'unsolvable')
    solvable_path = Path(path, 'solvable')

    solvable = 0
    files = os.listdir(solvable_path)
    len_solvable = len(files)
    if True:
        for file in files:
            current_file = Path(solvable_path, file)
            size, data = get_data(current_file)
            try:
                taquin = Taquin(size, data, heuristic)
                solvable += 1
            except NotSolvableError:
                print(f"{current_file} : unsolvable error")

    unsolvable = 0
    files = os.listdir(unsolvable_path)
    len_unsolvable = len(files)
    if True:
        for file in files:
            current_file = Path(unsolvable_path, file)
            size, data = get_data(current_file)
            try:
                taquin = Taquin(size, data, heuristic)
                print(f"{current_file} : solvable error")
            except NotSolvableError:
                unsolvable += 1

    print(solvable, len_solvable)
    print(unsolvable, len_unsolvable)

def main(path, heuristic):
    size, data = get_data(path)
    try:
        taquin = Taquin(size, data, heuristic)
        taquin.a_star()
    except UnknownHeuristic:
        print("This heuristic is not implemented")
    except NotSolvableError:
        print("This puzzle is not solvable")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--h')
    parser.add_argument('--p')
    args = parser.parse_args()
    try:
        os.path.exists(args.p)
        main(args.p, args.h)
        # test_errors(args.p)
        # test_unsolvable(args.p, args.h)
    except:
        print("Path to the file is invalid")
        