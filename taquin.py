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

def display_results(states, moves, time_complexity, size_complexity, size):
    for j in range(0, size):
        print(states[0][j])
    for i in range(1, len(states)):
        print(moves[i-1])
        for j in range(0, size):
            print(states[i][j])
    print(len(states))
    print(time_complexity)
    print(size_complexity)

def check_solvable(size: int, plateau: list):
    inversion = 0
    blank_row = None
    expected_blank_row = None
    current_array = []
    expected_array = []

    for i in range(0, size):
        for j in range(0, size):
            if plateau[i][j].current_value == 0:
                blank_row = size - i
            if plateau[i][j].expected_value == 0:
                expected_blank_row = size - i
            current_array.append(plateau[i][j].current_value)
            expected_array.append(plateau[i][j].expected_value)
        
    for i in range(0, len(current_array)):
        for j in range(i+1, len(current_array)):
            if current_array[i] != 0 and current_array[j] != 0 and expected_array.index(current_array[i]) > expected_array.index(current_array[j]):
                inversion += 1

    if size % 2 != 0:
        if inversion % 2 == 0:
            return True
    else:
        if blank_row % 2 == expected_blank_row % 2:
            inversion += 1
        if blank_row % 2 == 0 and inversion % 2 != blank_row % 2:
            return True
        if blank_row % 2 != 0 and inversion % 2 == blank_row % 2:
            return True
    return False

def connect(plateau: list, i: int, j: int, expected_value: int, size: int):
    plateau[i][j].expected_value = expected_value
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

class Taquin(object):

    def __init__(self, size: int, data, heuristique):
        if heuristique not in ['manhattan', 'hamming', 'gaschnig']:
            raise UnknownHeuristic
        self.size_complexity = 0
        self.time_complexity = 0
        self.heuristique = heuristique
        self.size = size
        plateau = []
        for i in range(0, size):
            plateau.append([])

        for i in range(0, size**2, size):
            for j in range(0, size):
                value = data[i+j]
                plateau[int(i / size)].append(Piece(value, int(i / size), j))
                if int(data[i+j]) == 0:
                    self.empty_pos = [int(i / size), j]
        self.plateau = connect_pieces(plateau, size)
        if check_solvable(self.size, self.plateau) == False:
            raise NotSolvableError
        self.expected_value_index = {} 
        for i in range(0, size):
            for j in range(0, size):
                self.expected_value_index[self.plateau[i][j].expected_value] = [self.plateau[i][j].x, self.plateau[i][j].y]
        self.moves_memory = []
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

    def list_state(self):
        state = []
        for i in range(0, self.size):
            state.append([])
            for j in range(0, self.size):
                state[i].append(self.plateau[i][j].current_value)
        return state

    def check_a_star(self, g, states, moves, move):
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

                tmp_states = copy.copy(states)
                state = self.list_state()
                tmp_states.append(state)
                self.time_complexity += 1
                self.open[etat] = {"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': priority, 'states': tmp_states, 'moves': tmp_moves}
                self.size_complexity = max(self.size_complexity, len(self.open))
                if  priority in self.priority:
                    self.priority[priority].append({"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': priority, 'key': etat, 'states': tmp_states, 'moves': tmp_moves})
                else:
                    self.priority[priority] = [{"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': priority, 'key': etat, 'states': tmp_states, 'moves': tmp_moves}]

    def a_star(self, current_depth: int=1, max_depth: int=10):
        i = 0
        count = 0
        states = [self.list_state()]
        moves = []
        is_solved = 1
        while is_solved != 0:
            if self.move_up():
                self.check_a_star(count, states, moves, 'up')
                self.move_down()
                
            if self.move_down():
                self.check_a_star(count, states, moves, 'down')
                self.move_up()
                
            if self.move_left():
                self.check_a_star(count, states, moves, 'left')
                self.move_right()
                
            if self.move_right():
                self.check_a_star(count, states, moves, 'right')
                self.move_left()

            index1 = min(self.priority.keys())
            best = self.priority[index1][-1]

            self.plateau = best['plateau']
            self.empty_pos = best['empty_pos']
            count = best['g']
            moves = best['moves']
            states = best['states']
            is_solved = best['h']
            self.close.append(best['key'])
            del self.open[best['key']]

            del self.priority[index1][-1]
            if len(self.priority[index1]) == 0:
                del self.priority[index1]

            self.count += 1
        display_results(states, moves, self.time_complexity, self.size_complexity, self.size)

    def is_solved(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.plateau[i][j].current_value != self.plateau[i][j].expected_value:
                    return False
        return True
