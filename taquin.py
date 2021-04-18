import time
import copy

SNAIL = {
    "right": "down",
    "down": "left",
    "left": "up",
    "up": "right"
}

class NotSolvableError(Exception):
    desc = "This puzzle have no solution"

class UnknownHeuristic(Exception):
    desc = "This heuristic is not implemented"

def check_solvable(size: int, plateau: list):
    current_inversion = 0
    expected_inversion = 0
    blank_row = None
    blank_row2 = None
    current_array = []
    expected_array = []

    for i in range(0, size):
        for j in range(0, size):
            if plateau[i][j].current_value == 0:
            # if plateau[i][j].current_value == plateau[size-1][size-1].expected_value:
                blank_row = i
                # blank_row = size - i
            if plateau[i][j].expected_value == 0:
                blank_row2 = i
                # blank_row2 = size - i
            current_array.append(plateau[i][j].current_value)
            expected_array.append(plateau[i][j].expected_value)

    for i in range(0, len(current_array)):
        for j in range(i+1, len(current_array)):
            if expected_array[i] > expected_array[j] and expected_array[i] != 0 and expected_array[j] != 0:
                expected_inversion += 1
            if current_array[i] > current_array[j] and current_array[i] != 0 and current_array[j] != 0:
                current_inversion += 1

    print('c1 :',current_inversion)
    print('e1 :', expected_inversion)
    if size % 2 == 0:
        current_inversion += blank_row
    # expected_inversion += blank_row2
    print('c2 :',current_inversion)
    print('e2 :', expected_inversion)
    if current_inversion % 2 == expected_inversion % 2:
        return True
    return False

    # for i in range(0, len(expected_array)):
    #     if current_array[i] != expected_array:
    #         for j in range(i + 1, len(expected_array)):
    #             if expected_array.index(current_array[i]) > expected_array.index(current_array[j]):
    #                 print(current_array[i], expected_array.index(current_array[i]), expected_array.index(current_array[j]))
    #                 inversion += 1
    #         seen = expected_array

    print("Blank_row:", blank_row)
    print("Inversion:", inversion)
    if size % 2 == 0:
        if blank_row % 2 != 0 and inversion % 2 == 0:
            return True
        elif blank_row % 2 == 0 and inversion % 2 != 0:
            return True
    else:
        if inversion % 2 == 0:
            return True
    return False

def connect(plateau: list, i: int, j: int, expected_value: int, size: int):
    plateau[i][j].expected_value = expected_value
    if (i + 1) * (j + 1) == size**2:
        plateau[i][j].normal_shape_expected_value = 0
    else:
        plateau[i][j].normal_shape_expected_value = i * size + j + 1
    if j > 0:
        plateau[i][j].left = plateau[i][j - 1]
    else:
        plateau[i][j].left = None
    try:
        plateau[i][j].right = plateau[i][j + 1]
    except IndexError:
        plateau[i][j].right = None
    if i > 0:
        plateau[i][j].up = plateau[i - 1][j]
    else:
        plateau[i][j].up = None
    try:
        plateau[i][j].down = plateau[i + 1][j]
    except IndexError:
        plateau[i][j].down = None
    return expected_value + 1

def connect_pieces(plateau: list, size: int, connection: str="right", i: int=0, j: int=0, value: int=1):
    if value == size * size:
        connect(plateau, i, j, 0, size)
        return plateau

    if connection == "right":
        while j < size-1 and plateau[i][j+1].expected_value == -1:
            value = connect(plateau, i, j, value, size)
            j += 1
        return connect_pieces(plateau, size, SNAIL[connection], i, j, value)

    if connection == "left":
        while j > 0 and plateau[i][j-1].expected_value == -1:
            value = connect(plateau, i, j, value, size)
            j -= 1
        return connect_pieces(plateau, size, SNAIL[connection], i, j, value)

    if connection == "down":
        while i < size-1 and plateau[i+1][j].expected_value == -1:
            value = connect(plateau, i, j, value, size)
            i += 1
        return connect_pieces(plateau, size, SNAIL[connection], i, j, value)

    if connection == "up":
        while i > 0 and plateau[i-1][j].expected_value == -1:
            value = connect(plateau, i, j, value, size)
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


def print_plat(plateau: list, size: int):
    print("Plateau :")
    for i in range(0, size):
        try:
            print(plateau[i][0].current_value, plateau[i][1].current_value, plateau[i][2].current_value, plateau[i][3].current_value)
        except:
            print(plateau[i][0].current_value, plateau[i][1].current_value, plateau[i][2].current_value)
    print()
    for i in range(0, size):
        try:
            print(plateau[i][0].normal_shape_expected_value, plateau[i][1].normal_shape_expected_value, plateau[i][2].normal_shape_expected_value, plateau[i][3].normal_shape_expected_value)
            print(plateau[i][0].current_value, plateau[i][1].normal_shape_expected_value, plateau[i][2].normal_shape_expected_value, plateau[i][3].normal_shape_expected_value)
        except:
            print(plateau[i][0].normal_shape_expected_value, plateau[i][1].normal_shape_expected_value, plateau[i][2].normal_shape_expected_value)
    print()


class Taquin(object):

    def __init__(self, size: int, data, heuristique):
        if heuristique not in ['manhattan', 'hamming', 'gaschnig']:
            raise UnknownHeuristic
        self.heuristique = heuristique
        self.size = size
        plateau = []
        for i in range(0, size):
            plateau.append([])

        empty_pos = None
        for i in range(0, size**2, size):
            for j in range(0, size):
                value = data[i+j]
                plateau[int(i / size)].append(Piece(value, int(i / size), j))
                if int(data[i+j]) == 0:
                    empty_pos = [int(i / size), j]
        self.plateau = connect_pieces(plateau, size)
        print_plat(self.plateau, self.size)
        if check_solvable(self.size, self.plateau) == False:
            raise NotSolvableError
        self.expected_value_index = {} 
        for i in range(0, size):
            for j in range(0, size):
                self.expected_value_index[self.plateau[i][j].expected_value] = [self.plateau[i][j].x, self.plateau[i][j].y]
        self.empty_pos = empty_pos
        self.last_move = None
        self.last_move_heuristique = 0
        self.moves_memory = []
        self.etat_to_cost = {}
        self.cost_to_etat = {}
        self.open = {}
        self.close = []
        self.count = 0
        self.priority = {}

    def plateau_to_string(self):
        string = ''
        for i in range(0, self.size):
            for j in range(0, self.size):
                string += str(self.plateau[i][j].current_value) + ','
        return string

    def distance_de_manhattan(self) -> float:
        h = 0
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.plateau[x][y].current_value != 0:
                    expected_x, expected_y = self.expected_value_index[self.plateau[x][y].current_value]
                    h += abs(x - expected_x) + abs(y - expected_y)
        return h

    def distance_de_hamming(self) -> int:
        h = 0
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.plateau[x][y].current_value != self.plateau[x][y].expected_value:
                    h += 1
        return h

    def distance_de_gaschnig(self):
        h = 0
        current_list = []
        expected_list = []
        for x in range(0, self.size):
            for y in range(0, self.size):
                current_list.append(self.plateau[x][y].current_value)
                expected_list.append(self.plateau[x][y].expected_value)
        while current_list != expected_list:
            if expected_list[current_list.index(0)] == 0:
                for i in range(0, len(current_list)):
                    if current_list[i] != expected_list[i]:
                        misplaced_value = current_list[i]
                        misplaced_index = i
                        break
                current_list[current_list.index(0)] = misplaced_value
                current_list[misplaced_index] = 0
            else:
                empty_index = current_list.index(0)
                exp_value = expected_list[empty_index]
                exp_value_current_index = current_list.index(exp_value)
                current_list[empty_index] = exp_value
                current_list[exp_value_current_index] = 0
            h += 1
        return h
                
    def move_up(self) -> bool:
        empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
        if empty_piece.up == None:
            return False
        else:
            empty_piece.current_value = empty_piece.up.current_value 
            self.empty_pos = [empty_piece.up.x, empty_piece.up.y]
            self.plateau[self.empty_pos[0]][self.empty_pos[1]].current_value = 0
            return True

    def move_down(self) -> bool:
        empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
        if empty_piece.down == None:
            return False
        else:
            empty_piece.current_value = empty_piece.down.current_value 
            self.empty_pos = [empty_piece.down.x, empty_piece.down.y]
            self.plateau[self.empty_pos[0]][self.empty_pos[1]].current_value = 0
            return True

    def move_left(self) -> bool:
        empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
        if empty_piece.left == None:
            return False
        else:
            empty_piece.current_value = empty_piece.left.current_value 
            self.empty_pos = [empty_piece.left.x, empty_piece.left.y]
            self.plateau[self.empty_pos[0]][self.empty_pos[1]].current_value = 0
            return True
            
    def move_right(self) -> bool:
        empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
        if empty_piece.right == None:
            return False
        else:
            empty_piece.current_value = empty_piece.right.current_value 
            self.empty_pos = [empty_piece.right.x, empty_piece.right.y]
            self.plateau[self.empty_pos[0]][self.empty_pos[1]].current_value = 0
            return True

    def check_a_star(self, g, moves, move):
        if self.heuristique == 'manhattan':
            h = self.distance_de_manhattan()
        if self.heuristique == 'hamming':
            h = self.distance_de_hamming()
        elif self.heuristique == 'gaschnig':
            h = self.distance_de_gaschnig()
        g += 1
        priority = h + g
        etat = self.plateau_to_string()
        if etat not in self.close:
            if etat not in self.open:
                tmp_moves = copy.copy(moves)
                tmp_moves.append(move)
                self.open[etat] = {"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': priority, 'moves': tmp_moves}
                if  priority in self.priority:
                    self.priority[priority].append({"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': priority, 'key': etat, 'moves': tmp_moves})
                else:
                    self.priority[priority] = [{"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': priority, 'key': etat, 'moves': tmp_moves}]

    def a_star(self, current_depth: int=1, max_depth: int=10):
        count = 0
        moves = []
        i = 0
        is_solved = 1
        while is_solved != 0:
            if self.move_up():
                self.check_a_star(count, moves, 'up')
                self.move_down()
                
            if self.move_down():
                self.check_a_star(count, moves, 'down')
                self.move_up()
                
            if self.move_left():
                self.check_a_star(count, moves, 'left')
                self.move_right()
                
            if self.move_right():
                self.check_a_star(count, moves, 'right')
                self.move_left()

            index1 = min(self.priority.keys())
            best = self.priority[index1][-1]

            self.plateau = best['plateau']
            self.empty_pos = best['empty_pos']
            count = best['g']
            moves = best['moves']
            is_solved = best['h']
            self.close.append(best['key'])
            del self.open[best['key']]

            del self.priority[index1][-1]
            if len(self.priority[index1]) == 0:
                del self.priority[index1]

            self.count += 1
            print(self.count, count)
        print(moves)
        print(len(moves))

    def is_solved(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.plateau[i][j].current_value != self.plateau[i][j].expected_value:
                    return False
        return True
