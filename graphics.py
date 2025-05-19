from tkinter import Tk, BOTH, Canvas, Button, Entry, Label
import tkinter as tk

class Point():
    def __init__(self, x, y):
        self.x = x      # x=0 is the left of the screen 
        self.y = y      # y=0 is the top of the screen

class Line():
    def __init__(self, pnt1: Point, pnt2: Point):
        self.pnt1 = pnt1
        self.pnt2 = pnt2

    def draw(self, canvas: Canvas, fill_color='black'):
        x1 = self.pnt1.x
        y1 = self.pnt1.y
        x2 = self.pnt2.x
        y2 = self.pnt2.y
        return canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

class Window():
    def __init__(self, width, height):
        self.__window = Tk()
        self.__window.title('Maze Solver')
        self.__window.columnconfigure(0, weight=1)
        self.__window.rowconfigure(0, weight=1)
        self.__running = False
        self.__window.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__window, bg='grey', height=height, width=width)
        self.__canvas.grid(row=0, column=0, sticky='nsew')

        self._user_input = tk.Frame(self.__window, borderwidth=5, relief='groove', width=width, height=200)
        self._user_input.grid(row=1, column=0, columnspan=20)

        self.input()

    def input(self):
        pass

    def redraw(self):
        self.__window.update_idletasks()
        self.__window.update()
        self._user_input.update_idletasks()
        self._user_input.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print('window closed....')

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color):
        return line.draw(self.__canvas, fill_color)

    def clear(self):
        self.__canvas.delete('all')

    def clear_moves(self, moves):
        self.__canvas.delete(moves)
        self.redraw()

    def generate_button(self):
        print("Nothing happened. Write some code!")

    def solve_button(self):
        print("Nothing happened. Write some code!")

        