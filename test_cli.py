import unittest
from unittest.mock import patch
from chess import Chess
from cli import *


class TestCli(unittest.TestCase):

    @patch('builtins.input', side_effect=[1, 1, 2, 2])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_valid_move(self, 
    mock_chess_move, 
    mock_print, 
    mock_input
    ):
        chess = Chess()
        play(chess)
    
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 1)
        self.assertEqual(mock_chess_move.call_count, 1)

    @patch("builtins.input", side_effect=[-1, 0, 2, 2])
    @patch("builtins.print")
    @patch.object(Chess, 'move')
    def test_out_of_board_move(
        self, 
        mock_chess_move, 
        mock_print, 
        mock_input
        ):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_chess_move.call_count, 0)


    @patch("builtins.input", side_effect=[1, 1, 2, 2])
    @patch("builtins.print")
    def test_invalid_move(self, mock_print, mock_input):
        chess = Chess()
        with patch.object(Chess, 'move', side_effect=InvalidMove):
            play(chess)

        mock_print.assert_called_with("Movimiento no válido")

if __name__ == '__main__':
    unittest.main()
