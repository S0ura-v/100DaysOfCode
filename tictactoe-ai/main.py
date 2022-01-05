import sys
import os
from board import Board
from player import Player 
from computer import ComputerEasy, ComputerImpossible
from termcolor import colored

def main(mode):
    if mode == "easy":
        computer = ComputerEasy("x")
    else:
        computer = ComputerImpossible("x")
    board = Board()
    player = Player("o") 

    while True:
        # computer will always be playing x:
        # playing the computer 
        computer.make_move(board=board, pos=computer.get_move(board=board, symbol="x"))
        
        # checking if a person won
        if board.is_win("x"):
            return "x"
        elif board.is_win("o"):
            return "o"

        # checking for tie 
        if not board.is_empty():
            return "tie"

        os.system("clear")
        board.print_schematic()
        board.print_rules()
        board.print_board() 

        # taking input 
        player_pos = int(input("Enter the position you want to make your next mark: "))
        if player_pos in board.get_possible_moves(): 
            player.make_move(board=board, pos=player_pos)
        else:
            continue

# running the code 
if __name__ == "__main__":
    # checking for CLArgs
    if len(sys.argv) != 2:
        print(colored("mode CLArgument not given", "red"))
        exit(1)
    elif sys.argv[1] not in ["easy", "impossible"]:
        print(colored("Usage: python3 main.py [easy/impossible]", "red"))
        exit(1)
    result = main(sys.argv[1])
    if result == "tie":
        print("This Game was a Tie")
    else:
        print(f"{result.upper()} Won the game")
