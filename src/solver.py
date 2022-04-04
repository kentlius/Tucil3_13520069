from puzzle import *
import copy

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
        return True, totalKURANG + X
    else:
        return False, totalKURANG + X

def isSolved(puzzle):
    return puzzle == GOAL

def swap(puzzle, row1, col1, row2, col2):
    puzzle[row1][col1], puzzle[row2][col2] = puzzle[row2][col2], puzzle[row1][col1]

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

def getCost(puzzle, depth):
    cost = 0
    for i in range(DIM):
        for j in range(DIM):
            if puzzle[i][j] != GOAL[i][j] and puzzle[i][j] != BLANK:
                cost += 1
    return cost + depth

class Node:
    def __init__(self, data=None):
        self.puzzle = data
        self.parent = None
        self.depth = 0

class PrioQueue(object):
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        return '\n'.join([str(i) for i in self.queue])

    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        temp = 0
        for i in range(len(self.queue)):
            if(self.queue[i][0] < self.queue[temp][0]):
                temp = i
        item = self.queue[temp]
        del self.queue[temp]
        return item

def displayPath(node):
    if(node.parent == None):
        return
    displayPath(node.parent)
    print("Move ",node.depth,": ")
    displayPuzzle(node.puzzle)
    print()

def solver(puzzle, totalNode):
    node = Node(puzzle)
    queue = PrioQueue()
    # [cost, node, move]
    queue.enqueue([getCost(node.puzzle, node.depth), node, ""])
    currentNode = Node(puzzle)
    visited = {}
    while not isSolved(currentNode.puzzle):
        minCostNode = queue.dequeue()
        currentNode = minCostNode[1]
        lastMove = minCostNode[2]
        visited[str(currentNode.puzzle)] = "visited"

        if isSolved(currentNode.puzzle):
            return currentNode, totalNode

        availableMoves = availableMove(currentNode.puzzle, lastMove)

        # Generate new node
        newDepth = currentNode.depth + 1
        for move in availableMoves:
            newNode = Node(moveBlank(currentNode.puzzle, move))
            if(str(newNode.puzzle) not in visited):
                newNode.parent = currentNode
                newNode.depth = newDepth
                newCost = getCost(newNode.puzzle, newDepth)

                totalNode += 1
                queue.enqueue([newCost, newNode, move])
    return node.puzzle, totalNode

if __name__ == "__main__":
    puzzle = readPuzzle("./test/solvable2.txt")
    currentNode, total = solver(puzzle, totalNode=0)
    displayPuzzle(puzzle)
    displayPath(currentNode)
    print(total)
