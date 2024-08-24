from piece import Piece

class Alfil(Piece):

    def ValidMoves(self, actual_position):
        
        x, y = actual_position