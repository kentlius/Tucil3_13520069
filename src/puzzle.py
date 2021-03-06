import random

DIM = 4 # dimension of puzzle
SIZE = DIM * DIM # board size
BLANK = "-" # blank tile

# Goal Node
GOAL = [["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", BLANK]]
PATH = "../test/" # path to puzzle files

# create shuffled 15 puzzle
def createShuffledPuzzle():
    value = ["1", "2", "3", "4",
             "5", "6", "7", "8",
             "9", "10", "11", "12",
             "13", "14", "15", BLANK]
    random.shuffle(value)
    puzzle = []
    for i in range(DIM):
        row = []
        for j in range(DIM):
            row.append(value[i * DIM + j])
        puzzle.append(row)
    return puzzle

# read puzzle from file
def readPuzzle(filename):
    puzzle = []
    with open(filename, "r") as f:
        for line in f:
            row = []
            for i in line.split():
                row.append(i)
            puzzle.append(row)
    return puzzle

# print puzzle
def displayPuzzle(puzzle):
    for i in range(DIM):
        print("---------------------")
        for j in range(DIM):
            print("|", end=" ")
            if(puzzle[i][j] == BLANK or int(puzzle[i][j]) < 10):
                print(puzzle[i][j], end="  ")
            else:
                print(puzzle[i][j], end=" ")
        print("|", end="")
        print()
    print("---------------------")
    print()

if __name__ == "__main__":
    print("Goal Puzzle:")
    displayPuzzle(GOAL)

    shuffledPuzzle = createShuffledPuzzle()
    print("Shuffled puzzle:")
    displayPuzzle(shuffledPuzzle)

    filePuzzle = readPuzzle(PATH + "solvable1.txt")
    print("File puzzle:")
    displayPuzzle(filePuzzle)
