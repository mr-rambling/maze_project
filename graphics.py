from tkinter import Tk, BOTH, Canvas

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
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

class Window():
    def __init__(self, width, height):
        self.__window = Tk()
        self.__window.title = 'Maze Solver'
        self.__canvas = Canvas(self.__window, bg='white', 
                               height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__window.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__window.update_idletasks()
        self.__window.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print('window closed....')

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color):
        line.draw(self.__canvas, fill_color)