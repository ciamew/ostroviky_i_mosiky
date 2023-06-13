import random
import tkinter as tk

count_w = random.randrange(4,7)
count_h = random.randrange(3,10)

#picture width
pw = 50
#picture height
ph = 50

# w = 400
# h = 550

w = count_w*pw+100
h = count_h*ph

win = tk.Tk()

canvas = tk.Canvas(win,width=w,height=h,bg="grey")
canvas.pack()


img = tk.PhotoImage(file="images/ostrov3.png")
img1 = tk.PhotoImage(file="images/ostrov0.png")
img2 = tk.PhotoImage(file="images/ostrov1.png")
img3 = tk.PhotoImage(file="images/ostrov2.png")
img4 = tk.PhotoImage(file="images/ostrov_kruh0.png")
img5 = tk.PhotoImage(file="images/ostrov_kruh1.png")

water = []
islands = []
money = 0

def setup():
    global water, islands
    for y in range(count_h):
        for x in range(count_w):
            result = random.random()
            # print(result)
            if result >= 0.2:
                water.append(canvas.create_image(pw * x, ph * y, image=img, anchor=tk.NW))
            else:
                islands.append(canvas.create_image(pw * x, ph * y, image=img1, anchor=tk.NW))
    # print(w,h)
    canvas.create_image(w-50, 0, anchor = "nw", image=img4, tags = "switcher")

def changer(e):
    global water, islands, money
    # print("klikkkkk")
    click = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if (len(click)!= 0 and click[0] in water):
        # print("klik vo vode")
        nx = (e.x // pw) *pw
        ny = (e.y // ph) *ph
        temp = click[0]
        canvas.delete(temp)
        water.remove(temp)
        if canvas.itemcget("switcher", "image") == "pyimage5":
            canvas.create_image(nx, ny, anchor="nw", image=img2, tags="bridge")
            money += 10
            paying()
        elif canvas.itemcget("switcher", "image") == "pyimage6":
            canvas.create_image(nx, ny, anchor="nw", image=img1, tags="island")
            money += 50
            paying()

def spinner(e):
    click = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y +1)
    image = canvas.itemcget(click[0],"image")
    print(image)
    if image == "pyimage3":
        canvas.itemconfig(click[0],image=img3)
    if image == "pyimage4":
        canvas.itemconfig(click[0], image=img2)

def island_clicker(e):
    click = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y +1)
    image = canvas.itemcget(click[0],"image")
    print(image)
    if image == "pyimage5":
        canvas.itemconfig(click[0],image=img5)
    if image == "pyimage6":
        canvas.itemconfig(click[0], image=img4)

def paying():
    global money
    canvas.delete("peniaze")
    canvas.create_text(w - 75, 25, text=money, font="Arial 15", tags="peniaze")
    canvas.create_text(w - 75, 8, text="money", font="Arial 7",fill="red")
paying()

canvas.bind("<Button-1>",changer)
canvas.tag_bind("bridge","<Button-1>",spinner)
canvas.tag_bind("switcher","<Button-1>",island_clicker)
setup()

win.mainloop()
