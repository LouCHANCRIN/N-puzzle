import time
import copy

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

def connect_pieces(plateau : list, size : int, connection : str="right", i : int=0, j : int=0, value : int=1):
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
    
    # print()
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
        self.last_move = None
        self.last_move_heuristique = 0
        self.moves_memory = []
        self.etat_to_cost = {}
        self.cost_to_etat = {}
        self.open = {}
        self.close = []
        self.count = 0
        self.priority = {}
        # self.close = {}

    def plateau_to_string(self):
        string = ''
        for i in range(0, self.size):
            for j in range(0, self.size):
                string += str(self.plateau[i][j].current_value) + ','
        return string

    def distance_de_manhattan(self) -> float:
        import math
        h = 0
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.plateau[x][y].current_value != 0:
                    expected_x, expected_y = self.expected_value_index[self.plateau[x][y].current_value]
                    h += abs(x - expected_x) + abs(y - expected_y)
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

    def check_a_star2(self, g):
        h = self.distance_de_manhattan()
        g += 1
        etat = self.plateau_to_string()
        if etat not in self.close:
            if etat not in self.open or (etat in self.open and self.open[etat]['f'] > h + g):
                self.open[etat] = {"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': h + g}
        else:
            if self.close[etat]['f'] > h + g:
                self.open[etat] = {"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': h + g}

    def check_a_star(self, g):
        import math
        h = self.distance_de_manhattan()
        g += 1
        priority = h + g
        etat = self.plateau_to_string()
        if etat not in self.close:
            if etat not in self.open or (etat in self.open and self.open[etat]['f'] > h + g):
                self.open[etat] = {"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': h + g, 'prio': g/self.size}
                if  priority in self.priority:
                    self.priority[priority].append({"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': h + g, 'prio': g/self.size})
                else:
                    self.priority[priority] = [{"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': h + g, 'prio': g/self.size}]
                # self.open[etat] = {"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': h + g, 'prio': self.count}
        # elif self.close[etat]['f'] > h + g:
        #         self.open[etat] = {"plateau": copy.deepcopy(self.plateau), "empty_pos": self.empty_pos, "h": h, 'g': g, 'f': h + g}


    def a_star(self, current_depth: int=1, max_depth: int=10):
        count = 0
        i = 0
        is_solved = 1
        while is_solved != 0:
            if self.move_up():
                self.check_a_star(count)
                self.move_down()
                
            if self.move_down():
                self.check_a_star(count)
                self.move_up()
                
            if self.move_left():
                self.check_a_star(count)
                self.move_right()
                
            if self.move_right():
                self.check_a_star(count)
                self.move_left()

            index1 = min(self.priority.keys())
            best = self.priority[index1][-1]

            self.plateau = best['plateau']
            self.empty_pos = best['empty_pos']
            count = best['g']
            is_solved = best['h']
            self.close.append(best)
            # self.close[best] = self.open[best]
            # del self.open[best]

            del self.priority[index1][-1]
            if len(self.priority[index1]) == 0:
                del self.priority[index1]

            self.count += 1
            print(int(self.count), count)

        # print_plat(self.plateau, self.size)


    def a_star_shortest_way(self, current_depth: int=1, max_depth: int=10):
        count = 0
        i = 0
        is_solved = 1
        while is_solved != 0:
            if self.move_up():
                self.check_a_star(count)
                self.move_down()
                
            if self.move_down():
                self.check_a_star(count)
                self.move_up()
                
            if self.move_left():
                self.check_a_star(count)
                self.move_right()
                
            if self.move_right():
                self.check_a_star(count)
                self.move_left()

            best = None
            for etat in self.open:
                if best == None:
                    best = etat
                elif self.open[etat]['f'] == self.open[best]['f']:
                    # if self.open[etat]['g'] <= self.open[best]['g']:
                    # if self.open[etat]['h'] - self.open[etat]['prio'] < self.open[best]['h'] - self.open[best]['prio']:
                    if self.open[etat]['h'] < self.open[best]['h']:
                        best = etat
                    # elif self.open[etat]['h'] == self.open[best]['h'] and self.open[etat]['prio'] < self.open[best]['prio']:
                    #     best = etat

                elif self.open[etat]['f'] < self.open[best]['f']:
                # elif self.open[etat]['f'] + self.open[etat]['prio'] < self.open[best]['f'] + self.open[best]['prio']:
                # elif self.open[etat]['f'] - self.open[etat]['prio'] < self.open[best]['f'] - self.open[best]['prio']:
                # elif self.open[etat]['f'] <= self.open[best]['f'] and self.open[etat]['g'] <= self.open[best]['g']:
                    # if self.open[etat]['prio'] < self.open[best]['prio']:
                    best = etat

            self.plateau = self.open[best]['plateau']
            self.empty_pos = self.open[best]['empty_pos']
            count = self.open[best]['g']
            is_solved = self.open[best]['h']
            self.close.append(best)
            # self.close[best] = self.open[best]
            del self.open[best]

            self.count += 1
        print(int(self.count), count)

        # print_plat(self.plateau, self.size)



    def is_solved(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.plateau[i][j].current_value != self.plateau[i][j].expected_value:
                    return False
        return True

    def a_star_mutliple_moves(self):
        '''Calcul de l'heuristique permettant de décider quels mouvement
        faire pour résoudre le taquin
        '''
        # max_step = self.size
        max_step = 1
        check = {"UP" : [], "DOWN": [], "LEFT" : [], "RIGHT": []}
        FUNCTIONS = {
            'UP' : self.move_up,
            'DOWN' : self.move_down,
            'LEFT' : self.move_left,
            'RIGHT' : self.move_right,
        }

        check['UP'] = self.check_all_moves_up(max_step=max_step)
        check['DOWN'] = self.check_all_moves_down(max_step=max_step)
        check['LEFT'] = self.check_all_moves_left(max_step=max_step)
        check['RIGHT'] = self.check_all_moves_right(max_step=max_step)
        print(f"Up : {check['UP']}")
        print(f"Down : {check['DOWN']}")
        print(f"Left : {check['LEFT']}")
        print(f"Right : {check['RIGHT']}")
        print_plat(self.plateau, self.size)
        print()
        best = 0
        best_count = 0
        best_key = None
        for key in check:
            for i in range(0, len(check[key])):
                if check[key][i][1] > best:
                    best = check[key][i][1]
                    best_count = check[key][i][0]
                    best_key = key
        for i in range(0, best_count):
            FUNCTIONS[best_key]()
        print_plat(self.plateau, self.size)
        print('\n\n\n\n')
        time.sleep(1)

    def check_all_moves_up(self, max_step: int=1) -> list:
        done = 0
        heuristique = []
        for i in range(0, max_step):
            empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
            if self.move_up():
                done += 1
                heuristique.append([done, self.heuristique1()])
            else:
                break

        for i in range(0, done):
            self.move_down()

        return heuristique

    def check_all_moves_down(self, max_step: int=1) -> list:
        done = 0
        heuristique = []
        for i in range(0, max_step):
            empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
            if self.move_down():
                done += 1
                heuristique.append([done, self.heuristique1()])
            else:
                break

        for i in range(0, done):
            self.move_up()

        return heuristique

    def check_all_moves_left(self, max_step: int=1) -> list:
        done = 0
        heuristique = []
        for i in range(0, max_step):
            empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
            if self.move_left():
                done += 1
                heuristique.append([done, self.heuristique1()])
            else:
                break

        for i in range(0, done):
            self.move_right()

        return heuristique

    def check_all_moves_right(self, max_step: int=1) -> list:
        done = 0
        heuristique = []
        for i in range(0, max_step):
            empty_piece = self.plateau[self.empty_pos[0]][self.empty_pos[1]]
            if self.move_right():
                done += 1
                heuristique.append([done, self.heuristique1()])
            else:
                break

        for i in range(0, done):
            self.move_left()

        return heuristique
