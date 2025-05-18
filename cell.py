from graphics import Window, Line, Point
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
        self.moves = []
        self.wall_color = 'black'
        self.bg_color = 'grey'
        self.move_color = 'red'
        self.undo_color = 'gray62'

    def draw(self):
        # left wall
        if self.left_wall:
            l = Line(Point(self._x1, self._y1), 
                     Point(self._x1, self._y2))
            self._win.draw_line(l, self.wall_color)
        else:
            l = Line(Point(self._x1, self._y1), 
                     Point(self._x1, self._y2))
            self._win.draw_line(l, self.bg_color)
        # right wall               
        if self.right_wall:
            l = Line(Point(self._x2, self._y1), 
                     Point(self._x2, self._y2))
            self._win.draw_line(l, self.wall_color)
        else:
            l = Line(Point(self._x2, self._y1), 
                     Point(self._x2, self._y2))
            self._win.draw_line(l, self.bg_color)  
        # top wall
        if self.top_wall:
            l = Line(Point(self._x1, self._y1), 
                     Point(self._x2, self._y1))
            self._win.draw_line(l, self.wall_color)
        else:
            l = Line(Point(self._x1, self._y1), 
                     Point(self._x2, self._y1))
            self._win.draw_line(l, self.bg_color) 
        # bottom wall
        if self.bottom_wall:
            l = Line(Point(self._x1, self._y2), 
                     Point(self._x2, self._y2))
            self._win.draw_line(l, self.wall_color)
        else:
            l = Line(Point(self._x1, self._y2), 
                     Point(self._x2, self._y2))
            self._win.draw_line(l, self.bg_color)  

    def draw_move(self, to_cell, undo=False):
        color = self.move_color
        if undo:
            color = self.undo_color
        p1 = Point(stat.mean([self._x1, self._x2]),
                   stat.mean([self._y1, self._y2]))
        p2 = Point(stat.mean([to_cell._x1, to_cell._x2]),
                   stat.mean([to_cell._y1, to_cell._y2]))
        self.moves.append(self._win.draw_line(Line(p1,p2), color))

    def clear_moves(self):
        for move in self.moves:
            self._win.clear_moves(move)