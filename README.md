# Maze-Solver-Simulation
Maze solver for micromause or maze robots. Coded with Python and Tkinter

## how to use?
If you have a maze code, paste your own instead of the maze code in the gui.py file.
If you do not have a labyrinth code, you can visit the "[Maze designer and creator](https://github.com/etemtaskin/Maze-Creator-and-Editor)" page to create one.

## How it works?
We use an algorithm called "Backtracking DFS with Path Commitment" to find the path.
The robot can only physically move along a single path. At each step, it visits only one cell, exploring all possible exits along that path before turning back.
If a path doesn't lead, it backtracks. It doesn't waste time revisiting cells it has already fully explored (thanks to the dead-end set).
