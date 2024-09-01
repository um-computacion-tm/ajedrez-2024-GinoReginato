import unittest
from horse import Horse
from piece import Piece

class TestHorse(unittest.TestCase):

    def test_movimientos_en_tablero_vacio(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        horse = Horse('White')
        actual_position = (4, 4)
        
        movimientos = horse.ValidMoves(actual_position, board)
        
        self.assertIn((6, 5), movimientos)
        self.assertIn((3, 2), movimientos)

    def test_movimientos_con_pieza_enemiga(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        horse = Horse('White')
        actual_position = (4, 4)
        board[6][5] = Piece('Black')

        movimientos = horse.ValidMoves(actual_position, board)
        
        self.assertIn((6, 5), movimientos)

if __name__ == "__main__":
    unittest.main()
