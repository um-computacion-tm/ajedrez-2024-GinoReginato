import unittest
from queen import Queen
from piece import Piece 

class TestQueenSimple(unittest.TestCase):

    def test_movimientos_en_tablero_vacio(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        queen = Queen('White')
        actual_position = (3, 3)
        
        movimientos = queen.ValidMoves(actual_position, board)
        
        self.assertIn((4, 3), movimientos) 
        self.assertIn((3, 4), movimientos)  
        self.assertIn((2, 2), movimientos) 

    def test_movimientos_con_pieza_enemiga(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        queen = Queen('White')
        actual_position = (3, 3)
        board[4][3] = Piece('Black') 

        movimientos = queen.ValidMoves(actual_position, board)
        
        
        self.assertIn((4, 3), movimientos)

if __name__ == "__main__":
    unittest.main()
