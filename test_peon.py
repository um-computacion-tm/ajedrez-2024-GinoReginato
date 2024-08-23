import unittest
from peon import Peon
from board import Board

class TestPeon(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()


    def test_white_pawn_initial_moves(self):
        peon_blanco = Peon('white')
        self.assertEqual(peon_blanco.ValidMoves((3, 1), self.board.position), [(3, 2), (3, 3)])  # Movimientos de peón blanco

    def test_black_pawn_initial_moves(self):
        peon_negro = Peon('black')
        self.assertEqual(peon_negro.ValidMoves((4, 6), self.board.position), [(4, 5), (4, 4)])  # Movimientos de peón negro
    
    
if __name__ == '__main__':
    unittest.main()

