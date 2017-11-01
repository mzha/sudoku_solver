# -- Sudoku Solver --
An attempt at solving sudoku using brute force methods.
The project has been coded using python 2.7.10

Currently, the project is able to solve sudoku puzzles that are of extra hard difficulty or lower. This has been tested by solving several puzzles at www.websudoku.com, on the "Evil" difficulty level.

Furthermore, this program is not yet able to solve the world's hardest sudoku puzzle.

The inputs to the solver are hard coded into the program.

#Features:
1. Solves the puzzle through an iterative process
2. Makes guesses to continue solving the puzzle

#Setup:

Clone the git repository using <code>git clone https://github.com/glee-/sudoku_solver.git</code>
After cloning the repository, run the program within a terminal using <code>python solver.py</code>

Within the program, the solver is called through the function <code>solve(board)</code>

#Future improvements

This program might be improved by importing numpy and using arrays, instead of the native lists.

Solving speed may be optimized by improving the guessing algorithm.
