import numpy as np
from itertools import product
import time

class Stack(object):
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def pop(self):
        return self.data.pop()
    def is_not_empty(self):
        return len(self.data) > 0 

class SubPart(object):

    def __init__(self, square, rows, cols):
        self.square = square
        self.rows = rows
        self.cols = cols
        self.num_set = set(range(10))
        self.original_zeros_raw = np.where(self.square == 0)
        self.original_zeros = zip(*np.where(self.square == 0))
        self.missing_nums = self.get_missing_nums()

    def get_missing_nums(self):
        return self.num_set.difference(set(np.reshape(self.square, 9, 1)))

    def get_combos(self):
        my_list = []

        for r, c in self.original_zeros:
            my_list.append(self.missing_nums.difference(set(self.cols[:,c]).union(set(self.rows[r]))))
        b = product(*my_list) 
        return [ele for ele in b if len(ele) == len(set(ele))]

    def fill(self, combo):
        self.square[self.original_zeros_raw] = combo

    def clear(self):                     
        self.square[self.original_zeros_raw] = 0


def check_solution(board):
    for line in board:
        if sorted(line) != range(1, 10):
            print("row: {}".format(line))
            return False


    for line in board.T:
        if sorted(line) != range(1, 10):
            print("column: {}".format(line))
            return False

    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            if sorted(board[i:i+3, j:j+3].ravel()) != range(1, 10):
                print("square: {}".format(board[i:i+3, j:j+3]))
                return False

    return True
 
def solve_sudoku(board):

    class_list = []

    for i in xrange(0,9,3):
        for j in xrange(0,9,3):
            class_list.append(SubPart(board[i:i+3, j:j+3], board[i:i+3, :], board[:,j:j+3]))

    class_list = zip(range(9), class_list)

    ind_map = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8}

    stack = Stack()
    stack.push(None)

    while stack.is_not_empty():

        combo = stack.pop()

        if combo is not None:

            for i in xrange(combo[0], 8):
                class_list[i][1].clear()

            # 8 has a different way of filling
            # we don't need to fill here
            if combo[0] != 8:
                class_list[combo[0]][1].fill(combo[1])
    
        if combo is None:
            for combo_0 in class_list[0][1].get_combos():
                stack.push((0, combo_0))

        elif combo[0] != 8: # Don't need to add 8 
            sub_part = class_list[ind_map[combo[0]]][1]
            for combo_n in sub_part.get_combos():
                stack.push((ind_map[combo[0]], combo_n))

        # if don't push 8 to the stack we don't get to this part
        if combo and combo[0] == 8:
            for combo_8 in class_list[8][1].get_combos():
                class_list[8][1].fill(combo_8)
                if check_solution(board):
                    return board
                class_list[8][1].clear() 
