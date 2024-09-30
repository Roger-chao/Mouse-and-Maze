import tkinter
from tkinter import messagebox

mx = 0; my = 1
play = 1
x = 0; y = 1
count=0
datax=[0]*10000
datay=[0]*10000

def main_proc():
    global mx, my, datax, datay, play
    canvas.coords("MYCHR", mx*50+25, my*50+25)
    mx=datax[play]
    my=datay[play]
    play=play+1
    if maze[my][mx] == 3 or maze[my][mx] == 2 or maze[my][mx] ==4:
        canvas.create_rectangle(mx*50, my*50, mx*50+49, my*50+49, fill="pink")
    canvas.delete("MYCHR")
    canvas.create_image(mx*50+25, my*50+25, image=img, tag="MYCHR")
    if maze[my][mx] == 3:
        canvas.create_text(375, 375, text='YOU WIN', font=('Arial', 100))
    elif maze[my-1][mx] != 2 and maze[my+1][mx] != 2 and maze[my][mx-1] != 2 and maze[my][mx+1] != 2 and maze[my-1][mx] != 3 and maze[my+1][mx] != 3 and maze[my][mx-1] != 3 and maze[my][mx+1] != 3 and maze[my-1][mx] != 4 and maze[my+1][mx] != 4 and maze[my][mx-1] != 4 and maze[my][mx+1] != 4:
        canvas.create_text(375, 375, text='YOU LOSE', font=('Arial', 100))
    else:root.after(85, main_proc)

root = tkinter.Tk()
root.title("在迷宮之內移動")
canvas = tkinter.Canvas(width=750, height=750, bg="white")
canvas.pack()
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
while(1):
    if maze[y-1][x]==3 or maze[y+1][x]==3 or maze[y][x-1]==3 or maze[y][x+1]==3:
        if maze[y-1][x]==3:
            y=y-1
        elif maze[y+1][x]==3:
            y=y+1
        elif maze[y][x-1]==3:
            x=x-1
        elif maze[y][x+1]==3:
            x=x+1
        count=count+1
        datax[count]=x
        datay[count]=y
        break
    elif maze[y-1][x]==0 or maze[y+1][x]==0 or maze[y][x-1]==0 or maze[y][x+1]==0:
        if maze[y-1][x]==0:
            y=y-1
        elif maze[y][x+1]==0:
            x=x+1
        elif maze[y+1][x]==0:
            y=y+1
        elif maze[y][x-1]==0:
            x=x-1
        count=count+1
        maze[y][x]=2
        datax[count]=x
        datay[count]=y
    else:
        maze[y][x]=4
        if maze[y-1][x]==2:
            y=y-1
        elif maze[y][x+1]==2:
            x=x+1
        elif maze[y+1][x]==2:
            y=y+1
        elif maze[y][x-1]==2:
            x=x-1
        count=count+1
        datax[count]=x
        datay[count]=y
    if count==0:
        canvas.create_text(375, 375, text='No exit', font=('Arial', 100))
        break
for y in range(15):
    for x in range(15):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*50, y*50, x*50+49, y*50+49, fill="skyblue")
canvas.create_rectangle(mx*50, my*50, mx*50+49, my*50+49, fill="pink")
print(count)
for y in range(15):
    print(maze[y])

img = tkinter.PhotoImage(file="nekopower.png")
canvas.create_image(mx*50+25, my*50+25, image=img, tag="MYCHR")
main_proc()
root.mainloop()
