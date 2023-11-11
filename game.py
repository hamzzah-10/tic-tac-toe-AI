import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class Tictactoe:
    def __init__(self):
        # Constructor for the Tic-Tac-Toe game
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        # Create an empty Tic-Tac-Toe board
        return [' ' for _ in range(9)]

    def print_board(self):
        # Print the current state of the board
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:  # List comprehension to format the board
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Print the board with numbered squares to guide players
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check if the move in 'square' with 'letter' results in a win
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3:(row_ind + 1) * 3]

        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]

        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True

        return False

    def empty_squares(self):
        # Check if there are any empty squares on the board
        return ' ' in self.board

    def num_empty_squares(self):
        # Count the number of empty squares on the board
        return self.board.count(' ')

    def available_moves(self):
        # Return a list of available (empty) squares
        return [i for i, x in enumerate(self.board) if x == " "]

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + " Wins!!")
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)

    if print_game:
        print("It's a tie!")

# Create players: Human 'X' and Random Computer 'O'


# Start the game with players, printing each move


x_wins = 0
o_wins = 0
ties = 0
for _ in range(10):
    x_player = SmartComputerPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = Tictactoe()

    result = play(t, x_player, o_player, print_game=True)

    if result == 'X':
        x_wins +=1
    elif result == 'O':
        o_wins +=1
    else:
        ties =+1

print(x_wins)                
print(o_wins)                
print(ties)                