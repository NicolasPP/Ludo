from tkinter import *
from tkinter import ttk

board = Tk()
board.title("Ludo")



main_frame = Frame(board,bg = "black", height = 900 , width = 900).grid(row = 0, column = 0,columnspan = 3, rowspan = 3)


top_left = Frame(main_frame, bg = "blue",height = 300 , width = 300)
top_left.grid(row = 0 ,column = 0,columnspan = 1,rowspan = 1, sticky = (N,W,E,S))
top_middle = Frame(main_frame, bg = "gray",height = 300 , width = 300)
top_middle.grid(row = 0 ,column = 1,columnspan = 1,rowspan = 1, sticky = (N,W,E,S))
top_right = Frame(main_frame, bg = "yellow",height = 300 , width = 300)
top_right.grid(row = 0 ,column = 2,columnspan = 1,rowspan = 1, sticky = (N,W,E,S))


middle_left = Frame(main_frame, bg = "gray",height = 300 , width = 300)
middle_left.grid(row = 1 ,column = 0,columnspan = 1,rowspan = 1, sticky = (N,W,E,S))
middle_middle = Frame(main_frame, bg = "gray",height = 300 , width = 300)
middle_middle.grid(row = 1 ,column = 1,columnspan = 1,rowspan = 1, sticky = (N,W,E,S))
middle_right = Frame(main_frame, bg = "gray",height = 300 , width = 300)
middle_right.grid(row = 1 ,column = 2,columnspan = 1,rowspan = 1, sticky = (N,W,E,S))

bottom_left = Frame(main_frame, bg = "red",height = 300 , width = 300)
bottom_left.grid(row = 2 ,column = 0,columnspan = 1,rowspan = 1, sticky = (N,W,E,S))
bottom_middle = Frame(main_frame, bg = "gray",height = 300 , width = 300)
bottom_middle.grid(row = 2 ,column = 1,columnspan = 1,rowspan = 1, sticky = (N,W,E,S))
bottom_right = Frame(main_frame, bg = "green",height = 300 , width = 300)
bottom_right.grid(row = 2 ,column = 2,columnspan = 1,rowspan = 1, sticky = (N,W,E,S))


can_top_left = Canvas(top_left,highlightbackground="black", bg = "blue",height = 300 , width = 300)
can_top_left.grid(row = 0 , column = 0,sticky = (N,W,E,S))
can_top_middle = Canvas(top_middle,highlightbackground="black", bg = "gray",height = 300 , width = 300)
can_top_middle.grid(row = 0 , column = 0,sticky = (N,W,E,S))
can_top_right = Canvas(top_right,highlightbackground="black", bg = "yellow",height = 300 , width = 300)
can_top_right.grid(row = 0 , column = 0,sticky = (N,W,E,S))

can_middle_left = Canvas(middle_left,highlightbackground="black", bg = "gray",height = 300 , width = 300)
can_middle_left.grid(row = 0 , column = 0,sticky = (N,W,E,S))
can_middle_middle = Canvas(middle_middle,highlightbackground="black", bg = "gray",height = 300 , width = 300)
can_middle_middle.grid(row = 0 , column = 0,sticky = (N,W,E,S))
can_middle_right = Canvas(middle_right,highlightbackground="black", bg = "gray",height = 300 , width = 300)
can_middle_right.grid(row = 0 , column = 0,sticky = (N,W,E,S))

can_bottom_left = Canvas(bottom_left,highlightbackground="black", bg = "red",height = 300 , width = 300)
can_bottom_left.grid(row = 0 , column = 0,sticky = (N,W,E,S))
can_bottom_middle = Canvas(bottom_middle,highlightbackground="black", bg = "gray",height = 300 , width = 300)
can_bottom_middle.grid(row = 0 , column = 0,sticky = (N,W,E,S))
can_bottom_right = Canvas(bottom_right,highlightbackground="black", bg = "green",height = 300 , width = 300)
can_bottom_right.grid(row = 0 , column = 0,sticky = (N,W,E,S))


## players
#can_top_left.create_oval()


board.mainloop()
