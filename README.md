# SudokuSolver

SudokuSolver is a Python project that automatically solves Sudoku puzzles using the pygame library for visualization. Users are not required to interact with the application as it initializes the Sudoku board in the code, solves it, and displays the solved puzzle automatically.

## Prerequisites

Before you can run this project, ensure you have the following prerequisites:

- Python installed on your system.
- The pygame library installed. You can install pygame using pip:

```bash
pip install pygame
```

## Getting Started

1. Open the `SudokuSolver.py` file in a code editor.

2. Locate the `board` variable in the code, which represents the initial Sudoku puzzle. **Please make sure to initialize the Sudoku puzzle you want to solve by modifying the `board` variable in the code**. You can change the initial puzzle to any Sudoku puzzle you'd like to solve. The puzzle is represented as a 2D list, where empty cells are represented by `0`.

3. Save the changes to the `SudokuSolver.py` file.

4. Open a terminal and navigate to the directory where the modified `SudokuSolver.py` file is located.

5. Run the SudokuSolver application by executing the following command:

```bash
python SudokuSolver.py
```

6. The application will display the initial Sudoku puzzle defined in the code.

7. The solver will automatically begin solving the puzzle.

8. Once the puzzle is successfully solved, the entire grid will flash green to indicate completion.

This addition clarifies how the initial Sudoku puzzle is represented in the code.

## Features

- Automatically initializes and solves a Sudoku puzzle.
- Visualizes the solving process using pygame.
- Displays the initial empty boxes in green and the grid turns grey upon successful puzzle completion.

## Customization

You can customize the initial Sudoku puzzle by modifying the `board` variable in the code. Input the puzzle you want to solve, and the solver will handle the rest of the process.

## How It Works

The SudokuSolver project uses a backtracking algorithm to solve Sudoku puzzles. This algorithm systematically fills in empty cells with numbers from 1 to 9, ensuring that each number is valid in its row, column, and 3x3 subgrid. If a number leads to an invalid configuration, the solver backtracks and tries a different number.

The solving process is visualized using the pygame library, allowing you to observe how the solver progresses towards a solution. Empty cells are initially highlighted in green, and the entire grid turns grey upon successful puzzle completion.

Understanding this backtracking algorithm can help you appreciate how the solver systematically finds a valid solution to Sudoku puzzles.

## Project In Action

### Initial Board

This is the initial Sudoku board that is assigned in the code:

<img src="https://github.com/racheldennis/SudokuSolver/assets/76753168/46e33e44-067d-47a8-b0c1-5ae4aec92feb" width="450" height="450">

<br><br>


### After Successful Puzzle Completion

After successfully solving the puzzle, the cells that were solved turn green.

<img src="https://github.com/racheldennis/SudokuSolver/assets/76753168/6847c0be-c2f9-402d-8f61-95fe8fac374e" width="450" height="450">

<br><br>


Then, the entire grid turns grey to indicate completion.

<img src="https://github.com/racheldennis/SudokuSolver/assets/76753168/edddb603-cfa3-4700-8957-f6b71f24e179" width="450" height="450">

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
