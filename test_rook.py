import unittest
from rook import Rook
from piece import Piece 

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_movimientos_en_tablero_vacio(self):
        rook = Rook('white')
        actual_position = (4, 4)
        movimientos = rook.ValidMoves(actual_position, self.board)
        
        self.assertIn((4, 5), movimientos)  
        self.assertIn((4, 3), movimientos) 
        self.assertIn((5, 4), movimientos)
        self.assertIn((3, 4), movimientos)

    def test_movimiento_con_pieza_enemiga(self):
        rook = Rook('white')
        actual_position = (4, 4)
        
        self.board[4][6] = Piece('black')  
        
        movimientos = rook.ValidMoves(actual_position, self.board)
        
        self.assertIn((4, 5), movimientos)
        self.assertIn((4, 6), movimientos)  
        self.assertNotIn((4, 7), movimientos) 

if __name__ == "__main__":
    unittest.main()
