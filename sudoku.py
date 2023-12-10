# . . . . . 9 . . .
# . . 7 . 8 6 . . .
# 6 . . 3 . . . . .
# . 4 . . . 7 . . 8
# . . . . . . . 3 2
# . . 3 6 . 5 1 . .
# . 6 . 7 . . . 8 .
# 3 . 2 . . . 4 9 .
# . 5 4 8 . . . . 3


class Sudoku:
    def __init__(self, meno_suboru):
        self.tab = []
        self.numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        with open(meno_suboru) as file:
            for line in file.readlines():
                self.tab.append([int(i) if i.isnumeric() else i for i in line.split()])

    def __str__(self):
        vypis = ""
        for line in self.tab:
            for value in line:
                if isinstance(value, set):
                    vypis += ". "
                else:
                    vypis += f"{str(value)} "
            vypis = vypis[:-1] + "\n"
        return vypis[:-1]

    def urob(self):
        tab_copy = [x[:] for x in self.tab]
        rotated = list(zip(*tab_copy[::-1]))
        for y, line in enumerate(tab_copy):
            for x, value in enumerate(line):
                if value == ".":
                    if y < 3 and x < 3:
                        slice = [row[:3] for row in tab_copy][:3]
                    elif y < 3 and x < 6:
                        slice = [row[3:6] for row in tab_copy][:3]
                    elif y < 3 and x < 9:
                        slice = [row[6:9] for row in tab_copy][:3]
                    elif y < 6 and x < 3:
                        slice = [row[:3] for row in tab_copy][3:6]
                    elif y < 6 and x < 6:
                        slice = [row[3:6] for row in tab_copy][3:6]
                    elif y < 6 and x < 9:
                        slice = [row[6:9] for row in tab_copy][3:6]
                    elif y < 9 and x < 3:
                        slice = [row[:3] for row in tab_copy][6:]
                    elif y < 9 and x < 6:
                        slice = [row[3:6] for row in tab_copy][6:]
                    elif y < 9 and x < 9:
                        slice = [row[6:9] for row in tab_copy][6:]
                    slice = set(sum(slice, []))
                    line = set(line)
                    column = set(rotated[x])
                    diff = self.numbers - line - column - slice
                    self.tab[y][x] = diff
        if any({} in sublist for sublist in self.tab):
            return None
        else:
            count = 0
            for line in self.tab:
                for value in line:
                    if isinstance(value, set) and len(value) == 1:
                        count += 1
            return count

    def nahrad(self):
        for i, line in enumerate(self.tab):
            for j, element in enumerate(line):
                if isinstance(element, set):
                    if len(element) > 1:
                        self.tab[i][j] = "."
                    else:
                        self.tab[i][j] = element.pop()

    def ries(self):
        ...

    def pocet_nezaplnenych(self):
        ...


s = Sudoku("input")
print(s)
print(s.urob())
s.nahrad()
print(s)
...
