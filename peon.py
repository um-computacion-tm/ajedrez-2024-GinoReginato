from piece import Piece

class Peon(Piece):

    def __init__(self, color):
        super().__init__(color)
    
    def ValidMoves(self, actual_position, board):
        
        x, y = actual_position
        movimientos = []
        capturas = []  

        if self.__color__ == 'white':
            movimientos.append((x, y + 1))

            if y == 1:  # Primer movimiento (se dan 2 pasos)
                movimientos.append((x, y + 2))

            if x > 0 and board[x - 1][y + 1] and board[x - 1][y + 1].__color__ == 'black':
                capturas.append((x - 1, y + 1))
            if x < 7 and board[x + 1][y + 1] and board[x + 1][y + 1].__color__ == 'black':
                capturas.append((x + 1, y + 1))

        else: 
            movimientos.append((x, y - 1))

            if y == 6:
                movimientos.append((x, y - 2))

        
            if x > 0 and board[x - 1][y - 1] and board[x - 1][y - 1].__color__ == 'white':
                capturas.append((x - 1, y - 1))
            if x < 7 and board[x + 1][y - 1] and board[x + 1][y - 1].__color__ == 'white':
                capturas.append((x + 1, y - 1))

        return movimientos + capturas 
