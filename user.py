from graphics import *
from maze import Maze
import tkinter as tk

class User(Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.__screen_x = width
        self.__screen_y = height

    def input(self):
        padding = 5
        paddingx= 20
        self._fields = {}
        self._fields['rows_label'] = Label(self._user_input, text='Rows:', font=('arial',15,'normal'))
        self._fields['rows_label'].grid(row=1, column=0, padx=paddingx, pady=padding)
        self._rows = tk.StringVar(value='20')
        self._fields['rows_entry'] = Entry(self._user_input, textvariable=self._rows, font=('arial',15,'normal'))
        self._fields['rows_entry'].grid(row=1, column=1, padx=paddingx, pady=padding)

        self._fields['cols_label'] = Label(self._user_input, text='Columns:', font=('arial',15,'normal'))
        self._fields['cols_label'].grid(row=3, column=0, padx=paddingx, pady=padding)
        self._cols = tk.StringVar(value='20')
        self._fields['cols_entry'] = Entry(self._user_input, textvariable=self._cols, font=('arial',15,'normal'))
        self._fields['cols_entry'].grid(row=3, column=1, padx=paddingx, pady=padding)

        self._fields['seed_label'] = Label(self._user_input, text='Seed:', font=('arial',15,'normal'))
        self._fields['seed_label'].grid(row=5, column=0, padx=paddingx, pady=padding)
        self._seed = tk.StringVar()
        self._fields['seed_entry'] = Entry(self._user_input, textvariable=self._seed, font=('arial',15,'normal'))
        self._fields['seed_entry'].grid(row=5, column=1, padx=paddingx, pady=padding)

        self._buttons = {}
        self._buttons['generate_button'] = Button(self._user_input, 
                   text="Generate Maze", 
                   command=self.generate_button,
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   justify="center",
                   overrelief="raised",
                   font=('arial',15,'normal'),
                   width=30)
        self._buttons['generate_button'].grid(row=1, column=2, padx=paddingx, pady=padding)
        self._buttons['solve_button'] = Button(self._user_input, 
                   text="Solve Maze", 
                   command=self.solve_button,
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   justify="center",
                   overrelief="raised",
                   font=('arial',15,'normal'),
                   width=30)
        self._buttons['solve_button'].grid(row=3, column=2, padx=paddingx, pady=padding)        

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
        solve_step_time = 0.005
        time_taken = self.maze.solve(solve_step_time)
        if time_taken != None:
            print(f'Solving took {round(time_taken,5)} seconds')
            return
        print("Maze couldn't be solved")