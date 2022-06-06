from tkinter import Button, Label
import random
from tkinter.messagebox import NO
from typing import Text
import Settings
import ctypes
import sys

#button instance that belongs to each cell object

#x and y in class takes values from board not from game window

class Cell:
    all = []
    cell_count = Settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x= x
        self.y = y

        #Append the object to the Cell.all list
        Cell.all.append(self)



#width and height = cells size
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,

        )
        #Button events (right click and left click)
        #bind prints when we for example left click
        #<Button-1> is left click   <Button-3> is right click
        btn.bind('<Button-1>', self.left_click_action) #Left Click
        btn.bind('<Button-3>', self.right_click_action) #Right Click
        #help to customize button after assign button object
        self.cell_btn_object = btn

    #the label cant be instance method cause its 1 time method to call throughout the game
    #this has to be static

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='gray33',
            fg= 'red',
            text=f"Cells Left: {Cell.cell_count}",
            font=("", 30)

        )
        Cell.cell_count_label_object = lbl


    #event helps left_click_action with typeerror
    #adding in else automatic click of surrounding cells in case of value 0
    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()

        else:
            if self.cells_surrounding_mines_lenght == 0:
                for cell_obj in self.cells_surrounding:
                    cell_obj.show_cell()
            self.show_cell()
            #If Mines count is equal to the cells left count, player won
            if Cell.cell_count == Settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'Game Over', 0)



        #Cancel Left and Right click events if cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')


#Return a cell object based on the value of x,y
    def get_cell_by_axis(self, x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell


    @property
    def cells_surrounding(self):
        cells = [
            self.get_cell_by_axis(self.x -1, self.y -1),
            self.get_cell_by_axis(self.x -1, self.y),
            self.get_cell_by_axis(self.x -1, self.y +1),
            self.get_cell_by_axis(self.x, self.y -1),
            self.get_cell_by_axis(self.x +1, self.y -1),
            self.get_cell_by_axis(self.x +1, self.y),
            self.get_cell_by_axis(self.x +1, self.y +1),
            self.get_cell_by_axis(self.x, self.y +1)
        ]
        
#getting rid of none cells in circuit
        cells = [cell for cell in cells if cell is not None]
        return cells

#identifying which surrounding cell is mine
    @property
    def cells_surrounding_mines_lenght(self):
        counter = 0
        for cell in self.cells_surrounding:
            if cell.is_mine:
                counter += 1

        return counter
        
#checking surrounding cells
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.cells_surrounding_mines_lenght)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                        text=f"Cells Left: {Cell.cell_count}"
                    )

                #If this was a mine candidate, then for safety, we should
                #configure the background color to SystemButtonFace
                self.cell_btn_object.configure(
                    bg="SystemButtonFace"
                )

        #Mark the cell as opened (Use is as the last line of this method)
        self.is_opened = True

#player loosing info
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        #exiting game after loosing
        sys.exit()





    def right_click_action(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False 


    #creating mines
    @staticmethod
    def randomize_mines():
        #sample takes elements from list and the amount to be randomized
        picked_cells = random.sample(
            Cell.all, Settings.MINES_COUNT

        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True


#repr is representing real names for each of object
    def __repr__(self):
        return f"Cell({self.x},{self.y})"
