import random

class Player:

    def __init__(self, name=""):
        self.name = name

    def play_move0(self):
        pass
    def play_move1(self, board):
        available_moves = board.available_moves()
        if available_moves:
            board.add_chip(self.process_board(board, available_moves))

    def process_board(self, board, available_moves):
        for col in available_moves:
            for row in range(len(board) - 1, -1, -1):
                if board[row][col] == 0:
                    if not board._check_winner(row, col):
                        continue
                    else:
                        return col

        return random.choice(available_moves)