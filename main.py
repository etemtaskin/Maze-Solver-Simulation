import tkinter as tk
import gui
import heapq

grid = gui.labyrinth
orig_bits = gui.orig_bits
rows, cols = len(grid), len(grid[0])
start_i, start_j = map(int, input("Start i j: ").split())
end_i, end_j = map(int, input("End i j: ").split())

def heuristic(i, j):
    return abs(i - end_i) + abs(j - end_j)

def get_neighbors(i, j):
    for di, dj, bitpos in [(-1,0,1),(1,0,0),(0,-1,3),(0,1,2)]:
        if orig_bits[i][j][bitpos] == '0':
            ni, nj = i+di, j+dj
            if 0 <= ni < rows and 0 <= nj < cols:
                yield ni, nj

def astar_search():
    g_scores = [[float('inf')] * cols for _ in range(rows)]
    f_scores = [[float('inf')] * cols for _ in range(rows)]
    parents = [[None] * cols for _ in range(rows)]
    open_heap = []
    closed_set = set()
    g_scores[start_i][start_j] = 0
    f_scores[start_i][start_j] = heuristic(start_i, start_j)
    heapq.heappush(open_heap, (f_scores[start_i][start_j], (start_i, start_j)))
    while open_heap:
        _, (i, j) = heapq.heappop(open_heap)
        if (i, j) in closed_set:
            continue
        closed_set.add((i, j))
        if (i, j) == (end_i, end_j):
            path = []
            node = (end_i, end_j)
            while node:
                path.append(node)
                node = parents[node[0]][node[1]]
            return path[::-1]
        for ni, nj in get_neighbors(i, j):
            if (ni, nj) in closed_set:
                continue
            tentative_g = g_scores[i][j] + 1
            if tentative_g < g_scores[ni][nj]:
                parents[ni][nj] = (i, j)
                g_scores[ni][nj] = tentative_g
                f_scores[ni][nj] = tentative_g + heuristic(ni, nj)
                heapq.heappush(open_heap, (f_scores[ni][nj], (ni, nj)))
    return []

path = astar_search()
root, C, cell, offs = gui.root, gui.C, gui.cell, gui.offs
r = cell/4
prev = (start_i, start_j)
index = 0

def draw_path_line(full_path):
    coords = []
    for i, j in full_path:
        x0, y0 = offs['original']
        coords.append((x0 + j*cell + cell/2, y0 + i*cell + cell/2))
    for a, b in zip(coords, coords[1:]):
        C.create_line(a[0], a[1], b[0], b[1], fill='green', width=2)

def on_space(event):
    global index, prev
    if index < len(path):
        i, j = path[index]
        dx = j - prev[1]
        dy = i - prev[0]
        gui.move(dx, dy)
        prev = (i, j)
        index += 1
    if index == len(path):
        draw_path_line(path)

root.bind('<space>', on_space)
root.mainloop()
