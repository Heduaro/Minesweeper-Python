from email import utils
from tkinter import *
import Settings
import Utilities
from Cell import Cell

root = Tk()
# Override window settings
root.configure(bg='gray33')
root.geometry(f'{Settings.WIDTH}x{Settings.HEIGHT}')
root.title("Game of Minesweeper")
root.resizable(False, False)

#frames for dividing window
top_frame = Frame(
    root,
    bg='gray33', #Change to red to see frames
    width= Settings.WIDTH,
    height= Utilities.height_prcnt(25)
)
#place- recives pixel value, 
# start it from(0,0)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='gray33',
    fg='red',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=Utilities.width_prcnt(25), y=0
)

left_frame = Frame(
    root,
    bg='gray33', #change to blue to see frames
    width=Utilities.width_prcnt(25),
    height=Utilities.height_prcnt(75)
)
left_frame.place(x=0, y=Utilities.height_prcnt(25))

#game center frame
center_frame = Frame(
    root,
    bg='gray33', #change to green to see frames
    width=Utilities.width_prcnt(75),
    height=Utilities.height_prcnt(75)
)
#starting from corner of frames (180x180px)
center_frame.place(
    x=Utilities.width_prcnt(25),
    y=Utilities.height_prcnt(25),
)


#Cells
#tkinter button(use it if the other one won't work)
#btn1 = Button(
#   center_frame,
#   bg='blue',
#   text='First Button'
# )
#btn1.place(x=0, y=0)

#proper button
# grid takes parent element and turns it into collumns and rows
#button using nested loops


for x in range(Settings.GRID_SIZE):
    for y in range (Settings.GRID_SIZE):
        c= Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

#Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
    )


#using static method
Cell.randomize_mines()

#Run window
root.mainloop()