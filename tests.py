import unittest
from Maze import Maze

param_list = [(10, 10), (50, 1), (12, 16)]

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        for p1, p2 in param_list:
            with self.subTest(p1=p1, p2=p2):
                num_rows = p1
                num_cols = p2
                m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
                self.assertEqual(
                    len(m1._cells),
                    num_cols
                )
                self.assertEqual(
                    len(m1._cells[0]),
                    num_rows
                )

    def test_break_entrace_and_exit(self):
        num_rows = 12
        num_cols = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()