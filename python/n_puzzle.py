import sys

class ArgsError(Exception):
    desc = "Invalid args"

class FormatError(Exception):
    desc = "Invalid number of values"

def get_data(path: str) -> list:
    with open(path) as _file:
        raw_data = _file.read()
    len_raw_data = len(raw_data)
    i = 0
    while i < len_raw_data:
        if raw_data[i] == '#':
            j = 0
            while raw_data[i + j] not in ['\n', '\0']:
                j += 1
            raw_data = raw_data[0:i] + raw_data[i + j:len_raw_data]
            len_raw_data = len(raw_data)
        i += 1
    return raw_data.split()

def a_star(plateau: list):
    return

def main():
    if (len(sys.argv) != 2 or (path := sys.argv[1]) == None):
        raise ArgsError
    data = get_data(path)
    size = int(data[0])
    if len(data) != (size * size + 1):
        raise FormatError
    del data[0]
    plateau = [[0] * size] * size
    for i in range(0, size * size, size):
        plateau[int(i / size)] = data[i:i + size]
    a_star(plateau)

if __name__ == "__main__":
    main()