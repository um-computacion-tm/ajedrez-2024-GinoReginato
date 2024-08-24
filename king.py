from piece import Piece

class King(Piece):

    def ValidMoves(self, actual_position):
        
        x, y = actual_position