from piece import Piece

class Peon(Piece):
    
    def ValidMoves(self, actual_position):
        
        x, y = actual_position
        movimientos = []
        
        if self.color == 'blanco':
            movimientos.append((x, y + 1))
            
            if y == 1:  # Primer movimiento (se dan 2 pasos)
                
                movimientos.append((x, y + 2))
        
        # Manera de comer una pieza (Diagonal)
            if x > 0 and tablero[x - 1][y + 1] and tablero[x - 1][y + 1].color == 'negro':
                capturas.append((x - 1, y + 1))
            if x < 7 and tablero[x + 1][y + 1] and tablero[x + 1][y + 1].color == 'negro':
                capturas.append((x + 1, y + 1))

        else:  # Color negro
            
            movimientos.append((x, y - 1))
            
            if y == 6:
                movimientos.append((x, y - 2))
        
         # Manera de comer una pieza (Diagonal)
            if x > 0 and tablero[x - 1][y + 1] and tablero[x - 1][y + 1].color == 'blanco':
                capturas.append((x - 1, y + 1))
            if x < 7 and tablero[x + 1][y + 1] and tablero[x + 1][y + 1].color == 'blanco':
                capturas.append((x + 1, y + 1))

        return movimientos
