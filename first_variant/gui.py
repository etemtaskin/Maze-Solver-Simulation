import tkinter

labyrinthCode = [
    [5, 12, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 12, 5],
    [1, 4, 10, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 10, 4, 1],
    [9, 8, 0, 10, 8, 10, 8, 10, 8, 10, 8, 10, 0, 8, 8, 2],
    [3, 0, 9, 0, 9, 0, 2, 0, 2, 0, 9, 0, 10, 0, 0, 2],
    [9, 0, 3, 8, 0, 8, 0, 8, 0, 8, 0, 9, 0, 8, 0, 2],
    [1, 10, 8, 2, 8, 2, 8, 2, 8, 2, 8, 10, 8, 2, 10, 1],
    [9, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2],
    [3, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 10, 0, 0, 2],
    [9, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 8, 2],
    [1, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 0, 2],
    [3, 0, 3, 8, 2, 10, 2, 10, 2, 10, 8, 2, 10, 0, 8, 2],
    [9, 8, 0, 0, 9, 0, 9, 0, 9, 0, 0, 8, 0, 8, 8, 2],
    [1, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 0, 2],
    [3, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 8, 2],
    [1, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 0, 2],
    [9, 12, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 8, 10, 12, 11]
]

startCell = (0, 0)
endCell   = (15, 15)
cellsize  = 20
margin    = 30

def setup():
    global root, canvas, robot, text_ids, offset2
    rows = len(labyrinthCode)
    cols = len(labyrinthCode[0])

    W = cols*cellsize*2 + margin + 2
    H = rows*cellsize + 2

    root = tkinter.Tk()
    root.title("Micromouse Simulation GUI")
    canvas = tkinter.Canvas(root, width=W, height=H, bg="white")
    canvas.pack()

    for r in range(rows):
        for c in range(cols):
            mask = labyrinthCode[r][c]
            x0, y0 = c*cellsize, r*cellsize
            x1, y1 = x0+cellsize, y0+cellsize
            if mask & 4: canvas.create_line(x0, y0, x1, y0) 
            if mask & 8: canvas.create_line(x0, y1, x1, y1)
            if mask & 1: canvas.create_line(x0, y0, x0, y1)
            if mask & 2: canvas.create_line(x1, y0, x1, y1)
    for (r, c) in (startCell, endCell):
        x0 = c*cellsize+1; y0 = r*cellsize+1
        x1 = x0+cellsize-2; y1 = y0+cellsize-2
        canvas.create_rectangle(x0, y0, x1, y1, fill="red", outline="")
    sr, sc = startCell
    gx0 = sc*cellsize+1; gy0 = sr*cellsize+1
    gx1 = gx0+cellsize-2; gy1 = gy0+cellsize-2
    robot = canvas.create_rectangle(gx0, gy0, gx1, gy1, fill="green", outline="")

    offset2 = cols*cellsize + margin
    text_ids = [[None]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            mask = labyrinthCode[r][c]
            x0 = offset2 + c*cellsize
            y0 = r*cellsize
            x1 = x0 + cellsize
            y1 = y0 + cellsize
            if mask & 4: canvas.create_line(x0, y0, x1, y0, fill="#bbb")
            if mask & 8: canvas.create_line(x0, y1, x1, y1, fill="#bbb")
            if mask & 1: canvas.create_line(x0, y0, x0, y1, fill="#bbb")
            if mask & 2: canvas.create_line(x1, y0, x1, y1, fill="#bbb")
            er, ec = endCell
            dist = abs(r-er) + abs(c-ec)
            tx = offset2 + c*cellsize + cellsize/2
            ty = r*cellsize + cellsize/2
            text_ids[r][c] = canvas.create_text(tx, ty, text=str(dist), font=("Arial", 10))

    return root, canvas, robot, text_ids, offset2

if __name__ == "__main__":
    root, canvas, robot, text_ids, offset2 = setup()
    root.mainloop()
