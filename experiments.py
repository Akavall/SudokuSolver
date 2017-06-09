import numpy as np
from sudoku_solver import solve_sudoku, check_solution

if __name__ == "__main__":

    # The puzzle is taken from skiena 
    # Algorithm Design Manual, page 239
    # it is intended to be challenging 
    skiena = np.array([[0,0,0,0,0,0,0,1,2],
                       [0,0,0,0,3,5,0,0,0],
                       [0,0,0,6,0,0,0,7,0],
                       [7,0,0,0,0,0,3,0,0],
                       [0,0,0,4,0,0,8,0,0],
                       [1,0,0,0,0,0,0,0,0],
                       [0,0,0,1,2,0,0,0,0],
                       [0,8,0,0,0,0,0,4,0],
                       [0,5,0,0,0,0,6,0,0]], dtype=np.int8)

    # The puzzle is taken from wikipedia article,
    # it is designed to work against brute force algorithms
    # https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#/media/File:Sudoku_puzzle_hard_for_brute_force.svg

    wiki_hard = np.array([[0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,3,0,8,5],
                          [0,0,1,0,2,0,0,0,0],
                          [0,0,0,5,0,7,0,0,0],
                          [0,0,4,0,0,0,1,0,0],
                          [0,9,0,0,0,0,0,0,0],
                          [5,0,0,0,0,0,0,7,3],
                          [0,0,2,0,1,0,0,0,0],
                          [0,0,0,0,4,0,0,0,9]])

    # example/first puzzle in project euler 96
    # https://projecteuler.net/problem=96
    project_euler_96_p1 = np.array([[0,0,3,0,2,0,6,0,0],
                                    [9,0,0,3,0,5,0,0,1],
                                    [0,0,1,8,0,6,4,0,0],
                                    [0,0,8,1,0,2,9,0,0],
                                    [7,0,0,0,0,0,0,0,8],
                                    [0,0,6,7,0,8,2,0,0],
                                    [0,0,2,6,0,9,5,0,0],
                                    [8,0,0,2,0,3,0,0,9],
                                    [0,0,5,0,1,0,3,0,0]])


    softball = np.array([[4,0,3,0,2,1,6,0,7],
                         [9,6,7,3,4,5,8,2,1],
                         [2,5,1,8,7,6,4,9,3],
                         [5,4,8,1,3,2,9,7,6],
                         [7,2,9,5,6,4,1,3,8],
                         [1,3,6,7,9,8,2,4,5],
                         [3,7,2,6,8,9,5,1,4],
                         [8,1,4,2,5,3,7,6,9],
                         [6,9,5,4,1,7,3,8,2]])


    softball_2 =  np.array([[4,8,3,0,2,0,6,0,0],
                            [9,6,7,3,0,5,0,0,1],
                            [0,5,1,8,0,6,4,0,0],
                            [0,0,8,1,0,2,9,0,0],
                            [7,0,0,0,0,0,0,0,8],
                            [0,0,6,7,0,8,2,0,0],
                            [0,0,2,6,0,9,5,0,0],
                            [8,0,0,2,0,3,0,0,9],
                            [0,0,5,0,1,0,3,0,0]])



    solution = solve_sudoku(real_sudoku)
    print "Solution:"
    print solution
    print(check_solution(np.array(solution)))


