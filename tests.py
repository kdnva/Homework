import unittest
from game import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def test_create_board(self):
        board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        tic_tac_toe = TicTacToe()
        tic_tac_toe.create_board()
        res = tic_tac_toe.board
        self.assertEqual(res, board)

    def test_is_player_win(self):
        board = [['x', 'x', 'x'], ['-', '-', '-'], ['-', '-', '-']]
        tic_tac_toe = TicTacToe()
        tic_tac_toe.board = board
        res = tic_tac_toe.is_player_win('x')
        self.assertTrue(res)

        board = [['-', '-', '-'], ['x', 'x', 'x'], ['-', '-', '-']]
        tic_tac_toe.board = board
        res = tic_tac_toe.is_player_win('x')
        self.assertTrue(res)

        board = [['-', '-', '-'], ['-', '-', '-'], ['x', 'x', 'x']]
        tic_tac_toe.board = board
        res = tic_tac_toe.is_player_win('x')
        self.assertTrue(res)

        board = [['x', '-', '-'], ['-', 'x', '-'], ['-', '-', 'x']]
        tic_tac_toe.board = board
        res = tic_tac_toe.is_player_win('x')
        self.assertTrue(res)

        board = [['-', '-', 'x'], ['-', 'x', '-'], ['x', '-', '-']]
        tic_tac_toe.board = board
        res = tic_tac_toe.is_player_win('x')
        self.assertTrue(res)

        board = [['x', '-', 'x'], ['-', '-', '-'], ['-', '-', '-']]
        tic_tac_toe.board = board
        res = tic_tac_toe.is_player_win('x')
        self.assertFalse(res)

        board = [['x', '-', '-'], ['-', '-', '-'], ['-', '-', 'x']]
        tic_tac_toe.board = board
        res = tic_tac_toe.is_player_win('x')
        self.assertFalse(res)

    def test_is_board_filled(self):
        board = [['x', 'x', '-'], ['-', 'O', '-'], ['O', '-', 'O']]
        tic_tac_toe = TicTacToe()
        tic_tac_toe.board = board
        res = tic_tac_toe.is_board_filled()
        self.assertFalse(res)

        board = [['x', 'x', 'O'], ['O', 'O', 'x'], ['O', 'x', 'O']]
        tic_tac_toe.board = board
        res = tic_tac_toe.is_board_filled()
        self.assertTrue(res)
