WIDTH=1440
HEIGHT=720
GRID_SIZE=7
# FOR BOARD SHOWING MINES LEFT
CELL_COUNT = GRID_SIZE ** 2
#Double slash forces it to be int number so we don't have for example 3,25 mines
MINES_COUNT =(CELL_COUNT) // 4