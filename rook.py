from piece import Piece

class Rook(Piece):
    
    def ValidMoves(self, actual_position, board):
        x, y = actual_position
        movimientos = []


        direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in direcciones:
            actual_x, actual_y = x, y
            
            while True:
                actual_x += dx
                actual_y += dy
                
            
                if 0 <= actual_x < 8 and 0 <= actual_y < 8:
                    if board[actual_x][actual_y] is None:  
                        movimientos.append((actual_x, actual_y))
                    elif board[actual_x][actual_y].get_color() != self.get_color():
                        movimientos.append((actual_x, actual_y))
                        break  
                    else: 
                        break
                else:           
                    break

        return movimientos
