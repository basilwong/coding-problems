from board import Board
from player import Player

def run():
    board = Board()
    player1 = Player(1)
    player2 = Player(2)
    while board.available_moves():
        player1.play_move(board)
        if board.available_moves():
            player2.play_move(board)

if __name__ == "__main__":
    run()
