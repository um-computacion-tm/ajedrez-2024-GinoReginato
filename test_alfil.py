import unittest
from alfil import Alfil
from piece import Piece

class TestAlfil(unittest.TestCase):

    def test_movimientos_en_tablero_vacio(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        alfil = Alfil('White')
        actual_position = (4, 4)
        
        movimientos = alfil.ValidMoves(actual_position, board)
        
    
        self.assertIn((5, 5), movimientos) 
        self.assertIn((3, 3), movimientos)
        self.assertIn((2, 6), movimientos)

    def test_movimientos_con_pieza_enemiga(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        alfil = Alfil('White')
        actual_position = (4, 4)
        board[6][6] = Piece('Black')

        movimientos = alfil.ValidMoves(actual_position, board)
        
        
        self.assertIn((6, 6), movimientos)

if __name__ == "__main__":
    unittest.main()
