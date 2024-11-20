from Window import Window
from Line import Line
from Point import Point

class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, top_left: Point, bottom_right: Point):
        if self._win is None:
            return
        self._x1 = top_left.x
        self._x2 = bottom_right.x
        self._y1 = top_left.y
        self._y2 = bottom_right.y

        if self.has_left_wall:
            l = Line(top_left, Point(top_left.x, bottom_right.y))
            self._win.draw_line(l, "Black")
        if self.has_top_wall:
            l = Line(top_left, Point(bottom_right.x, top_left.y))
            self._win.draw_line(l, "Black")
        if self.has_right_wall:
            l = Line(Point(bottom_right.x, top_left.y), bottom_right)
            self._win.draw_line(l, "Black")
        if self.has_bottom_wall:
            l = Line(Point(top_left.x, bottom_right.y), bottom_right)
            self._win.draw_line(l, "Black")
    
    def draw_move(self, to_cell, undo=False):
        colour = "gray" if undo else "red"
        
        middleSelf = self.middle(
            Point(self._x1, self._y1), 
            Point(self._x2, self._y2))
        middleTo = self.middle(
            Point(to_cell._x1, to_cell._y1), 
            Point(to_cell._x2, to_cell._y2))
        
        l = Line(middleSelf, middleTo)
        
        self._win.draw_line(l, colour)


    def middle(self, p1: Point, p2: Point):
        x = abs(p1.x + p2.x) // 2
        y = abs(p1.y + p2.y) // 2

        return Point(x, y)