from chess import Chess, OutOfBoardError, InvalidMove

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        print("turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))

        
        
        if not (0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7):
            raise OutOfBoardError("Movimiento fuera del tablero")

        chess.move(from_row, from_col, to_row, to_col)

    except OutOfBoardError as e:
        print(e)
    except InvalidMove as e:
        print("Movimiento no válido")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
