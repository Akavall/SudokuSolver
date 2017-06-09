Sudoku Puzzle Solver Algorithm

Simple, yet powerful approach.

1) We divide the puzzle into nine "subparts", where each subpart
is "sector" or "square", and columns and rows associated with it.
For example:

```
0 0 3 0 2 0 6 0 0
9 0 0 3 0 5 0 0 1
0 0 1 8 0 6 4 0 0
0 0 8 
7 0 0 
0 0 6 
0 0 2 
8 0 0 
0 0 5 
```

Subpart 1, could look like this. The "square" part

```
0 0 3
9 0 0
0 0 1
```

is treated differently; the subpart "owns it" it can make changes to
 it, while the data contained in rows and columns is just used for viewing, to help us restrict the values that we can put in the 0-slots of the square.

Building 9 different subparts is fairly straight-forward

2) Generate possible coordinate value combination per each subpart: 

For example, for the above subpart, possible values are:

```
[2,4,5,6,7,8]
```

For each 0-element, we find possible values, based on square, col, row 
restrictions, e.g, you cannot have two of the same values in the same column.

Then given these values, we construct combinations of possible values given
per coordinates, in this case it is three possible set of coordinates:

```
Possible Values
[(4, 8, 6, 7, 2, 5), (4, 8, 6, 7, 5, 2), (5, 8, 6, 4, 2, 7)]
Coordinates of current zeros 
[(0, 0), (0, 1), (1, 1), (1, 2), (2, 0), (2, 1)]
```

Therefore, one combo would be:
```
(0,0) -> 4
(0,1) -> 8
(1,1) -> 6
(1,2) -> 7
(2,0) -> 2
(2,1) -> 5
```

and so on

We got all combos for each part!

3) Iterate over all possible combos in all parts to find the solution.

That's it! 

After we filled the values in the first subpart, the next subpart will see 
these values in their rows/columns, and restrict their values accordingly.

However getting this part might be annoying technically. The most straight-
forward approach would be to write a nested loop with 9 levels; it will work.
In my approach above I a while loop and a Stack to accomplish the same task,
the code is more elegant, but not as easy to read. 

Performance:

The above algorithms solves easy sudoku puzzles in less than a second.
The problem that I pulled from wikipedia article on sudoku algorithms, does
not give my algorithm any problems; it solves it in 7 seconds. However, a
"challenging problem" from Skiena Algorithms Manual, poses difficulty it 
takes 3.5 minutes to solve. You can find those puzzles in `experiments.py`



