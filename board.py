from rook import Rook
from horse import Horse
from bishop import Bishop
from king import King
from queen import Queen
from peon import Peon

class Board:
    def __init__(self):
        self.position = []
        for _ in range(8):
            col = [None] * 8
            self.position.append(col)
        
        # Inicialización de piezas
        self.position[0][0] = Rook("Black")
        self.position[0][7] = Rook("Black")
        self.position[7][7] = Rook("White")
        self.position[7][0] = Rook("White")

        self.position[0][2] = Bishop("Black")
        self.position[0][5] = Bishop("Black")
        self.position[7][2] = Bishop("White")
        self.position[7][5] = Bishop("White")

        self.position[0][1] = Horse("Black")
        self.position[0][6] = Horse("Black")
        self.position[7][1] = Horse("White")
        self.position[7][6] = Horse("White")

        self.position[0][4] = King("Black")
        self.position[7][4] = King("White")

        self.position[0][3] = Queen("Black")
        self.position[7][3] = Queen("White")

        self.position[1] = [Peon("Black")] * 8
        self.position[6] = [Peon("White")] * 8

