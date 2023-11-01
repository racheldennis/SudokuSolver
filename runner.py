import pygame
import sys
from pygame.locals import QUIT
import time

# Initialize pygame
pygame.init()

count = True

# Set the countdown duration in seconds
countdown_duration = 10

# Keep track of time
start_time = time.time()

# Flags to control solving animation
solving = True
solved_board = None
solving_delay = 0  # Delay in milliseconds (adjust as needed)

# Highlight empty cells for 10 seconds, then make the entire board green
highlight_empty_duration = 10  # 10 seconds
highlight_empty = True  # Flag to control highlighting empty cells

# Constants
WIDTH, HEIGHT = 540, 540
GRID_SIZE = WIDTH // 9
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRID_THICKNESS = 2
FONT_SIZE = 50  # Increase the font size

# Create an initial Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Copy the board for solving
solving_board = [row[:] for row in board]

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SudokuSolver")

# Load a font
font = pygame.font.Font(None, FONT_SIZE)

# Initialize the game state
selected_cell = None

# Flash background color variables
flash_color = WHITE  # Start with a white background
flash_interval = 2000  # Interval to switch background color in milliseconds
flash_timer = 0

# Add drawing functions
def draw_grid():
    for i in range(10):
        # Determine if this line should be thicker to represent a 3x3 square border
        thickness = GRID_THICKNESS
        if i % 3 == 0:
            thickness = GRID_THICKNESS * 3  # Make the lines 3 times thicker for 3x3 squares

        # Horizontal lines
        pygame.draw.line(screen, BLACK, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE), thickness)

        # Vertical lines
        pygame.draw.line(screen, BLACK, (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT), thickness)

def draw_numbers(board):
    for i in range(9):
        for j in range(9):
            if board is not None and board[i][j] != 0:
                number = font.render(str(board[i][j]), True, BLACK)
                text_rect = number.get_rect(center=(j * GRID_SIZE + GRID_SIZE // 2, i * GRID_SIZE + GRID_SIZE // 2))
                screen.blit(number, text_rect)
            else:
                pygame.draw.rect(screen, (200, 200, 200), (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                draw_grid()

def valid(board, num, pos): # pos represents the row and column of a cell within the Sudoku board
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    # Calculate the top-left cell of the 3x3 box that contains the given position (pos).
    box_x = pos[1] // 3  # Determine the box's column (0, 1, or 2)
    box_y = pos[0] // 3  # Determine the box's row (0, 1, or 2)

    for i in range(box_y * 3, box_y * 3 + 3):  # Iterate over the rows in the box
        for j in range(box_x * 3, box_x * 3 + 3):  # Iterate over the columns in the box
            if board[i][j] == num and (i, j) != pos:  # If the number exists in the box and not at the given position (pos)
                return False  # The number is not valid
            
    return True  # The number is valid

def solve_board():
    global solving, solved_board, flash_color
    if solving:
        find = find_empty(solving_board)
        if not find:
            solving = False
            solved_board = [row[:] for row in solving_board]
            flash_color = GREEN  # Set background color to green when solved
            return
        else:
            row, col = find

        for i in range(1, 10):
            if valid(solving_board, i, (row, col)):
                solving_board[row][col] = i

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.time.delay(solving_delay)  # Introduce a delay
                screen.fill(WHITE)
                draw_grid()
                draw_numbers(solving_board)
                pygame.display.update()

                if solve_board():
                    return

        solving_board[row][col] = 0

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def main():
    global flash_timer, flash_color, solving, solved_board, start_time, highlight_empty, count

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        
        if count == True:
            screen.fill(WHITE)  # Start with a white background
            draw_numbers(solving_board)
            draw_grid()
            pygame.display.update()  # Update the screen to show any changes made before freezing
            pygame.time.delay(10000)  # Delay for 10,000 milliseconds (10 seconds)
            count = False
        
        if solving:
            solve_board()

        elapsed_time = time.time() - start_time

        if elapsed_time < highlight_empty_duration:
            # Highlight empty cells in green
            screen.fill(WHITE)  # Start with a white background
            empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
            for i, j in empty_cells:
                pygame.draw.rect(screen, GREEN, (j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                draw_numbers(solved_board if not solving else solving_board)
                draw_grid()
        else:
            # Make the entire board grey
            if highlight_empty:
                # Reset the start time and set the flag to switch to grey
                start_time = time.time()
                highlight_empty = False
            screen.fill((200, 200, 200))
            draw_grid()
            draw_numbers(solved_board if not solving else solving_board)

        pygame.display.update()

if __name__ == "__main__":
    main()
