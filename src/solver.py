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

def moveBlank(puzzle, move):
    newPuzzle = []
    for i in range(DIM):
        row = []
        for j in range(DIM):
            row.append(puzzle[i][j])
        newPuzzle.append(row)
    if move == 'up':
        up(newPuzzle)
    elif move == 'down':
        down(newPuzzle)
    elif move == 'left':
        left(newPuzzle)
    elif move == 'right':
        right(newPuzzle)

    return newPuzzle

def availableMove(puzzle):
    availableMoves = []
    row, col = findBlank(puzzle)
    if row > 0:
        availableMoves.append('up')
    if row < DIM - 1:
        availableMoves.append('down')
    if col > 0:
        availableMoves.append('left')
    if col < DIM - 1:
        availableMoves.append('right')
    return availableMoves

def getCost(puzzle):
    cost = 0
    for i in range(DIM):
        for j in range(DIM):
            if puzzle[i][j] != GOAL[i][j] and puzzle[i][j] != BLANK:
                cost += 1
    return cost

def solver(puzzle, totalNode):
    puzzleQueue = list(zip([0], [0], [puzzle], [""])) # cost, depth, puzzle, move

    while puzzleQueue != []:
        lowestCostIndex = min(range(len(puzzleQueue)), key=puzzleQueue.__getitem__)
        lowestZip = puzzleQueue.pop(lowestCostIndex)
        lowestDepth = lowestZip[1]
        currentNode = lowestZip[2]
        lastMove = lowestZip[3]
        
        # displayPuzzle(currentNode)
        # print()

        # check if puzzle is solved
        if isSolved(currentNode):
            return totalNode

        availableMoves = availableMove(currentNode)

        # delete opposite last move
        if(lastMove == "up"):
            availableMoves.remove("down")
        elif(lastMove == "down"):
            availableMoves.remove("up")
        elif(lastMove == "left"):
            availableMoves.remove("right")
        elif(lastMove == "right"):
            availableMoves.remove("left")

        lowestDepth += 1
        for move in availableMoves:
            totalNode += 1

            newNode = moveBlank(currentNode, move)
            newCost = getCost(newNode) + lowestDepth
            
            puzzleQueue.append((newCost,lowestDepth, newNode, move))

if __name__ == "__main__":
    puzzle = readPuzzle("./test/test.txt")
    solver(puzzle, totalNode=0)
