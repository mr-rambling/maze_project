from graphics import *
from maze import Maze
import tkinter as tk
import time

class User(Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__screen_x = width
        self.__screen_y = height

    def generate_button(self):
        num_rows = int(self._rows.get())
        num_cols = int(self._cols.get())
        margin = 20
        cell_size_y = (self.__screen_y - 2 * margin) / num_rows
        cell_size_x = (self.__screen_x - 2 * margin) / num_cols
        self.clear()    
        print("It's a new maze!")   
        seed = self._seed.get()
        draw_time = 0
        self.maze = Maze(margin, margin, num_rows, num_cols, 
                cell_size_x, cell_size_y, self, seed=seed, draw_time=draw_time)
        
    def solve_button(self):
        self.maze.reset_moves()
        solve_step_time = 0.00
        time_taken = self.maze.solve(solve_step_time)
        if time_taken != None:
            print(f'Solving took {round(time_taken,5)} seconds')
            return
        print("Maze couldn't be solved")