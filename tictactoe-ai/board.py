class Board():
    def __init__(self):
        self.positions = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    def make_move(self, symbol, pos):
        self.positions[pos] = symbol
    
    def print_board(self):
        """Prints the current board"""
        board_vis = f"""
     |     |     
  {self.positions[1]}  |  {self.positions[2]}  |  {self.positions[3]}
     |     |
-----------------
     |     |  
  {self.positions[4]}  |  {self.positions[5]}  |  {self.positions[6]}
     |     |
-----------------
     |     | 
  {self.positions[7]}  |  {self.positions[8]}  |  {self.positions[9]}
     |     |
"""
        print(board_vis) 

    def print_schematic(self):
        """Prints the board schematics for better user interface"""
        board_vis = f"""
     |     |     
  1  |  2  |  3
     |     |
-----------------
     |     |  
  4  |  5  |  6
     |     |
-----------------
     |     | 
  7  |  8  |  9
     |     |
"""
        print(board_vis)

    def print_rules(self):
        """Prints the rules for tic tac toe""" 
        print("""
Rules
    1) Input an integer only between 1 - 9
    2) Your input should not coincide with an already marked position
    3) Enjoy!!
        """)
    
    def is_empty(self):
        """Returns True if the board is empty, otherwise False"""
        for i in range(1, len(self.positions)):
            if self.positions[i] == " ":
                return True 
        return False
    
    def is_win(self, symbol):
        """Returns True if any player has won, otherwise False"""
        if (self.positions[1] == self.positions[4] == self.positions[7] == symbol) or \
               (self.positions[2] == self.positions[5] == self.positions[8] == symbol) or \
               (self.positions[3] == self.positions[6] == self.positions[9] == symbol) or \
               (self.positions[1] == self.positions[5] == self.positions[9] == symbol) or \
               (self.positions[3] == self.positions[5] == self.positions[7] == symbol) or \
               (self.positions[1] == self.positions[2] == self.positions[3] == symbol) or \
               (self.positions[4] == self.positions[5] == self.positions[6] == symbol) or \
               (self.positions[7] == self.positions[8] == self.positions[9] == symbol):
            return True
        else:
            return False
    
    def get_possible_moves(self):
        return [i for i in range(1, len(self.positions)) if self.positions[i] == " "]
    

