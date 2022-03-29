import random

DIM = 4 # dimension of puzzle
SIZE = DIM * DIM # board size
BLANK = "-" # blank tile

# Goal Node
GOAL = [["1", "2", "3", "4"], ["5", "6", "7", "8"], ["9", "10", "11", "12"], ["13", "14", "15", BLANK]]
PATH = "./test/" # path to puzzle files

# create shuffled 15 puzzle
def createShuffledPuzzle():
    value = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", BLANK]
    random.shuffle(value)

    puzzle = []
    it = 0
    for i in range(DIM):
        row = []
        for j in range(DIM):
            row.append(value[it])
            it += 1
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
        for j in range(DIM):
            print(puzzle[i][j], end=" ")
        print()

if __name__ == "__main__":
    print("Goal Puzzle:")
    displayPuzzle(GOAL)
    print()

    shuffledPuzzle = createShuffledPuzzle()
    print("Shuffled puzzle:")
    displayPuzzle(shuffledPuzzle)
    print()

    filePuzzle = readPuzzle(PATH + "1.txt")
    print("File puzzle:")
    displayPuzzle(filePuzzle)

