SNAIL = {
    "right": "down",
    "down": "left",
    "left": "up",
    "up": "right"
}

def connect(plateau: list, i: int, j: int, expected_value: int):
    plateau[i][j].expected_value = expected_value
    try:
        plateau[i][j].left = plateau[i][j - 1]
    except IndexError:
        plateau[i][j].left = None
    try:
        plateau[i][j].right = plateau[i][j + 1]
    except IndexError:
        plateau[i][j].right = None
    try:
        plateau[i][j].up = plateau[i - 1][j]
    except IndexError:
        plateau[i][j].up = None
    try:
        plateau[i][j].down = plateau[i + 1][j]
    except IndexError:
        plateau[i][j].down = None
    return expected_value + 1

def connect_pieces(plateau: list, size: int, connection: str= "right", i = 0, j = 0, value=1):
    if value == size * size:
        connect(plateau, i, j, 0)
        return plateau

    if connection == "right":
        while j < size-1 and plateau[i][j+1].expected_value == -1:
            value = connect(plateau, i, j, value)
            j += 1
        return connect_pieces(plateau, size, SNAIL[connection], i, j, value)

    if connection == "left":
        while j > 0 and plateau[i][j-1].expected_value == -1:
            value = connect(plateau, i, j, value)
            j -= 1
        return connect_pieces(plateau, size, SNAIL[connection], i, j, value)

    if connection == "down":
        while i < size-1 and plateau[i+1][j].expected_value == -1:
            value = connect(plateau, i, j, value)
            i += 1
        return connect_pieces(plateau, size, SNAIL[connection], i, j, value)

    if connection == "up":
        while i > 0 and plateau[i-1][j].expected_value == -1:
            value = connect(plateau, i, j, value)
            i -= 1
        return connect_pieces(plateau, size, SNAIL[connection], i, j, value)

class Piece(object):

    def __init__(self, value: int, x: int, y: int):
        self.expected_value = -1
        self.current_value = value
        self.x = x
        self.y = y
        self.up = None
        self.down = None
        self.left = None
        self.right = None

class Taquin(object):

    def __init__(self, size: int, data: list):
        # the data should be cleaned before being sent here
        self.size = size
        plateau = []
        for i in range(0, size):
            plateau.append([])

        empty_pos = None
        for i in range(0, size * size, size):
            for j in range(0, size):
                value = int(data[i+j])
                plateau[int(i / size)].append(Piece(value, int(i / size), j))
                if int(data[i+j]) == 0:
                    empty_pos = [int(i / size), j]
        self.plateau = connect_pieces(plateau, size)
        self.empty_pos = empty_pos

    def is_solved(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.plateau[i][j].current_value != self.plateau[i][j].expected_value:
                    return False
        return True