import tkinter as tk

labyrinth=[[7, 5, 12, 12, 6, 7, 5, 12, 12, 4, 6, 5, 6, 5, 6, 5, 12, 12, 12, 12, 12, 12, 6, 13, 12, 12, 12, 4, 6, 13, 4, 6], [3, 9, 6, 7, 3, 3, 9, 12, 6, 3, 9, 10, 3, 3, 9, 10, 13, 12, 4, 14, 5, 6, 9, 6, 5, 12, 6, 3, 9, 12, 10, 3], [9, 12, 10, 1, 10, 9, 12, 12, 10, 9, 6, 7, 9, 10, 5, 6, 5, 12, 2, 5, 10, 9, 6, 3, 9, 6, 9, 10, 5, 6, 7, 3], [5, 4, 14, 3, 5, 12, 12, 12, 12, 12, 10, 1, 12, 12, 2, 9, 2, 13, 10, 3, 13, 6, 3, 9, 6, 9, 6, 5, 10, 3, 3, 3], [3, 9, 12, 10, 3, 13, 12, 12, 4, 12, 12, 10, 7, 5, 10, 7, 3, 5, 12, 10, 5, 10, 1, 14, 9, 6, 3, 9, 6, 3, 9, 2], [3, 5, 12, 4, 10, 5, 12, 6, 1, 12, 12, 12, 10, 1, 6, 9, 10, 3, 5, 12, 10, 5, 10, 5, 12, 10, 3, 5, 10, 9, 6, 3], [3, 9, 14, 9, 4, 10, 5, 10, 11, 5, 12, 12, 6, 11, 3, 5, 12, 10, 1, 12, 6, 9, 12, 10, 5, 12, 2, 9, 6, 5, 10, 3], [9, 12, 12, 6, 3, 5, 10, 5, 12, 10, 5, 6, 9, 12, 2, 3, 5, 6, 3, 5, 2, 5, 6, 13, 10, 5, 10, 5, 10, 3, 5, 10], [7, 5, 6, 3, 11, 9, 6, 1, 12, 12, 10, 3, 13, 4, 10, 3, 3, 3, 11, 3, 9, 10, 9, 12, 6, 3, 5, 10, 5, 10, 9, 6], [1, 10, 3, 3, 5, 12, 10, 3, 5, 12, 6, 9, 6, 3, 7, 3, 3, 9, 12, 10, 5, 12, 4, 14, 3, 3, 3, 5, 10, 13, 4, 10], [11, 5, 2, 3, 9, 6, 7, 1, 10, 13, 10, 5, 10, 9, 2, 3, 9, 6, 5, 6, 9, 6, 9, 6, 3, 3, 3, 9, 12, 6, 9, 14], [5, 10, 11, 3, 5, 10, 3, 3, 5, 12, 12, 10, 5, 12, 10, 9, 12, 10, 3, 9, 6, 9, 6, 9, 10, 3, 9, 4, 14, 9, 12, 6], [3, 5, 6, 9, 10, 13, 8, 10, 3, 7, 5, 6, 9, 6, 7, 5, 12, 4, 10, 7, 3, 7, 3, 13, 6, 1, 6, 3, 5, 12, 12, 2], [9, 10, 1, 6, 13, 4, 12, 4, 10, 9, 10, 1, 6, 9, 2, 3, 7, 3, 13, 8, 2, 3, 9, 6, 1, 10, 9, 10, 3, 5, 12, 10], [5, 6, 3, 9, 12, 10, 5, 10, 5, 12, 6, 3, 11, 5, 10, 3, 3, 3, 5, 6, 1, 10, 5, 10, 9, 12, 14, 5, 10, 9, 12, 14], [3, 9, 10, 7, 5, 12, 10, 5, 10, 7, 3, 1, 12, 10, 5, 10, 3, 3, 3, 3, 11, 5, 10, 13, 4, 12, 6, 1, 12, 6, 5, 6], [1, 12, 6, 9, 8, 12, 14, 3, 5, 2, 3, 9, 12, 6, 9, 12, 2, 9, 10, 9, 12, 10, 5, 12, 10, 5, 10, 9, 14, 9, 10, 3], [9, 14, 3, 5, 12, 12, 6, 9, 10, 3, 3, 5, 6, 11, 5, 12, 10, 5, 6, 13, 4, 12, 10, 5, 12, 10, 5, 12, 6, 5, 12, 2], [5, 12, 10, 3, 7, 5, 8, 12, 6, 3, 9, 10, 9, 6, 9, 12, 12, 10, 9, 6, 3, 5, 14, 3, 13, 4, 10, 5, 10, 1, 6, 11], [1, 12, 6, 3, 3, 3, 7, 5, 10, 3, 5, 12, 6, 1, 12, 14, 5, 12, 6, 9, 10, 3, 5, 10, 5, 10, 5, 10, 5, 10, 9, 6], [3, 7, 3, 1, 10, 3, 1, 10, 5, 10, 1, 6, 11, 9, 12, 12, 8, 14, 9, 4, 12, 2, 9, 6, 3, 5, 10, 13, 10, 5, 6, 3], [3, 3, 9, 10, 5, 10, 3, 7, 3, 5, 10, 9, 4, 6, 5, 4, 14, 5, 6, 11, 5, 2, 7, 9, 10, 9, 12, 12, 12, 10, 9, 2], [3, 1, 4, 14, 3, 5, 8, 10, 3, 3, 5, 12, 10, 3, 11, 3, 5, 10, 9, 6, 3, 3, 9, 12, 4, 12, 12, 4, 12, 12, 6, 3], [3, 3, 3, 5, 10, 9, 6, 5, 10, 11, 9, 12, 6, 3, 5, 10, 9, 6, 13, 8, 10, 9, 12, 6, 9, 6, 7, 9, 6, 5, 10, 3], [3, 11, 3, 9, 12, 6, 11, 3, 5, 12, 12, 12, 10, 9, 2, 5, 12, 10, 5, 12, 6, 13, 12, 8, 6, 9, 8, 14, 3, 9, 14, 3], [3, 5, 2, 13, 6, 9, 12, 10, 9, 4, 12, 6, 13, 12, 10, 9, 12, 6, 9, 6, 3, 5, 12, 6, 9, 6, 5, 6, 9, 6, 5, 10], [9, 10, 9, 6, 1, 12, 6, 5, 6, 9, 14, 9, 12, 12, 6, 5, 12, 8, 14, 3, 9, 10, 7, 9, 6, 9, 10, 9, 6, 3, 3, 7], [13, 12, 6, 9, 10, 7, 3, 3, 9, 12, 12, 6, 5, 12, 2, 9, 12, 12, 12, 10, 13, 12, 8, 6, 9, 6, 13, 4, 10, 3, 9, 2], [5, 12, 10, 5, 12, 2, 3, 9, 6, 5, 6, 9, 10, 5, 10, 7, 5, 12, 4, 12, 12, 12, 6, 9, 6, 9, 6, 9, 12, 10, 5, 10], [1, 12, 6, 3, 7, 3, 9, 12, 10, 11, 1, 6, 5, 10, 13, 8, 10, 5, 10, 5, 12, 14, 9, 6, 1, 14, 3, 5, 12, 6, 3, 7], [3, 7, 9, 10, 3, 1, 12, 12, 12, 12, 10, 11, 3, 13, 4, 6, 5, 10, 5, 10, 5, 12, 12, 10, 3, 5, 10, 9, 6, 3, 9, 2], [9, 8, 12, 12, 10, 9, 12, 12, 12, 12, 12, 12, 8, 12, 10, 9, 10, 13, 8, 12, 8, 12, 12, 12, 10, 9, 12, 12, 10, 9, 12, 10]]
cell=10
rows,cols=len(labyrinth),len(labyrinth[0])
m,g=10,30
W=m*2+cols*cell*2+g
H=m*3+rows*cell*2

root=tk.Tk()
root.title("Labytrinth Algorythim")
C=tk.Canvas(root,width=W,height=H,bg="white")
C.pack()

orig_bits=[[format(v,"04b") for v in row] for row in labyrinth]
wall_ids={name:[[{} for _ in range(cols)] for _ in range(rows)] for name in("original","filled","empty")}
filled_state=[[{s:True for s in("top","bottom","left","right")} for _ in range(cols)] for _ in range(rows)]
empty_state=[[{s:False for s in("top","bottom","left","right")} for _ in range(cols)] for _ in range(rows)]
offs={"original":(m,m),"numbered":(m+cols*cell+g,m),"filled":(m,m+rows*cell+g),"empty":(m+cols*cell+g,m+rows*cell+g)}
text_ids={"filled":[[None]*cols for _ in range(rows)],"empty":[[None]*cols for _ in range(rows)]}
history_filled=[]
history_empty=[]

def draw_cell_walls(i,j,bits,region):
    x0,y0=offs[region]
    x,y=x0+j*cell,y0+i*cell
    corners={"top":((x,y),(x+cell,y)),"bottom":((x,y+cell),(x+cell,y+cell)),"left":((x,y),(x,y+cell)),"right":((x+cell,y),(x+cell,y+cell))}
    d={}

    for side,bitpos in [("bottom",0),("top",1),("right",2),("left",3)]:
        if bits[bitpos]=="1":
            a,b=corners[side]
            d[side]=C.create_line(a,b)
    wall_ids[region][i][j]=d

for i in range(rows):
    for j in range(cols):
        draw_cell_walls(i,j,orig_bits[i][j],"original")

for i in range(rows):
    for j in range(cols):
        x0,y0=offs["numbered"]
        C.create_text(x0+j*cell+cell/2,y0+i*cell+cell/2,text=str(labyrinth[i][j]),font=("Arial",max(int(cell*0.4),8)),fill="blue")

for i in range(rows):
    for j in range(cols):
        draw_cell_walls(i,j,"1111","filled")
        wall_ids["empty"][i][j]={}

for name in("filled","empty"):
    for i in range(rows):
        for j in range(cols):
            x0,y0=offs[name]
            tx,ty=x0+j*cell+cell/2,y0+i*cell+cell/2
            text_ids[name][i][j]=C.create_text(tx,ty,text=str(15 if name=="filled" else 0),font=("Arial",max(int(cell*0.4),8)),fill="green")

pi,pj=0,0
player_ids={}
r=cell/4

for region in offs:
    x0,y0=offs[region]
    player_ids[region]=C.create_oval(x0+pj*cell+cell/2-r,y0+pi*cell+cell/2-r,x0+pj*cell+cell/2+r,y0+pi*cell+cell/2+r,fill="red",outline="")

def update_text(i,j,name):
    bits=[ '1' if (filled_state if name=="filled" else empty_state)[i][j][s] else '0' for s in("bottom","top","right","left")]
    C.itemconfigure(text_ids[name][i][j],text=str(int(''.join(bits),2)))

def record_history():
    history_filled.append([[int(''.join('1' if filled_state[i][j][s] else '0' for s in("bottom","top","right","left")),2) for j in range(cols)] for i in range(rows)])
    history_empty.append([[int(''.join('1' if empty_state[i][j][s] else '0' for s in("bottom","top","right","left")),2) for j in range(cols)] for i in range(rows)])

def move(dx,dy):
    global pi,pj
    i,j=pi,pj
    bits=orig_bits[i][j]
    if dx==0 and dy==-1 and bits[1]=="1":return
    if dx==0 and dy==1 and bits[0]=="1":return
    if dx==-1 and dy==0 and bits[3]=="1":return
    if dx==1 and dy==0 and bits[2]=="1":return
    ni,nj=i+dy,j+dx
    if not(0<=ni<rows and 0<=nj<cols):return
    pi,pj=ni,nj

    for region,pid in player_ids.items():
        ox,oy=offs[region]
        C.coords(pid,ox+pj*cell+cell/2-r,oy+pi*cell+cell/2-r,ox+pj*cell+cell/2+r,oy+pi*cell+cell/2+r)

    for side,bitpos,di,dj in [("bottom",0,1,0),("top",1,-1,0),("right",2,0,1),("left",3,0,-1)]:
        opp={"bottom":"top","top":"bottom","right":"left","left":"right"}[side]
        if orig_bits[pi][pj][bitpos]=="0":
            if filled_state[pi][pj][side]:
                wid=wall_ids["filled"][pi][pj].get(side)
                if wid:C.itemconfigure(wid,state="hidden")
                filled_state[pi][pj][side]=False
                update_text(pi,pj,"filled")

            ni2,nj2=pi+di,pj+dj
            if 0<=ni2<rows and 0<=nj2<cols and filled_state[ni2][nj2][opp]:
                wid2=wall_ids["filled"][ni2][nj2].get(opp)
                if wid2:C.itemconfigure(wid2,state="hidden")
                filled_state[ni2][nj2][opp]=False
                update_text(ni2,nj2,"filled")

        else:
            x0,y0=offs["empty"]
            x,y=x0+pj*cell,y0+pi*cell
            corners_self={"top":((x,y),(x+cell,y)),"bottom":((x,y+cell),(x+cell,y+cell)),"left":((x,y),(x,y+cell)),"right":((x+cell,y),(x+cell,y+cell))}
            if not empty_state[pi][pj][side]:
                a,b=corners_self[side]
                wall_ids["empty"][pi][pj][side]=C.create_line(a,b)
                empty_state[pi][pj][side]=True
                update_text(pi,pj,"empty")
            ni2,nj2=pi+di,pj+dj

            if 0<=ni2<rows and 0<=nj2<cols:
                x2,y2=x0+nj2*cell,y0+ni2*cell
                corners_nb={"top":((x2,y2),(x2+cell,y2)),"bottom":((x2,y2+cell),(x2+cell,y2+cell)),"left":((x2,y2),(x2,y2+cell)),"right":((x2+cell,y2),(x2+cell,y2+cell))}
                
                if not empty_state[ni2][nj2][opp]:
                    a2,b2=corners_nb[opp]
                    wall_ids["empty"][ni2][nj2][opp]=C.create_line(a2,b2)
                    empty_state[ni2][nj2][opp]=True
                    update_text(ni2,nj2,"empty")
    record_history()
