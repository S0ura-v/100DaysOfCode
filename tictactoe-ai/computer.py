from board import Board
import random

class ComputerEasy():
    def __init__(self, symbol="x"):
        self.symbol = symbol

    def make_move(self, board: Board, pos: int):
        board.make_move(symbol=self.symbol, pos=pos) 

    def get_move(self, board: Board, symbol: str):
        possible_moves = board.get_possible_moves()
        return random.choice(possible_moves)
    
class ComputerImpossible():
    def __init__(self, symbol="x"):
        self.symbol = symbol
    
    def make_move(self, board: Board, pos: int):
        board.make_move(symbol=self.symbol, pos=pos) 
    
    def get_move(self, board: Board, symbol: str):
        return self.minimax(board, symbol)["index"]
    
    def minimax(self, board: Board, player: str):
        # all possible empty indices 
        available_spots = board.get_possible_moves()

        # checking for empty board 
        if len(available_spots) == 9:
            return {"index": 5}

        # checking for base cases
        if board.is_win("x"):
            return {"score": 1 * (len(available_spots) + 1)}
        elif board.is_win("o"):
            return {"score": -1 * (len(available_spots) + 1)}
        elif not board.is_empty():
            return {"score": 0}
        
        # collecting all the moves 
        moves = []

        for i in range(len(available_spots)):
            # storing the move in a dictionary
            move = {}
            move["index"] = available_spots[i]

            # creating the new board 
            board.positions[available_spots[i]] = player

            # recursive calls
            if player == "x":
                move["score"] = self.minimax(board=board, player="o")["score"]
            elif player == "o":
                move["score"] = self.minimax(board=board, player="x")["score"]
            
            # ressetting to empty position  
            board.positions[available_spots[i]] = " "

            # adding to the array 
            moves.append(move)

        # defining the best move
        best_move = None 
        
        # checking for the best move
        if player == "x":
            best_score = -10000
            for i in range(len(moves)):
                if moves[i]["score"] > best_score:
                    best_move = moves[i]["index"]
                    best_score = moves[i]["score"]
        else:
            best_score = 10000
            for i in range(len(moves)):
                if moves[i]["score"] < best_score:
                    best_move = moves[i]["index"]
                    best_score = moves[i]["score"]
        return {"score": best_score, "index": best_move}
    
        
