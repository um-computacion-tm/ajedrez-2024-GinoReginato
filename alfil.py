from piece import Piece

class Alfil(Piece):

    def ValidMoves(self, actual_position, Board):
        
        x, y = actual_position

        movimientos = []

        direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy

            while 0 <= nx < 8 and 0 <= ny < 8:
                if Board[nx][ny] is None:
                    movimientos.append((nx, ny))
                elif Board[nx][ny].get_color() != self.get_color():
                    movimientos.append((nx, ny))
                    break
                else:
                    break

                nx += dx
                ny += dy

        return movimientos
