from pieces import Piece

class Rook(Piece):

    def valid_moves(self, actual_position, board):
        x, y = actual_position
        movimientos = []

        # Movimientos hacia arriba y abajo
        direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in direcciones:
            actual_x, actual_y = x, y
            
            while True:
                actual_x += dx
                actual_y += dy
                
            
                if 0 <= actual_x < 8 and 0 <= actual_y < 8:
                    if board[actual_x][actual_y] is None:  # La casilla está vacía
                        movimientos.append((actual_x, actual_y))
                    elif board[actual_x][actual_y].color != self.color:  # Pieza en el camino
                        movimientos.append((actual_x, actual_y))
                        break  # Choca con otra pieza para comer
                    else: 
                        break
                else:           # Pieza del mismo color
                    break

        return movimientos



        