from puzzle import *
import copy
import time

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

def isSolved(puzzle):
    return puzzle == GOAL

def swap(puzzle, row1, col1, row2, col2):
    temp = puzzle[row1][col1]
    puzzle[row1][col1] = puzzle[row2][col2]
    puzzle[row2][col2] = temp

def findBlank(puzzle):
    for i in range(DIM):
        for j in range(DIM):
            if puzzle[i][j] == BLANK:
                return i, j

def moveBlank(puzzle, move):
    tempPuzzle = copy.deepcopy(puzzle)
    row, col = findBlank(tempPuzzle)
    if move == "up":
        swap(tempPuzzle, row, col, row - 1, col)
    elif move == "down":
        swap(tempPuzzle, row, col, row + 1, col)
    elif move == "left":
        swap(tempPuzzle, row, col, row, col - 1)
    elif move == "right":
        swap(tempPuzzle, row, col, row, col + 1)
    return tempPuzzle

def availableMove(puzzle, lastMove):
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

    delOppositeMove(availableMoves, lastMove)
    return availableMoves

def delOppositeMove(moves, lastMove):
    if(lastMove == "up"):
        moves.remove("down")
    elif(lastMove == "down"):
        moves.remove("up")
    elif(lastMove == "left"):
        moves.remove("right")
    elif(lastMove == "right"):
        moves.remove("left")

def getCost(puzzle):
    cost = 0
    for i in range(DIM):
        for j in range(DIM):
            if puzzle[i][j] != GOAL[i][j] and puzzle[i][j] != BLANK:
                cost += 1
    return cost

def solver(puzzle, totalNode):
    aliveNode = list(zip([0], [0], [puzzle], [""])) # cost, depth, puzzle, move
    # dict = {} # key: puzzle, value: [cost, depth, move]

    while aliveNode != []:
        lowestCostIndex = min(range(len(aliveNode)), key=aliveNode.__getitem__)
        lowestZip = aliveNode.pop(lowestCostIndex)
        currentDepth = lowestZip[1]
        currentNode = lowestZip[2]
        lastMove = lowestZip[3]

        # dict[aliveNode[lowestCostIndex][2]] = 1

        if isSolved(currentNode):
            return totalNode

        availableMoves = availableMove(currentNode, lastMove)

        # Generate new node
        newDepth = currentDepth + 1
        for move in availableMoves:
            totalNode += 1

            newNode = moveBlank(currentNode, move)
            newCost = getCost(newNode) + newDepth
            
            aliveNode.append((newCost, newDepth, newNode, move))

if __name__ == "__main__":
    puzzle = readPuzzle("./test/solvable1.txt")
    timerStart = time.perf_counter()
    total = solver(puzzle, totalNode=0)
    timerEnd = time.perf_counter()
    print(f"Elapsed Time: {timerEnd - timerStart:0.10f} seconds")
    print(total)
