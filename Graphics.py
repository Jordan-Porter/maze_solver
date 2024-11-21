from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas: Canvas, fill_colour: str):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_colour, width=2)

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True

        while self.running == True:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line: Line, fill_colour: str):
        line.draw(self.canvas, fill_colour)

class Cell:
    def __init__(self, win: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False
    
    def draw(self, top_left: Point, bottom_right: Point):
        if self._win is None:
            return
        self._x1 = top_left.x
        self._x2 = bottom_right.x
        self._y1 = top_left.y
        self._y2 = bottom_right.y

        if self.has_left_wall:
            l = Line(top_left, Point(top_left.x, bottom_right.y))
            self._win.draw_line(l, "black")
        else:
            l = Line(top_left, Point(top_left.x, bottom_right.y))
            self._win.draw_line(l, "#F0F0F0")
        if self.has_top_wall:
            l = Line(top_left, Point(bottom_right.x, top_left.y))
            self._win.draw_line(l, "black")
        else:
            l = Line(top_left, Point(bottom_right.x, top_left.y))
            self._win.draw_line(l, "#F0F0F0")
        if self.has_right_wall:
            l = Line(Point(bottom_right.x, top_left.y), bottom_right)
            self._win.draw_line(l, "black")
        else:
            l = Line(Point(bottom_right.x, top_left.y), bottom_right)
            self._win.draw_line(l, "#F0F0F0")
        if self.has_bottom_wall:
            l = Line(Point(top_left.x, bottom_right.y), bottom_right)
            self._win.draw_line(l, "black")
        else:
            l = Line(Point(top_left.x, bottom_right.y), bottom_right)
            self._win.draw_line(l, "#F0F0F0")
    
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