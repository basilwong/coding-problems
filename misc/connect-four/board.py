BOARD_ROWS = 6
BOARD_COLS= 7
CONNECT_FOUR = 4
DIRECTIONS = (((0, 1), (0, -1)), ((1, 0), (-1, 0)), ((-1, 1), (1, -1)), ((-1, -1), (1, 1)))
PLAYER_1 = 1
PLAYER_2 = 2
EMPTY = 0
GAME_IS_ENDED = 3

class Board:

    def __init__(self):
        self._new_game()

    def _new_game(self):
        self.board = [[0] * BOARD_COLS for _ in range(BOARD_ROWS)]
        self.state = PLAYER_1  # Players 1 and 2
        self.winner = None
        self._pretty_print_board()
        print(f"New Game: PLAYER {self.state} it is your turn.")

    def available_moves(self):
        if self.state == GAME_IS_ENDED:
            return list()
        available_cols = list()
        for col in range(BOARD_COLS):
            if self.board[0][col] == 0:
                available_cols.append(col)
        return available_cols

    def add_chip(self, col):
        """
        Returns false if the column is unavailable.
        :param col:
        :return:
        """
        for row in range(BOARD_ROWS - 1, -1, -1):
            if self.board[row][col] == EMPTY:
                return self._add_chip_to_board(row, col)
        return False

    def _add_chip_to_board(self, row, col):
        if not self.available_moves():
            self.state = GAME_IS_ENDED
            self._print_game_is_tie()
            return False
        self.board[row][col] = self.state
        self._pretty_print_board()
        if self._check_winner(row, col):
            self.winner = self.state
            self.state = GAME_IS_ENDED
            self._print_winner()
        else:
            self._new_state()
            if not self.available_moves():
                self.state = GAME_IS_ENDED
                self._print_game_is_tie()
            else:
                print(f"PLAYER {self.state} it is your turn.")
        return True

    def _check_winner(self, row, col):

        for dimension in DIRECTIONS:
            print(dimension, DIRECTIONS)
            count = 1
            for direction in dimension:
                temp_row, temp_col = row + direction[0], col + direction[1]
                while not self._check_out_of_bounds(temp_row, temp_col) and self.board[temp_row][temp_col] == self.state:
                    count += 1
                    if count >= CONNECT_FOUR:
                        return True
                    temp_row += direction[0]
                    temp_col += direction[1]
        return False

    def _print_winner(self):
        print(f"PLAYER {self.winner} is the winner!!!")

    def _print_game_is_tie(self):
        print("The game is a tie!!!")

    def _new_state(self):
        self.state = PLAYER_2 if self.state == PLAYER_1 else PLAYER_1

    def _check_out_of_bounds(self, row, col):
        return row < 0 or col < 0 or row >= BOARD_ROWS or col >= BOARD_COLS

    def _pretty_print_board(self):
        print("### Connect Four Board ###")
        for i in range(BOARD_ROWS):
            print(self.board[i])

    def _artificial_tie(self):
        self.board = [[3] * BOARD_COLS for _ in range(BOARD_ROWS)]
        self.board[0][0] = 0