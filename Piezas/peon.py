from piece import Piece

class Peon(Piece):
    
    def ValidMoves(self, actual_position):
        
        x, y = actual_position
        movimientos = []
        
        if self.color == 'blanco':
            movimientos.append((x, y + 1))
            
            if y == 1:  # Primer movimiento (se dan 2 pasos)
                
                movimientos.append((x, y + 2))
        
        else:  # Color negro
            
            movimientos.append((x, y - 1))
            
            if y == 6:
                movimientos.append((x, y - 2))
        
        return movimientos
