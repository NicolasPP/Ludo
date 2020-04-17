from tkinter import *
from tkinter import ttk

board = Tk()
board.title("Ludo")
board.geometry("1100x1100")
tiles = []


main_frame = Canvas(board,bg = "gray", height = 1050, width = 1050)
main_frame.grid(row = 0, column = 0,columnspan = 3, rowspan = 3)


#def coords_converter(coords):


for i in range(8):
     tiles.append(main_frame.create_rectangle(1000-(i*50),350,1050-(i*50),470, fill = "white"))
     main_frame.create_text(main_frame.coords(tiles[i])[0]+20,main_frame.coords(tiles[i])[1]+20, text = i+1)

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
print(main_frame.coords(1))
print(tiles)

top_left_rec = main_frame.create_rectangle(0,0,350,350, fill = "blue")
top_right_rec = main_frame.create_rectangle(700,0,1050,350, fill = "Yellow")
bottom_left_rec = main_frame.create_rectangle(0,700,350,1050, fill = "red")
bottom_right_rec = main_frame.create_rectangle(700,700,1050,1050, fill = "green")


board.mainloop()
