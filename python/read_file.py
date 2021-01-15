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
