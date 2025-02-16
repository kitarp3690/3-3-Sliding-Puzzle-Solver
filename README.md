
# 3x3 Sliding Puzzle Solver Using A* algorithm

This project implements a 3x3 sliding puzzle solver using the A* (A-star) algorithm in Python. The sliding puzzle consists of 8 numbered tiles and one empty space, with the goal of arranging the tiles in numerical order. The A* algorithm is employed to find the shortest path from the initial configuration to the solved state by evaluating possible moves based on a heuristic (Manhattan Distance). The program efficiently solves the puzzle and outputs the sequence of moves to reach the solution.

## Features

- Solves the 3x3 sliding puzzle using the A* algorithm.
- Displays the sequence of moves from the initial state to the solved state.
- Uses Manhattan Distance as the heuristic function to guide the search for the solution.
- Prints each step in the solution path.


## Requirements

- Python 3.12.0
- numpy for matrix manipulations.
- heapq for implementing the priority queue used in the A* algorithm.
## Installation

```bash
git clone https://github.com/kitarp3690/3x3-puzzle-solver.git
```
```bash
pip install numpy
```
```bash
cd 3-3-puzzle-solver
```
```bash
python main.py
```
    
## Usage/Examples

To use the sliding puzzle solver, simply run script given below. It will prompt you to input the initial state of the puzzle, where you need to enter numbers for each tile in the 3x3 grid, using 0 for the empty space.
```bash
python main.py
```

### Sample Input:
```
Enter number for [0][0] block: 5
Enter number for [0][1] block: 1
Enter number for [0][2] block: 2
Enter number for [1][0] block: 4
Enter number for [1][1] block: 0
Enter number for [1][2] block: 3
Enter number for [2][0] block: 7
Enter number for [2][1] block: 8
Enter number for [2][2] block: 6
```

### Sample Output
```
Initial State of Puzzle:
[[5 1 2]
 [4 0 3]
 [7 8 6]]

Steps:
step 1:
[[1 2 3]
 [4 5 6]
 [7 8 0]]
Solved!
```

## Acknowledgements

- Inspired by classic 8-puzzle problem.
- A* algorithm inspired by various online resources.
- Thanks to contributors and the Python community for the great libraries and tools!
## Contact Information

For any questions, feel free to contact me via GitHub or at my email: pratikshrestha362@gmail.com.

## Author

- [Pratik Shrestha](https://www.github.com/kitarp3690)

