
import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def __get_random_first_player(self):
        return random.randint(0, 1)

    def __fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def __swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def __show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.__get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.__show_board()

            valid = False
            while not valid:
                # taking user input
                row, col = list(
                    map(
                        int,
                        input(
                            "Enter row and column numbers to fix spot: "
                            ).split()))
                print()
                try:
                    row = int(row)
                    col = int(col)
                except ValueError:
                    print("Incorrect input. Not a number")
                    continue
                if row >= 1 and row <= 3 and col >= 1 and col <= 3:
                    if(str(self.board[row - 1][col - 1]) == '-'):
                        self.__fix_spot(row - 1, col - 1, player)
                        valid = True

                    else:
                        print("Incorrect input. This place is not empty")
                else:
                    print("Incorrect input. Enter two number from 1 to 3")

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.__swap_player_turn(player)

        # showing the final view of board
        print()
        self.__show_board()


# starting the game
# tic_tac_toe = TicTacToe()
# tic_tac_toe.start()
