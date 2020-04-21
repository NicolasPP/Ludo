from tkinter import *
import random

board = Tk()
board.title("Ludo")
board.geometry("1300x1300")
tiles = []
safe_tiles = [4,11,16,21,28,33,38,45,50,55,62,67]


## color order
yellow_tile_order = {}
blue_tile_order = {}
red_tile_order = {}
green_tile_order ={}
for j in range(1,73):
    yellow_tile_order[j] = j+4

for j in range(1,73):
    if j > 64:
        blue_tile_order[j] = j + 12
    elif j > 47:
        blue_tile_order[j] = (j+21)%68
    else: 
        blue_tile_order[j] = (j+21)%69
for j in range(1,73):
    if j > 64:
        red_tile_order[j] = j + 20
    elif j > 30 :
        red_tile_order[j] = (j+38)%68
    else: 
        red_tile_order[j] = (j+38)%69 
for j in range(1,73):
    if j > 64:
        green_tile_order[j] = j + 28
    elif j > 13 :
        green_tile_order[j] = (j+55)%68
    else: 
        green_tile_order[j] = (j+55)%69
order_list = [yellow_tile_order,blue_tile_order,red_tile_order,green_tile_order]
    
## main frame / menu
main_frame = Canvas(board, bg="gray", height=1050, width=1050)
main_frame.grid(row=0, column=0, columnspan=3, rowspan=3)
menu = Frame(board, height = 100, width = 100, bg = "gray")
menu.grid(row = 0, column = 4, rowspan = 3 , columnspan = 3, sticky = (N,E,S,W))

class Counter:
    def __init__(self,current_tile, current_tile_order, original_position,id_num,can_circle, block):
        self.current_tile = current_tile
        self.current_tile_order = current_tile_order
        self.id_num = id_num
        self.original_position = original_position
        self.can_circle = can_circle
        self.block = block


    def __str__(self):
            return "Counter : %s %s" % (self.id_num, self.current_tile)

    def __repr__(self):
            return str(self)
    def move(self, tile_destination, tile_order_destination):
        if self.current_tile_order == 0:
            self.current_tile_order = 1
        for i in range(self.current_tile_order,tile_order_destination+1):
            if self.block:
                move_object(main_frame,self.can_circle,(main_frame.coords(order_list[players.index(current_player)][i])[0]+20,main_frame.coords(order_list[players.index(current_player)][i])[1]), 15)
            else:
                print(order_list[players.index(current_player)][i])
                move_object(main_frame,self.can_circle,(main_frame.coords(order_list[players.index(current_player)][i])[0],main_frame.coords(order_list[players.index(current_player)][i])[1]), 15)
        block = False
        self.current_tile = tile_destination
        self.current_tile_order = tile_order_destination
    def hui_jia(self):
        self.current_tile = 0
        self.current_tile_order = 0
        move_object(main_frame,self.can_circle,self.original_position, 15)

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


# Creating all the tiles
for i in range(8):
    if i == 4:
        tiles.append(main_frame.create_rectangle(1000 - (i * 50), 350, 1050 - (i * 50), 470, fill="yellow"))
    else:
        tiles.append(main_frame.create_rectangle(1000 - (i * 50), 350, 1050 - (i * 50), 470, fill="white"))

for i in range(8):
    if i == 3:
        tiles.append(main_frame.create_rectangle(580, 350 - (i * 50), 700, 400 - (i * 50), fill="gray"))
    else:    
        tiles.append(main_frame.create_rectangle(580, 350 - (i * 50), 700, 400 - (i * 50), fill="white"))

tiles.append(main_frame.create_rectangle(470, 0, 580, 50, fill="gray"))

for i in range(8):
    if i == 4:
        tiles.append(main_frame.create_rectangle(350, 0 + (i * 50), 470, 50 + (i * 50), fill="blue"))
    else:
        tiles.append(main_frame.create_rectangle(350, 0 + (i * 50), 470, 50 + (i * 50), fill="white"))
        

for i in range(8):
    if i ==  3:
        tiles.append(main_frame.create_rectangle(400 - (i * 50), 350, 350 - (i * 50), 470, fill="gray"))
    else:
        tiles.append(main_frame.create_rectangle(400 - (i * 50), 350, 350 - (i * 50), 470, fill="white"))

tiles.append(main_frame.create_rectangle(0, 470, 50, 580, fill="gray"))

for i in range(8):
    if i == 4:
        tiles.append(main_frame.create_rectangle(0 + (i * 50), 580, 50 + (i * 50), 700, fill="red"))
    else:
        tiles.append(main_frame.create_rectangle(0 + (i * 50), 580, 50 + (i * 50), 700, fill="white"))

for i in range(8):
    if i == 3:
        tiles.append(main_frame.create_rectangle(350, 650 + (i * 50), 470, 700 + (i * 50), fill="gray"))
    else:
        tiles.append(main_frame.create_rectangle(350, 650 + (i * 50), 470, 700 + (i * 50), fill="white"))

tiles.append(main_frame.create_rectangle(470, 1000, 580, 1050, fill="gray"))

for i in range(8):
    if i == 4:
        tiles.append(main_frame.create_rectangle(580,1050-(i*50),700,1000 - (i * 50), fill = "green"))
    else:
        tiles.append(main_frame.create_rectangle(580, 1050 - (i * 50), 700, 1000 - (i * 50), fill="white"))

for i in range(8):
    if i == 3:
        tiles.append(main_frame.create_rectangle(650 + (i * 50), 700, 700 + (i * 50), 580, fill="gray"))
    else:
        tiles.append(main_frame.create_rectangle(650 + (i * 50), 700, 700 + (i * 50), 580, fill="white"))

tiles.append(main_frame.create_rectangle(1000, 470, 1050, 580, fill="gray"))

# yellow house tiles
for i in range(7):
    tiles.append(main_frame.create_rectangle(1000 - (i * 50), 470, 950 - (i * 50), 580, fill="yellow"))
tiles.append(main_frame.create_polygon(650,400,525,525,650,650, fill="yellow", outline = "black"))

# blue house tiles
for i in range(7):
    tiles.append(main_frame.create_rectangle(470,50+ (i * 50),580,100+ (i * 50), fill = "blue"))
tiles.append(main_frame.create_polygon(650,400,525,525,400,400, fill = "blue", outline = "black"))

# red house tiles

for i in range(7):
    tiles.append(main_frame.create_rectangle(50+ (i * 50),470,100+ (i * 50),580, fill = "red"))
tiles.append(main_frame.create_polygon(400,650,525,525,400,400, fill = "red", outline = "black"))

#green house tiles

for i in range(7):
    tiles.append(main_frame.create_rectangle(470,1000- (i * 50),580,950- (i * 50), fill = "green"))

tiles.append(main_frame.create_polygon(400,650,525,525,650,650, fill = "green", outline = "black"))

main_frame.tag_raise(8)

# creating all the numbers
for i in range(68):
    if i == 24:
        main_frame.create_text(main_frame.coords(tiles[i])[0] + 60, main_frame.coords(tiles[i])[1] + 10, text=i + 1)
    else:
        main_frame.create_text(main_frame.coords(tiles[i])[0] + 10, main_frame.coords(tiles[i])[1] + 10, text=i + 1)


# player square


top_left_rec = main_frame.create_rectangle(0, 0, 350, 350, fill="blue")
top_right_rec = main_frame.create_rectangle(700, 0, 1050, 350, fill="Yellow")
bottom_left_rec = main_frame.create_rectangle(0, 700, 350, 1050, fill="red")
bottom_right_rec = main_frame.create_rectangle(700, 700, 1050, 1050, fill="green")

## players
blue = []

blue.append(Counter(0, 0, (100, 100) ,"b1",main_frame.create_oval(100, 100, 135, 135, fill="blue"), block = False))
blue.append(Counter(0, 0, (250, 250) ,"b2",main_frame.create_oval(250, 250, 215, 215, fill="blue"), block = False))
blue.append(Counter(0, 0, (250, 100),"b3",main_frame.create_oval(250, 100, 215, 135, fill="blue"), block = False))
blue.append(Counter(0, 0, (100, 250) ,"b4",main_frame.create_oval(100, 250, 135, 215, fill="blue"), block = False))

yellow = []
yellow.append(Counter(0, 0, (800, 100),"y1",main_frame.create_oval(800, 100, 835, 135, fill="yellow"), block = False))
yellow.append(Counter(0, 0, (950, 250),"y2",main_frame.create_oval(950, 250, 915, 215, fill="yellow"), block = False))
yellow.append(Counter(0, 0, (950, 100),"y3",main_frame.create_oval(950, 100, 915, 135, fill="yellow"), block = False))
yellow.append(Counter(0, 0, (800, 250),"y4",main_frame.create_oval(800, 250, 835, 215, fill="yellow"), block = False))

red = []

red.append(Counter(0, 0, (100, 800),"r1",main_frame.create_oval(100, 800, 135, 835, fill="red"), block = False))
red.append(Counter(0, 0, (250, 950),"r2",main_frame.create_oval(250, 950, 215, 915, fill="red"), block = False))
red.append(Counter(0, 0, (250, 800),"r3",main_frame.create_oval(250, 800, 215, 835, fill="red"), block = False))
red.append(Counter(0, 0, (100, 950),"r4",main_frame.create_oval(100, 950, 135, 915, fill="red"), block = False))

green = []

green.append(Counter(0, 0, (800, 800),"g1",main_frame.create_oval(800, 800, 835, 835, fill="green"), block = False))
green.append(Counter(0, 0, (950, 950),"g2",main_frame.create_oval(950, 950, 915, 915, fill="green"), block = False))
green.append(Counter(0, 0, (950, 800),"g3",main_frame.create_oval(950, 800, 915, 835, fill="green"), block = False))
green.append(Counter(0, 0, (800, 950),"g4",main_frame.create_oval(800, 950, 835, 915, fill="green"), block = False))

# functions
            
def valid_move(counter, dice_roll):
    for i in range (counter.current_tile_order+1,counter.current_tile_order+dice_roll+1):
        for j in players:
            x = 0
            for b in j:                
                if b.current_tile ==  order_list[players.index(current_player)][i]:
                    x += 1
                if x == 2:
                    return False
    
    if counter.current_tile_order+dice_roll > 72:
                return False
    return True

def will_eat(counter,dice_roll):
    for j in players:
        for b in j:
            if order_list[players.index(current_player)][counter.current_tile_order + dice_roll] == b.current_tile:
                    return True
    return False

def will_make_blockade(counter,dice_roll):
    for j in players:
        for b in j:                
            if b in current_player and order_list[players.index(current_player)][counter.current_tile_order + dice_roll] == b.current_tile:
                return True
    return False

players_string = ["yellow","blue","red","green"]
def change_turn():
    global current_player
    c = players.index(current_player)
    current_player = players[(c+1)%4]
    players_string = ["yellow","blue","red","green"]
    turn_label = Label(menu, text = players_string[(c+1)%4], font=("Helvetica", 32), bg = players_string[(c+1)%4])
    turn_label.grid(row = 3, column = 0, sticky = (N,E,S,W))

def eat_player(counter, dice_roll):
    for j in players:
        for b in j:
            if order_list[players.index(current_player)][counter.current_tile_order + dice_roll] == b.current_tile:
                counter.move(b.current_tile, counter.current_tile_order + dice_roll)
                b.hui_jia
                
                
#def form_blockade(counter, dice_roll):
  #  for j in players:
      #  for b in j:                
          #  if order_list[players.index(current_player)][counter.current_tile_order + dice_roll] == b.current_tile:


prevprev = False
prev = False
def dice_roll():
    global a , b, prev , prevprev
    dice.config(state = "disabled")
    a = random.randint(4,5)
    b = random.randint(4,5)
    a = b
    a_l = Label(menu, text = a,font=("Helvetica", 32), bg = "gray")
    a_l.grid(row = 1 ,column = 0,sticky = (N,E,S,W))
    b_l = Label(menu, text = b,font=("Helvetica", 32),bg = "gray")
    b_l.grid(row = 2 ,column = 0,sticky = (N,E,S,W) )
    if a == b:     
        if prevprev and prev:
            current_biggest = current_player[0]
            for i in current_player:
                if i.current_tile_order >= current_biggest.current_tile_order and i.current_tile <= 68:
                    current_biggest = i                                                        
            current_biggest.hui_jia() 
            change_turn()
            prevprev = False
            prev = False
            dice.config(state = "normal")
        else:
            turn()
            prevprev = prev
            prev = True
            dice.config(state = "normal")
    else:
        turn()
        change_turn()
        prevprev = False
        prev = False
        dice.config(state = "normal") 


def turn():
    spaces = 2
    for i in current_player:
        if i.current_tile_order == 1:
            spaces -= 1
    for i in current_player:
        if i.current_tile == 0 and spaces >= 1:
            if (a == 5 and b == 5 ):
                if spaces != 2:
                    i.block = True
                    i.move(5+players.index(current_player)*17,1)
                    spaces -= 1
                else:
                    i.move(5+players.index(current_player)*17,1)
                    spaces -= 1
            elif (a + b) == 5:
                if spaces != 2:
                    i.block = True
                    i.move(5+players.index(current_player)*17,1)
                    brea
                else:
                    i.move(5+players.index(current_player)*17,1)
                    break
            elif (a==5 or b==5):
                if spaces != 2:
                    i.block = True
                    i.move(5+players.index(current_player)*17,1)
                    break
                else:
                    i.move(5+players.index(current_player)*17,1)
                    break         
    
def click(event):
    print("click")    
                    

## dice
dice = Button(menu, text = "roll dice", font=("Helvetica", 32), command = dice_roll, relief = SUNKEN)
dice.grid(row = 0, column = 0,sticky = (N,E,S,W))


current_player = yellow
players = [yellow, blue, red , green]


#buttonBG = main_frame.create_rectangle(350, 350, 450, 450, fill="grey40", outline="grey60")
#buttonTXT = main_frame.create_text(50, 15, text="click")
#main_frame.tag_bind(buttonBG, "<Button-1>", click) ## when the square is clicked runs function "clicked".
#main_frame.tag_bind(buttonTXT, "<Button-1>", click) ## same, but for the text.


board.mainloop()
