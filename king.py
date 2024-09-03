from piece import Piece

class King(Piece):

    def ValidMoves(self, actual_position, board):
        
        x, y = actual_position
        movimientos = []

       
        direcciones = [
            (1, 0), (-1, 0), (0, 1), (0, -1), 
            (1, 1), (1, -1), (-1, 1), (-1, -1) 
        ]

        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy

          
            if 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] is None: 
                    movimientos.append((nx, ny))
                elif board[nx][ny].get_color() != self.get_color(): 
                    movimientos.append((nx, ny))

        return movimientos
