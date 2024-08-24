from piece import Piece    

class Horse(Piece):

    def ValidMoves(self, actual_position):
        
        x, y = actual_position