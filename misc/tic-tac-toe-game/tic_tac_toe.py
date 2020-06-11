

class Game:

    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [[" "] * self.board_size for _ in range(self.board_size)]
        self.turns = 0
        self.__game_state()

    def __game_state(self):
        max_turns = self.board_size * self.board_size
        while self.turns < max_turns:
            winner = self.__check_winner()
            if winner:
                print(winner + " is the winner!")
                break
            sym = "X" if self.turns % 2 == 0 else "O"
            turn_input = self.__get_turn()
            self.board[turn_input[0]][turn_input[1]] = sym
            self.turns += 1

    def __get_turn(self, message=""):
        self.__print_board()
        print(message)
        turn_input = input("Please type next move then press enter: ").split()
        if len(turn_input) != 2:
            return self.__get_turn("Please enter two coordinates split by space.")
        turn_input[0], turn_input[1] = int(turn_input[0]), int(turn_input[1])
        if turn_input[0] < 0 or turn_input[0] >= self.board_size:
            return self.__get_turn("Please enter two coordinates within the board size.")
        elif turn_input[1] < 0 or turn_input[1] >= self.board_size:
            return self.__get_turn("Please enter two coordinates within the board size.")
        elif self.board[turn_input[0]][self.board[turn_input[1]] != " ":
            return self.__get_turn("Space has already been taken.")
        return turn_input

    def __print_board(self):
        for line in self.board:
            print("| ", end="")
            for element in line:
                print(element + " ", end="")
            print(" |")
        print("\n\n")

    def __check_winner(self):
        for i in range(self.board_size):
            result = self.__check_line(self.board[:][i])
            if result:
                return result
            result = self.__check_line(self.board[i][:])
            if result:
                return result
        # Diagonal Case
        result = self.__check_line([self.board[x][x] for x in range(self.board_size)])
        if result:
            return result
        else:
            return None

    def __check_line(self, arr):
        sym = arr[0]
        for e in arr:
            if e == " " or e != sym:
                return None
        return sym

if __name__ == "__main__":
    Game()
