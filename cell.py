from graphics import *
import statistics as stat

class Cell():
    '''
    x1   top-left corner

    y1   top-left corner

    x2   bottom-right corner

    y2   bottom-right corner
    '''
    def __init__(self, win:Window=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._x1 = None   # top-left corner
        self._y1 = None   # top-left corner
        self._x2 = None   # bottom-right corner
        self._y2 = None   # bottom-right corner
        self._win = win
        self.visited = False

    def draw(self):
        # left wall
        if self.left_wall:
            l = Line(Point(self._x1, self._y1), 
                     Point(self._x1, self._y2))
            self._win.draw_line(l, 'black')
        else:
            l = Line(Point(self._x1, self._y1), 
                     Point(self._x1, self._y2))
            self._win.draw_line(l, 'white')
        # right wall               
        if self.right_wall:
            l = Line(Point(self._x2, self._y1), 
                     Point(self._x2, self._y2))
            self._win.draw_line(l, 'black')
        else:
            l = Line(Point(self._x2, self._y1), 
                     Point(self._x2, self._y2))
            self._win.draw_line(l, 'white')  
        # top wall
        if self.top_wall:
            l = Line(Point(self._x1, self._y1), 
                     Point(self._x2, self._y1))
            self._win.draw_line(l, 'black')
        else:
            l = Line(Point(self._x1, self._y1), 
                     Point(self._x2, self._y1))
            self._win.draw_line(l, 'white') 
        # bottom wall
        if self.bottom_wall:
            l = Line(Point(self._x1, self._y2), 
                     Point(self._x2, self._y2))
            self._win.draw_line(l, 'black')
        else:
            l = Line(Point(self._x1, self._y2), 
                     Point(self._x2, self._y2))
            self._win.draw_line(l, 'white')  

    def draw_move(self, to_cell, undo=False):
        color = 'red'
        if undo:
            color = 'gray'
        p1 = Point(stat.mean([self._x1, self._x2]),
                   stat.mean([self._y1, self._y2]))
        p2 = Point(stat.mean([to_cell._x1, to_cell._x2]),
                   stat.mean([to_cell._y1, to_cell._y2]))
        self._win.draw_line(Line(p1,p2), color)