import unittest
from piece import Piece
from peon import Peon

class TestPeon(unittest.TestCase):
    
    def test_movimientos_peon_blanco(self):
        peon_blanco = Peon('white')
        board = [[None for _ in range(8)] for _ in range(8)] 
        
        movimientos = peon_blanco.ValidMoves((1, 1), board)
        self.assertIn((1, 2), movimientos)
        self.assertIn((1, 3), movimientos) 

    def test_movimientos_peon_negro(self):
        peon_negro = Peon('black')
        board = [[None for _ in range(8)] for _ in range(8)] 
        
        movimientos = peon_negro.ValidMoves((6, 6), board)
        self.assertIn((6, 5), movimientos) 
        self.assertIn((6, 4), movimientos) 
    
    def test_movimientos_con_pieza_blanca(self):
        peon_blanco = Peon('white')
        board = [[None for _ in range(8)] for _ in range(8)] 
        peon_negro = Peon('black')
        board[2][2] = peon_negro  
        
        movimientos = peon_blanco.ValidMoves((1, 1), board)
        self.assertIn((2, 2), movimientos) 

    def test_movimientos_con_pieza_negra(self):
        peon_negro = Peon('black')
        board = [[None for _ in range(8)] for _ in range(8)] 
        peon_blanco = Peon('white')
        board[5][5] = peon_blanco 
        
        movimientos = peon_negro.ValidMoves((6, 6), board)
        self.assertIn((5, 5), movimientos)

if __name__ == '__main__':
    unittest.main()

