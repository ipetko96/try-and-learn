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
        for y, row in enumerate(tab_copy):
            for x, value in enumerate(row):
                if value == ".":
                    square = [row[(x - x % 3):x - x % 3 + 3] for row in tab_copy][(y - y % 3):y - y % 3 + 3]
                    square = set(sum(square, []))
                    row = set(row)
                    column = set(rotated[x])
                    diff = self.numbers - row - column - square
                    self.tab[y][x] = diff
        if any(set() in sublist for sublist in self.tab):
            return None
        else:
            count = 0
            for row in self.tab:
                for value in row:
                    if isinstance(value, set) and len(value) == 1:
                        count += 1
            return count

    def nahrad(self):
        for i, line in enumerate(self.tab):
            for j, element in enumerate(line):
                if isinstance(element, set):
                    if len(element) == 1:
                        self.tab[i][j] = element.pop()
                    else:
                        self.tab[i][j] = "."

    def ries(self):
        self.nahrad()
        nahraditelne = self.urob()
        pocet_cyklov = 0
        while nahraditelne is not None:
            pocet_cyklov += 1
            self.nahrad()
            if nahraditelne == 0:
                return (pocet_cyklov, self.pocet_nezaplnenych())
            nahraditelne = self.urob()
        self.urob()
        self.nahrad()
        return (pocet_cyklov + 1, None)

    def pocet_nezaplnenych(self):
        return sum(x.count(".") for x in self.tab)
