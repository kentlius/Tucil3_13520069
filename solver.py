from puzzle import *

# check if the puzzle can be solved
# def isSolveable(puzzle):
#     return True

# check if puzzle is solved
def isSolved(puzzle):
    return puzzle == GOAL

# swap two tiles
def swap(puzzle, row1, col1, row2, col2):
    temp = puzzle[row1][col1]
    puzzle[row1][col1] = puzzle[row2][col2]
    puzzle[row2][col2] = temp

# find blank tile
def findBlank(puzzle):
    for i in range(DIM):
        for j in range(DIM):
            if puzzle[i][j] == BLANK:
                return i, j

# move blank tile
def right(puzzle):
    row, col = findBlank(puzzle)
    if col < DIM - 1:
        swap(puzzle, row, col, row, col + 1)

def left(puzzle):
    row, col = findBlank(puzzle)
    if col > 0:
        swap(puzzle, row, col, row, col - 1)

def up(puzzle):
    row, col = findBlank(puzzle)
    if row > 0:
        swap(puzzle, row, col, row - 1, col)

def down(puzzle):
    row, col = findBlank(puzzle)
    if row < DIM - 1:
        swap(puzzle, row, col, row + 1, col)

if __name__ == "__main__":
    filePuzzle = readPuzzle(PATH + "1.txt")
    print("File puzzle:")
    displayPuzzle(filePuzzle)
    print()

    down(filePuzzle)
    displayPuzzle(filePuzzle)
    print()

    right(filePuzzle)
    displayPuzzle(filePuzzle)
    print()

    down(filePuzzle)
    displayPuzzle(filePuzzle)
    print()
