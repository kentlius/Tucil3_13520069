import tkinter as tk
from tkinter.filedialog import askopenfilename
from solver import *
import tkinter.messagebox as tkMessageBox
import time

def displayInfo(puzzle):
    _, totalKURANG = isSolvable(puzzle)
    nilaiKurang = tk.Message(root, 
    text=f"Nilai KURANG(i):\nKURANG(1): {KURANG(1, puzzle)}\nKURANG(2): {KURANG(2, puzzle)}\nKURANG(3): {KURANG(3, puzzle)}\nKURANG(4): {KURANG(4, puzzle)}\nKURANG(5): {KURANG(5, puzzle)}\nKURANG(6): {KURANG(6, puzzle)}\nKURANG(7): {KURANG(7, puzzle)}\nKURANG(8): {KURANG(8, puzzle)}\nKURANG(9): {KURANG(9, puzzle)}\nKURANG(10): {KURANG(10, puzzle)}\nKURANG(11): {KURANG(11, puzzle)}\nKURANG(12): {KURANG(12, puzzle)}\nKURANG(13): {KURANG(13, puzzle)}\nKURANG(14): {KURANG(14, puzzle)}\nKURANG(15): {KURANG(15, puzzle)}\nKURANG(16): {KURANG(16, puzzle)}\nSigma KURANG(i) + X: {totalKURANG}")
    nilaiKurang.grid(row=0, column=2, rowspan=3)

def openFile():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    currentPuzzle = readPuzzle(filepath)
    for i in range(DIM):
        for j in range(DIM):
            entry[i * DIM + j].delete(0, tk.END)
            entry[i * DIM + j].insert(0, f"{currentPuzzle[i][j]}")
    displayInfo(currentPuzzle)
    root.title(f"15 Puzzle Solver - {filepath}")

def shufflePuzzle():
    currentPuzzle = createShuffledPuzzle()
    for i in range(DIM):
        for j in range(DIM):
            entry[i * DIM + j].delete(0, tk.END)
            entry[i * DIM + j].insert(0, f"{currentPuzzle[i][j]}")
    displayInfo(currentPuzzle)

def displayPuzzleGUI(puzzle):
    for i in range(DIM):
        for j in range(DIM):
            entry[i * DIM + j].delete(0, tk.END)
            entry[i * DIM + j].insert(0, f"{puzzle[i][j]}")

def displayPathGUI(node):
    if(node.parent == None):
        return
    displayPathGUI(node.parent)
    displayPuzzleGUI(node.puzzle)

def solvePuzzle():
    currentPuzzle = [[0 for i in range(DIM)] for j in range(DIM)]
    for i in range(DIM):
        for j in range(DIM):
            currentPuzzle[i][j] = str(entry[i * DIM + j].get())
    isSolve, _ = isSolvable(currentPuzzle)
    if(not isSolve):
        tkMessageBox.showinfo("Error", "Puzzle is not solvable")
        return
    timerStart = time.perf_counter()
    pathNode, totalNode = solver(currentPuzzle, totalNode = 0)
    timerEnd = time.perf_counter()
    if(not isSolved(currentPuzzle)):
        displayPathGUI(pathNode)

    tk.Label(root, text="Puzzle Solved!").grid(row=3, columnspan=2, padx=5)
    tk.Label(root, text=f"Elapsed Time: {timerEnd - timerStart:0.7f} s").grid(row=4, columnspan=2, padx=5, sticky=tk.W)
    tk.Label(root, text=f"Created Node: {totalNode}").grid(row=5, columnspan=2, padx=5, sticky=tk.W)

root = tk.Tk()
root.title("15 Puzzle Solver")

puzzle = tk.Frame(root)
puzzle.grid(row=0, columnspan=2, padx=5, pady=5)

entry = []
for i in range(SIZE):
    entry.append(tk.Entry(puzzle, width=4, justify=tk.CENTER, font=("Consolas", 20)))
    entry[i].grid(row=i//DIM, column=i%DIM)
    entry[i].insert(0, GOAL[i//DIM][i%DIM])

tk.Button(root, text='Shuffle', command=shufflePuzzle).grid(row=1, column=0, padx=5, pady=5, sticky=tk.EW)
tk.Button(root, text='Open File', command=openFile).grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
tk.Button(root, text='Solve', command=solvePuzzle).grid(row=2, columnspan=2, padx=5, pady=5, sticky=tk.EW)

root.mainloop()
