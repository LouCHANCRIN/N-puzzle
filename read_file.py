import os

class FormatError(Exception):
    desc = "Invalid number of values"

def get_data(path: str) -> list:
    if os.path.isdir(path):
        raise FormatError
    with open(path) as _file:
        raw_data = _file.read()
    len_raw_data = len(raw_data)
    if len_raw_data == 0:
        raise FormatError
    i = 0

    raw_data = raw_data.split('\n')
    cleaned_data = []
    for line in raw_data:
        cleaned_line = line.split('#')[0]
        if cleaned_line != '':
            cleaned_data.append(cleaned_line.split())
    if len(cleaned_data) == 0 or len(cleaned_data[0]) != 1:
        raise FormatError
    
    data = []
    for line in cleaned_data:
        for value in line:
            if not value.isnumeric():
                raise FormatError
            data.append(int(value))    

    size = int(data[0])
    del data[0]
    
    if len(data) != (size * size):
        raise FormatError

    for i in range(0, len(data)):
        if i not in data:
            raise FormatError
    return size, data