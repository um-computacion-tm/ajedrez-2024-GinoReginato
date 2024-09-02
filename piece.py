class Piece:
    
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        return self.__color__

    def ValidMoves(self, actual_position):
        raise NotImplementedError
