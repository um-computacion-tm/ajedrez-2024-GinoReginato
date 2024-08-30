import unittest
from king import King
from piece import Piece

class TestKing(unittest.TestCase):

    def test_movimientos_en_tablero_vacio(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        king = King('White')
        actual_position = (4, 4)
        
        movimientos = king.ValidMoves(actual_position, board)
        
        movimientos_esperados = [
            (5, 4), (3, 4), (4, 5), (4, 3),
            (5, 5), (5, 3), (3, 5), (3, 3)
        ]
        self.assertCountEqual(movimientos, movimientos_esperados)

    def test_movimientos_con_pieza_enemiga(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        king = King('White')
        actual_position = (4, 4)
        board[5][4] = Piece('Black')

        movimientos = king.ValidMoves(actual_position, board)
        
        self.assertIn((5, 4), movimientos)

if __name__ == "__main__":
    unittest.main()
