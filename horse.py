from piece import Piece    

class Horse(Piece):
    def movimientos_validos(self, actual_position, Board):
        x, y = actual_position
        movimientos = []

        # Posibles movimientos del caballo en forma de L
        movimientos_validos = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2)
        ]

        for nx, ny in movimientos_validos:
            if 0 <= nx < 8 and 0 <= ny < 8:
                if Board[nx][ny] is None: 
                    movimientos.append((nx, ny))
                elif Board[nx][ny].color != self.color: 
                    movimientos.append((nx, ny))

        return movimientos
