import unittest

from unittest.mock import patch
from queens import *

N = 8
mock_chessboard = [[" □ " for j in range(N)] for i in range(N)]
SOLUTION = []

class Tests(unittest.TestCase):
    def test_create_chessboard_for_N(self):
        self.assertEqual(create_chessboard(N), mock_chessboard)

    def test_is_collision_false_when_no_queens(self):
        queens = [-1] * N
        self.assertEqual(check_collision(queens, 0, 0), False)
    
    def test_is_collision_true_on_diagonals(self):
        queens = [0, 5, -1, -1, -1, -1, 1, 7]
        self.assertEqual(check_collision(queens, 3, 3), True)

    def test_is_collision_true_on_horizontal(self):
        queens = [-1, 3, -1, -1, -1, 3, -1, -1]
        self.assertEqual(check_collision(queens, 3, 3), True)

    def test_is_8_queens_sollution_92(self):
        sols = []
        queens = [-1 for i in range(8)]
        n_queens(queens, 0, sols)
        self.assertEqual(len(sols), 92)

    def test_is_10_queens_sollution_92(self):
        sols = []
        queens = [-1 for i in range(10)]
        n_queens(queens, 0, sols)
        self.assertEqual(len(sols), 724)

if __name__ == '__main__':
    unittest.main()
