import time

SNAIL = {
    "right": "down",
    "down": "left",
    "left": "up",
    "up": "right"
}

def connect(plateau: list, i: int, j: int, expected_value: int):
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


def print_plat(plateau: list, size: int):
    print("Plateau :")
    for i in range(0, size):
        try:
            print(plateau[i][0].current_value, plateau[i][1].current_value, plateau[i][2].current_value, plateau[i][3].current_value)
        except:
            print(plateau[i][0].current_value, plateau[i][1].current_value, plateau[i][2].current_value)
    
    print()
    # current_piece = plateau[0][0]
    # tmp = plateau[0][0]
    # while tmp != None:
    #     while current_piece != None:
    #         print('r :', current_piece.current_value)
    #         current_piece = current_piece.right
    #     print("down")
    #     tmp = tmp.down
    #     current_piece = tmp
    # current_piece = plateau[size-1][size-1]
    # tmp = plateau[size-1][size-1]
    # while tmp != None:
    #     while current_piece != None:
    #         time.sleep(0.1)
    #         print('l :', current_piece.current_value)
    #         current_piece = current_piece.left
    #     print("down")
    #     tmp = tmp.up
    #     current_piece = tmp
    
    # print("Attendu :")
    # for i in range(0, size):
    #     try:
    #         print(plateau[i][0].expected_value, plateau[i][1].expected_value, plateau[i][2].expected_value, plateau[i][3].expected_value)
    #     except:
    #         print(plateau[i][0].expected_value, plateau[i][1].expected_value, plateau[i][2].expected_value)



class Taquin(object):

    def __init__(self, size: int, data):
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
        self.expected_value_index = {} 
        for i in range(0, size):
            for j in range(0, size):
                self.expected_value_index[self.plateau[i][j].expected_value] = [self.plateau[i][j].x, self.plateau[i][j].y]
        self.empty_pos = empty_pos
    
    def heuristique1(self) -> int:
        total = 0
        for x in range(0, self.size):
            for y in range(0, self.size):
                # print(f"current : {self.plateau[x][y].current_value}, excpected : {self.plateau[x][y].expected_value}")
                expected_x, expected_y = self.expected_value_index[self.plateau[x][y].current_value]
                # print(f"exp x : {expected_x}, exp y : {expected_y}")
                # print(f"cur x : {x}, cur y : {y}")
                # print(abs(x - expected_x) + abs(y - expected_y))
                # print()
                total += abs(x - expected_x) + abs(y - expected_y)
        # print(total)
        return total

    def move_up(self) -> bool:
        empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
        # print(empty_piece.x, empty_piece.y)
        if empty_piece.up == None:
            return False
        else:
            empty_piece.current_value = empty_piece.up.current_value 
            self.empty_pos = [empty_piece.up.x, empty_piece.up.y]
            self.plateau[self.empty_pos[0]][self.empty_pos[1]].current_value = 0
            return True

    def move_down(self) -> bool:
        empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
        # print(empty_piece.x, empty_piece.y)
        if empty_piece.down == None:
            return False
        else:
            empty_piece.current_value = empty_piece.down.current_value 
            self.empty_pos = [empty_piece.down.x, empty_piece.down.y]
            self.plateau[self.empty_pos[0]][self.empty_pos[1]].current_value = 0
            return True

    def move_left(self) -> bool:
        empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
        # print(empty_piece.x, empty_piece.y)
        if empty_piece.left == None:
            return False
        else:
            empty_piece.current_value = empty_piece.left.current_value 
            self.empty_pos = [empty_piece.left.x, empty_piece.left.y]
            self.plateau[self.empty_pos[0]][self.empty_pos[1]].current_value = 0
            return True
            
    def move_right(self) -> bool:
        empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
        # print(empty_piece.x, empty_piece.y)
        if empty_piece.right == None:
            return False
        else:
            empty_piece.current_value = empty_piece.right.current_value 
            self.empty_pos = [empty_piece.right.x, empty_piece.right.y]
            self.plateau[self.empty_pos[0]][self.empty_pos[1]].current_value = 0
            return True

    def check_moves_up(self, max_step: int=1) -> list:
        done = 0
        heuristique = []
        for i in range(0, max_step):
            time.sleep(0.1)
            empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
            if self.move_up():
                done += 1
                heuristique.append([done, self.heuristique1()])
            else:
                break

        for i in range(0, done):
            self.move_down()

        return heuristique

    def check_moves_down(self, max_step: int=1) -> list:
        done = 0
        heuristique = []
        for i in range(0, max_step):
            time.sleep(0.1)
            empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
            if self.move_down():
                done += 1
                heuristique.append([done, self.heuristique1()])
            else:
                break

        for i in range(0, done):
            self.move_up()

        return heuristique

    def check_moves_left(self, max_step: int=1) -> list:
        done = 0
        heuristique = []
        for i in range(0, max_step):
            time.sleep(0.1)
            empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
            if self.move_left():
                done += 1
                heuristique.append([done, self.heuristique1()])
            else:
                break

        for i in range(0, done):
            self.move_right()

        return heuristique

    def check_moves_right(self, max_step: int=1) -> list:
        done = 0
        heuristique = []
        for i in range(0, max_step):
            time.sleep(0.1)
            empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
            if self.move_right():
                done += 1
                heuristique.append([done, self.heuristique1()])
            else:
                break

        for i in range(0, done):
            self.move_left()

        return heuristique

    def a_star(self):
        '''Calcul de l'heuristique permettant de décider quels mouvement
        faire pour résoudre le taquin
        '''

        max_step = self.size
        up_move = self.check_moves_up(max_step=max_step)
        down_move = self.check_moves_down(max_step=max_step)
        left_move = self.check_moves_left(max_step=max_step)
        right_move = self.check_moves_right(max_step=max_step)
        print_plat(self.plateau, self.size)
        print(up_move, "\n")
        print(down_move, "\n")
        print(left_move, "\n")
        print(right_move, "\n")

        return 0

    def is_solved(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.plateau[i][j].current_value != self.plateau[i][j].expected_value:
                    return False
        return True