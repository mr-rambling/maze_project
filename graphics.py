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
        self.__canvas = Canvas(self.__window, bg='grey', 
                               height=height, width=width)
        self.__canvas.grid(row=0, column=0, sticky='nsew')
        self.__user_input = tk.Frame(self.__window, borderwidth=5, relief='groove', width=width, height=200)
        self.__user_input.grid(row=1, column=0, columnspan=20)
        self.__running = False
        self.__window.protocol("WM_DELETE_WINDOW", self.close)

        padding = 5
        paddingx= 20
        self._fields = {}
        self._fields['rows_label'] = Label(self.__user_input, text='Rows:', font=('arial',15,'normal'))
        self._fields['rows_label'].grid(row=1, column=0, padx=paddingx, pady=padding)
        self._rows = tk.StringVar(value='20')
        self._fields['rows_entry'] = Entry(self.__user_input, textvariable=self._rows, font=('arial',15,'normal'))
        self._fields['rows_entry'].grid(row=1, column=1, padx=paddingx, pady=padding)

        self._fields['cols_label'] = Label(self.__user_input, text='Columns:', font=('arial',15,'normal'))
        self._fields['cols_label'].grid(row=3, column=0, padx=paddingx, pady=padding)
        self._cols = tk.StringVar(value='20')
        self._fields['cols_entry'] = Entry(self.__user_input, textvariable=self._cols, font=('arial',15,'normal'))
        self._fields['cols_entry'].grid(row=3, column=1, padx=paddingx, pady=padding)

        self._fields['seed_label'] = Label(self.__user_input, text='Seed:', font=('arial',15,'normal'))
        self._fields['seed_label'].grid(row=5, column=0, padx=paddingx, pady=padding)
        self._seed = tk.StringVar()
        self._fields['seed_entry'] = Entry(self.__user_input, textvariable=self._seed, font=('arial',15,'normal'))
        self._fields['seed_entry'].grid(row=5, column=1, padx=paddingx, pady=padding)

        self._buttons = {}
        self._buttons['generate_button'] = Button(self.__user_input, 
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
        self._buttons['solve_button'] = Button(self.__user_input, 
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

    def redraw(self):
        self.__window.update_idletasks()
        self.__window.update()
        self.__user_input.update_idletasks()
        self.__user_input.update()

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

        