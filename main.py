from graphics import Window, Line, Point
from cell import Cell
from maze import Maze
import random

def main():
    num_rows = 10
    num_cols = 10
    margin = 20
    screen_x = 800
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows    
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, 
                cell_size_x, cell_size_y, win, seed=1)
    
    win.wait_for_close()

main()