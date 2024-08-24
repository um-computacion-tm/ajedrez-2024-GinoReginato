import unittest
from rook import Rook
from piece import Piece 

class TestRook(unittest.TestCase):

    def setUp(self):
      
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_movimiento_libre(self):
    
        rook = Rook('white')
        actual_position = (4, 4)
        movimientos = rook.ValidMoves(actual_position, self.board)
        
    
        self.assertIn((4, 5), movimientos)  
        self.assertIn((4, 3), movimientos) 
        self.assertIn((5, 4), movimientos)
        self.assertIn((3, 4), movimientos)


if __name__ == "__main__":
    unittest.main()
