
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

for i in range(1,1):
    print(i)
        
        
