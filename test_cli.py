import unittest
from unittest.mock import patch
from chess import Chess
from cli import play
from cli import OutOfBoardError, InvalidMove

class TestCli(unittest.TestCase):

    @patch("builtins.input", side_effect=['1', '1', '2', '2'])
    @patch("builtins.print")
    def test_valid_move(self, mock_print, mock_input):
        chess = Chess()
        play(chess)
    
        mock_print.assert_any_call("turn: ", chess.turn)

    @patch("builtins.input", side_effect=['-1', '0', '2', '2'])
    @patch("builtins.print")
    def test_out_of_board_move(self, mock_print, mock_input):
        chess = Chess()
        with self.assertRaises(OutOfBoardError):
            play(chess)
        mock_print.assert_called_with("Movimiento fuera de tablero")

    @patch("builtins.input", side_effect=['1', '1', '2', '2'])
    @patch("builtins.print")
    def test_invalid_move(self, mock_print, mock_input):
        chess = Chess()
        with patch.object(Chess, 'move', side_effect=InvalidMove):
            play(chess)

        mock_print.assert_called_with("Movimiento no válido")

if __name__ == '__main__':
    unittest.main()
