from puzzle import *

# https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2020-2021/Algoritma-Branch-and-Bound-2021-Bagian1.pdf (page 18)
def POSISI(num, puzzle):
    if(num == 16):
        i, j = findBlank(puzzle)
        return i * DIM + j
    for i in range(DIM):
        for j in range(DIM):
            if puzzle[i][j] == str(num):
                return i * DIM + j

def KURANG(num, puzzle):
    count = 0
    for i in range(1, SIZE + 1):
        if POSISI(num, puzzle) < POSISI(i, puzzle):
            if(num > i):
                count += 1
    return count

# check if the puzzle can be solved
def isSolvable(puzzle):
    row, col = findBlank(puzzle)
    if (row + col) % 2 == 0:
        X = 0
    else:
        X = 1

    totalKURANG = 0
    for i in range (1, SIZE + 1):
        totalKURANG += KURANG(i, puzzle)

    if (totalKURANG + X) % 2 == 0:
        return True
    else:
        return False

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
    filePuzzle = readPuzzle(PATH + "unsolvable1.txt")
    print("File puzzle:")
    displayPuzzle(filePuzzle)
    print("Solvable:", isSolvable(filePuzzle))
    print()

    # down(filePuzzle)
    # displayPuzzle(filePuzzle)
    # print()

    # right(filePuzzle)
    # displayPuzzle(filePuzzle)
    # print()

    # down(filePuzzle)
    # displayPuzzle(filePuzzle)
    # print()
