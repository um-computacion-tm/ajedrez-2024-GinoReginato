class OutOfBoardError(Exception):
    """Excepción para movimientos fuera del tablero."""
    pass

class InvalidMove(Exception):
    """Excepción para movimientos inválidos en el ajedrez."""
    pass

from board import Board

class Chess:

    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        # Aquí podrías lanzar InvalidMove si el movimiento es inválido
        self.change_turn()

    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
