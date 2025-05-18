from cell import Cell
from graphics import *
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols,
                 cell_size_x, cell_size_y, win:Window=None,
                 seed=None, draw_time=0.01):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: list[list[Cell]] = []
        if seed:
            random.seed(seed)
        self.__draw_time = draw_time

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for col in range(self._num_cols):
            col_cells = []
            for row in range(self._num_rows):
                cell = Cell(self._win)
                cell._x1 = self._x1 + col * self._cell_size_x
                cell._y1 = self._y1 + row * self._cell_size_y
                cell._x2 = cell._x1 + self._cell_size_x
                cell._y2 = cell._y1 + self._cell_size_y                
                col_cells.append(cell)
            self._cells.append(col_cells)

        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self._win is None:
            return
        self._cells[col][row].draw()
        self._animate_maze()

    def _animate_maze(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(self.__draw_time)

    def _animate_solver(self, t):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(t)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)

    def _break_walls_r(self, col, row):
        self._cells[col][row].visited = True

        while True:
            visit = []

            # Check which cell(s) to visit next
            # left
            if col > 0 and not self._cells[col-1][row].visited:
                visit.append([col-1,row])
            # right
            if col < self._num_cols-1 and not self._cells[col+1][row].visited:
                visit.append([col+1,row])   
            # up
            if row > 0 and not self._cells[col][row-1].visited:
                visit.append([col,row-1])   
            # down
            if row < self._num_rows-1 and not self._cells[col][row+1].visited:
                visit.append([col,row+1])              

            # return if nowhere to go
            if visit == []:
                self._draw_cell(col,row)
                return
            
            next = random.choice(visit)

            # delete walls between this cell and next
            # left
            if next[0] == col - 1:
                self._cells[col][row].left_wall = False
                self._cells[col-1][row].right_wall = False
            # right
            if next[0] == col + 1:
                self._cells[col][row].right_wall = False
                self._cells[col+1][row].left_wall = False
            # up
            if next[1] == row - 1:
                self._cells[col][row].top_wall = False
                self._cells[col][row-1].bottom_wall = False
            # down
            if next[1] == row + 1:
                self._cells[col][row].bottom_wall = False
                self._cells[col][row+1].top_wall = False

            self._break_walls_r(next[0],next[1])

    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].visited = False

    def solve(self,t):
        start = time.time()
        solved = self._solve_r(0,0,t)
        end = time.time()
        if solved:
            print('Maze solved!')
            return end - start
        print('Maze not solved :(')

    def reset_moves(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].clear_moves()
        self._reset_cells_visited()

    def _solve_r(self,col,row,t):
        self._animate_solver(t)
        self._cells[col][row].visited = True
        if col == self._num_cols-1 and row == self._num_rows-1: 
            return True
        
        # left
        if (col - 1 >= 0 and not self._cells[col][row].left_wall 
            and not self._cells[col-1][row].visited):
                to_cell = self._cells[col-1][row]
                self._cells[col][row].draw_move(to_cell)
                if self._solve_r(col-1,row,t):
                    return True
                self._cells[col][row].draw_move(to_cell,undo=True)               
        # right
        if (col + 1 < self._num_cols and not self._cells[col][row].right_wall
             and not self._cells[col+1][row].visited):
                to_cell = self._cells[col+1][row]
                self._cells[col][row].draw_move(to_cell)
                if self._solve_r(col+1,row,t):
                    return True
                self._cells[col][row].draw_move(to_cell,undo=True)  
        # up
        if (row - 1 >= 0 and not self._cells[col][row].top_wall 
            and not self._cells[col][row-1].visited):
                to_cell = self._cells[col][row-1]
                self._cells[col][row].draw_move(to_cell)
                if self._solve_r(col,row-1,t):
                    return True
                self._cells[col][row].draw_move(to_cell,undo=True)  
        # down
        if (row + 1 < self._num_rows and not self._cells[col][row].bottom_wall 
            and not self._cells[col][row+1].visited):
                to_cell = self._cells[col][row+1]
                self._cells[col][row].draw_move(to_cell)
                if self._solve_r(col,row+1,t):
                    return True
                self._cells[col][row].draw_move(to_cell,undo=True)

        return False  

