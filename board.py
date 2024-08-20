
from peon import Peon
from rook import Rook
from horse import Horse
from alfil import Alfil
from king import King
from queen import Queen


class Board:
    def __init__(self):
        self.__position__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__position__.append(col)
        #Posicion Torre
        self.__position__[0][0] = Rook ("Black")
        self.__position__[0][7] = Rook ("Black")
        
        self.__position__[7][7] = Rook ("White")
        self.__position__[7][0] = Rook ("White")
        
        #Posicion Alfil
        self.__position__[0][2] = Alfil ("Black")
        self.__position__[0][5] = Alfil ("Black")
        
        self.__position__[7][2] = Alfil ("White")
        self.__position__[7][5] = Alfil ("White")
        
        #Posicion Caballo
        self.__position__[0][1] = Horse ("Black")
        self.__position__[0][5] = Horse ("Black")
        
        self.__position__[7][6] = Horse ("White")
        self.__position__[7][1] = Horse ("White")
        
        #Posicion Rey
        self.__position__[0][4] = King ("Black")
        
        self.__position__[7][4] = King ("White")
        
        #Posicion Reina
        self.__position__[0][3] = Queen ("Black")
        
        self.__position__[7][3] = Queen ("White")
        
        #Posicion Peones
        self.__position__[1][0] = Peon ("Black")
        self.__position__[1][1] = Peon ("Black")
        self.__position__[1][2] = Peon ("Black")
        self.__position__[1][3] = Peon ("Black")
        self.__position__[1][4] = Peon ("Black")
        self.__position__[1][5] = Peon ("Black")
        self.__position__[1][6] = Peon ("Black")
        self.__position__[1][7] = Peon ("Black")

        self.__position__[6][0] = Peon ("White")
        self.__position__[6][1] = Peon ("White")
        self.__position__[6][2] = Peon ("White")
        self.__position__[6][3] = Peon ("White")
        self.__position__[6][4] = Peon ("White")
        self.__position__[6][5] = Peon ("White")
        self.__position__[6][6] = Peon ("White")
        self.__position__[6][7] = Peon ("White")
