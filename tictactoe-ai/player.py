from board import Board

class Player():
    def __init__(self, symbol):
        self.symbol = symbol
        
    def make_move(self, board: Board, pos: int):
        board.make_move(symbol=self.symbol, pos=pos)

