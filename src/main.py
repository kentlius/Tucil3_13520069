import os
import time
from solver import *

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
    # if KURANG(i, puzzle) != 0:
        print(i, ":", KURANG(i, puzzle))
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
    totalNode = solver(puzzle, totalNode = 0)
    timerEnd = time.perf_counter()
    print("Solved!")
    print(f"Elapsed Time: {timerEnd - timerStart:0.10f} seconds")
    print("Created Node:", totalNode)
    print()
    input("Press Enter to exit...")
else:
    input("Press Enter to exit...")