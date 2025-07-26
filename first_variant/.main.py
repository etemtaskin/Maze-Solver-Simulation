import time
from gui import setup, labyrinthCode, startCell, endCell, cellsize, margin

root, canvas, robot, text_ids, offset2 = setup()
rows, cols = len(labyrinthCode), len(labyrinthCode[0])

dirs = [
    (-1, 0, 0, -cellsize),
    (1, 0, 0, cellsize),
    (0, -1, -cellsize, 0),
    (0, 1, cellsize, 0)
]
dir_bits = {
    (-1, 0): 4,
    (1, 0): 8,
    (0, -1): 1,
    (0, 1): 2
}

sr, sc = startCell
er, ec = endCell

from collections import deque
INF = rows * cols + 1
dist = [[INF]*cols for _ in range(rows)]
queue = deque()
dist[er][ec] = 0
queue.append((er, ec))

while queue:
    r, c = queue.popleft()
    for dr, dc, _, _ in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            # check walls from neighbor to current
            mask = labyrinthCode[nr][nc]
            if mask & dir_bits.get((-dr, -dc), 0):
                continue
            if dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

def can_move(r, c, dr, dc):
    mask = labyrinthCode[r][c]
    if mask & dir_bits[(dr, dc)]:
        return False
    nr, nc = r + dr, c + dc
    return 0 <= nr < rows and 0 <= nc < cols

r, c = sr, sc
canvas.itemconfig(text_ids[r][c], fill="#080")
while (r, c) != (er, ec):
    best = None
    for dr, dc, dx, dy in dirs:
        if not can_move(r, c, dr, dc):
            continue
        nr, nc = r + dr, c + dc
        if dist[nr][nc] < dist[r][c]:
            if best is None or dist[nr][nc] < dist[best[0]][best[1]]:
                best = (nr, nc, dx, dy)
    if best is None:
        print("Stuck, no decreasing neighbor!")
        break
    nr, nc, dx, dy = best
    canvas.move(robot, dx, dy)
    root.update()
    time.sleep(0.1)
    canvas.itemconfig(text_ids[nr][nc], fill="#080")
    x0 = offset2 + c*cellsize + cellsize/2
    y0 = r*cellsize + cellsize/2
    x1 = x0 + dx
    y1 = y0 + dy
    canvas.create_line(x0, y0, x1, y1, fill="green", width=2)
    r, c = nr, nc

root.mainloop()
