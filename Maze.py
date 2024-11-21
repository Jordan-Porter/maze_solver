from Graphics import Window, Cell, Point
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, seed = None ,win: Window = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        # col = [Cell() for i in range(self.num_rows)]
        # cells = [col for i in range(self.num_cols)]
        # self._cells = cells
        # self._draw_cell(self,)
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i , j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(Point(x1, y1), Point(x2, y2))
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        col = self._num_cols - 1
        row = self._num_rows -1
        self._cells[col][row].has_bottom_wall = False
        self._draw_cell(col, row)
    
    def _break_walls_r(self, i ,j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # determine top
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # determine right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # determine bottom
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
            
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return
            
            direction = random.randrange(len(next_index_list))
            next_index = next_index_list[direction]

            # make path between current cell and next cell
            # break left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # break top
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            # break right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # break bottom
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            
            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        solved = self._solve_r(0, 0)
        return solved

    def _solve_r(self, i, j):        
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # left direction
        if (
            i > 0 
            and self._cells[i][j].has_left_wall == False 
            #and self._cells[i - 1][j].has_right_wall == False 
            and self._cells[i - 1][j].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            solved = self._solve_r(i - 1, j)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo = True)
        # top direction
        if (
            j > 0 
            and self._cells[i][j].has_top_wall == False 
            #and self._cells[i][j - 1].has_bottom_wall == False 
            and self._cells[i][j - 1].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            solved = self._solve_r(i, j - 1)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo = True)
        # right direction
        if (
            i < self._num_cols - 1 
            and self._cells[i][j].has_right_wall == False 
            #and self._cells[i + 1][j].has_left_wall == False 
            and self._cells[i + 1][j].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            solved = self._solve_r(i + 1, j)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo = True)
        # bottom direction
        if (
            j < self._num_rows - 1 
            and self._cells[i][j].has_bottom_wall == False 
            #and self._cells[i][j + 1].has_top_wall == False 
            and self._cells[i][j + 1].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            solved = self._solve_r(i, j + 1)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo = True)

        return False
