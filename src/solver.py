import os
import time
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

def solver(puzzle):
    for i in range(3):
        displayPuzzle(puzzle)
        print()
    return 0

if __name__ == "__main__":
    print("Solver for 15-puzzle")
    print("====================")
    print()
    print("1. Random Puzzle")
    print("2. Test Puzzle")
    print("3. Exit")
    print()
    choice = 0
    while(choice != 1 and choice != 2 and choice != 3):
        choice = int(input("Enter your choice: "))
        if choice == 1:
            puzzle = createShuffledPuzzle()
        elif choice == 2:
            filename = input("Enter filename: ")
            puzzle = readPuzzle(PATH + filename)
        elif choice == 3:
            exit()
        else:
            print("Invalid choice")

    os.system("cls")
    print("Puzzle:")
    displayPuzzle(puzzle)
    print()
    row, col = findBlank(puzzle)
    if (row + col) % 2 == 0:
        X = 0
    else:
        X = 1
    totalKURANG = 0
    print("Nilai KURANG(i):")
    for i in range(1, SIZE + 1):
        if KURANG(i, puzzle) != 0:
            print(i,":", KURANG(i, puzzle))
            totalKURANG += KURANG(i, puzzle)
    print()
    print("\sum_{n=1}^{16}KURANG(i) + X:", totalKURANG + X)
    print()
    print("Solvable?", isSolvable(puzzle))
    print()
    
    if(isSolvable(puzzle)):
        input("Press Enter to solve...")
        os.system("cls")
        print("Solving...")
        print()
        timerStart = time.perf_counter()
        solver(puzzle)
        timerEnd = time.perf_counter()
        print("Solved!")
        print(f"Elapsed Time: {timerEnd - timerStart:0.4f} seconds")
        print("Created Node :", "??")
        print()
        input("Press Enter to exit...")
    else:
        input("Press Enter to exit...")