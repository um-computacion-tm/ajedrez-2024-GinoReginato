import unittest
from bishop import Bishop
from piece import Piece

class TestBishop(unittest.TestCase):

    def test_movimientos_en_tablero_vacio(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        bishop = Bishop('White')
        actual_position = (4, 4)
        
        movimientos = bishop.ValidMoves(actual_position, board)
        
        self.assertIn((5, 5), movimientos)
        self.assertIn((3, 3), movimientos)
        self.assertIn((2, 6), movimientos)

    def test_movimientos_con_pieza_enemiga(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        bishop = Bishop('White')
        actual_position = (4, 4)
        board[6][6] = Bishop('Black')

        movimientos = bishop.ValidMoves(actual_position, board)
        
        self.assertIn((6, 6), movimientos)

if __name__ == "__main__":
    unittest.main()

