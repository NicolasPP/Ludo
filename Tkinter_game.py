from tkinter import *


board = Tk()
board.title("Ludo")
board.geometry("1100x1100")
tiles = []


main_frame = Canvas(board,bg = "gray", height = 1050, width = 1050)
main_frame.grid(row = 0, column = 0,columnspan = 3, rowspan = 3)



def move_object(canvas, object_id, destination, speed=50):
    dest_x, dest_y = destination
    coords = canvas.coords(object_id)
    current_x = coords[0]
    current_y = coords[1]

    new_x, new_y = current_x, current_y
    delta_x = delta_y = 0
    if current_x < dest_x:
        delta_x = 1
    elif current_x > dest_x:
        delta_x = -1

    if current_y < dest_y:
        delta_y = 1
    elif current_y > dest_y:
        delta_y = -1

    if (delta_x, delta_y) != (0, 0):
        canvas.move(object_id, delta_x, delta_y)

    if (new_x, new_y) != (dest_x, dest_y):
        canvas.after(speed, move_object, canvas, object_id, destination, speed)


## Creating all the tiles
for i in range(8):
     tiles.append(main_frame.create_rectangle(1000-(i*50),350,1050-(i*50),470, fill = "white"))

for i in range(8):
     tiles.append(main_frame.create_rectangle(580,350-(i*50),700,400-(i*50), fill = "white"))

tiles.append(main_frame.create_rectangle(470,0,580,50, fill = "white"))

for i in range(8):
     tiles.append(main_frame.create_rectangle(350,0+(i*50),470,50+(i*50), fill = "white"))

for i in range(8):
     tiles.append(main_frame.create_rectangle(400-(i*50),350,350-(i*50),470, fill = "white"))

tiles.append(main_frame.create_rectangle(0,470,50,580, fill = "white"))

for i in range(8):
     tiles.append(main_frame.create_rectangle(0+(i*50),580,50+(i*50),700, fill = "white"))

for i in range(8):
     tiles.append(main_frame.create_rectangle(350,650+(i*50),470,700+(i*50), fill = "white"))

tiles.append(main_frame.create_rectangle(470,1000,580,1050, fill = "white"))

for i in range(8):
     tiles.append(main_frame.create_rectangle(580,1050-(i*50),700,1000-(i*50), fill = "white"))

for i in range(8):
     tiles.append(main_frame.create_rectangle(650+(i*50),700,700+(i*50),580, fill = "white"))

tiles.append(main_frame.create_rectangle(1000,470,1050,580, fill = "white"))
## creating all the numbers
for i in range(68):
     if i == 24:
          main_frame.create_text(main_frame.coords(tiles[i])[0]+60,main_frame.coords(tiles[i])[1]+10, text = i+1)
     else:
          main_frame.create_text(main_frame.coords(tiles[i])[0]+10,main_frame.coords(tiles[i])[1]+10, text = i+1)




top_left_rec = main_frame.create_rectangle(0,0,350,350, fill = "blue")
top_right_rec = main_frame.create_rectangle(700,0,1050,350, fill = "Yellow")
bottom_left_rec = main_frame.create_rectangle(0,700,350,1050, fill = "red")
bottom_right_rec = main_frame.create_rectangle(700,700,1050,1050, fill = "green")


## players
blue = []

blue.append(main_frame.create_oval(100,100,135,135,fill = "blue"))
blue.append(main_frame.create_oval(250,250,215,215,fill = "blue"))
blue.append(main_frame.create_oval(250,100,215,135,fill = "blue"))
blue.append(main_frame.create_oval(100,250,135,215,fill = "blue"))

yellow = []
yellow.append(main_frame.create_oval(800,100,835,135,fill = "yellow"))
yellow.append(main_frame.create_oval(950,250,915,215,fill = "yellow"))
yellow.append(main_frame.create_oval(950,100,915,135,fill = "yellow"))
yellow.append(main_frame.create_oval(800,250,835,215,fill = "yellow"))

red = []

red.append(main_frame.create_oval(100,800,135,835,fill = "red"))
red.append(main_frame.create_oval(250,950,215,915,fill = "red"))
red.append(main_frame.create_oval(250,800,215,835,fill = "red"))
red.append(main_frame.create_oval(100,950,135,915,fill = "red"))

green = []

green.append(main_frame.create_oval(800,800,835,835,fill = "green"))
green.append(main_frame.create_oval(950,950,915,915,fill = "green"))
green.append(main_frame.create_oval(950,800,915,835,fill = "green"))
green.append(main_frame.create_oval(800,950,835,915,fill = "green"))


board.mainloop()
