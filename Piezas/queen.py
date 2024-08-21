from pieces import Piece

class Queen(Piece):

    def ValidMoves(self, actual_position):
        
        x, y = actual_position