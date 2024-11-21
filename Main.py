from Graphics import Window, Cell, Point, Line
from Maze import Maze
import sys

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    seed = 52

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, seed, win)

    maze.solve()

    win.wait_for_close()

# win = Window(800, 600)

# line = Line(Point(0,0), Point(100,100))
# win.draw_line(line, "Black")

# cell = Cell(win)
# cell.draw(Point(150,150), Point(300,300))

# cell2 = Cell(win)
# cell2.draw(Point(500,500), Point(600,600))

# cell.draw_move(cell2, False)

# win.wait_for_close()

main()