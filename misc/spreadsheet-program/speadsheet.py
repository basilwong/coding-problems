

class Spreadsheet:

    def __init__(self, columns, rows):
        self.sheet = [[""] * columns for _ in range(rows)]

    def update(self, val, x, y):
        self.sheet[y][x] = str(val)

    def print_sheet(self):
        for line in self.sheet:
            for i in range(len(line)):
                print(line[i], end="")
                if i != len(line) - 1:
                    print("|", end="")
                else:
                    print("")

    def print_pretty(self):
        for line in self.sheet:
            for i in range(len(line)):
                max_length = max([len(x) for x in [row[i] for row in self.sheet]])
                print(line[i].ljust(max_length), end="")
                if i != len(line) - 1:
                    print("|", end="")
                else:
                    print("")


if __name__ == "__main__":
    x = Spreadsheet(3, 4)

    x.update("bob", 0, 0)
    x.update(10, 1, 0)
    x.update("foo", 2, 0)
    x.update("alice", 0, 1)
    x.update(5, 1, 1)
    x.update("cat", 2, 3)


    x.print_sheet()
    x.print_pretty()
