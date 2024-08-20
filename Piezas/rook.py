from piece import Piece

class Rook(Piece):

    def ValidMoves(self, actual_position):
        
        x, y = actual_position