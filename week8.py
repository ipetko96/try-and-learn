class Stvorce:
    def __init__(self, n):
        self.pole = [[0] * (n**2) for _ in range(n**2)]

    def urob(self, index):
        self.slice_column = [len(self.pole) // 2, len(self.pole) // 2]
        self.slice_row = [len(self.pole) // 2, len(self.pole) // 2]
        for i in index:
            self.sub_pole = self.pole[:]
            if i == "1":
                self.sub_pole = [self.sub_pole[j][:len(self.sub_pole) // 2] for j in range(0, len(self.sub_pole) // 2)]
                self.slice_row[0] -= len(self.sub_pole)
                self.slice_column[1] += len(self.sub_pole)
            elif i == "2":
                self.sub_pole = [self.sub_pole[j][len(self.sub_pole) // 2:] for j in range(0, len(self.sub_pole) // 2)]
                self.slice_column[0] -= len(self.sub_pole)
                self.slice_row[1] += len(self.sub_pole)
            elif i == "3":
                self.pole = [self.pole[j][:len(self.pole) // 2] for j in range(len(self.pole) // 2, len(self.pole))]
            elif i == "4":
                self.pole = [self.pole[j][len(self.pole) // 2:] for j in range(len(self.pole) // 2, len(self.pole))]
        for y in range(self.slice_column[0], self.slice_row[0]):
            for x in range(self.slice_column[1], self.slice_row[1]):
                if self.pole[y][x] == 0:
                    self.pole[y][x] = 1
                elif self.pole[y][x] == 1:
                    self.pole[y][x] = 0

    def pocet(self):
        print(
            (sum([i.count(0) for i in self.pole]), sum([i.count(1) for i in self.pole]))
        )

    def vypis(self):
        for i in self.pole:
            print(i)


stv = Stvorce(2)
stv.pocet()
stv.vypis()
print()
stv.urob("2")
stv.pocet()
stv.vypis()

# 1 2
# 3 4
#   - - - - - - - - - - - - - - - -
#   - - - - - - - - - - - - - - - -
#   - - - - - - - - - - - - - - - -
#   - - - - X X X X X X X X - - - -
#   - - X X X X X X X X X X X X - -
#   - X X X X X X X X X X X X X X -
#   X X X X - - X X X X - - X X X X
#   X X X X - - X X X X - - X X X X
#   X X X X X X X X X X X X X X X X
#   X X X X X X X X X X X X X X X X
#   - X X X X - - - - - - X X X X -
#   - - X X X X - - - - X X X X - -
#   - - - - X X X X X X X X - - - -
#   - - - - - - - - - - - - - - - -
#   - - - - - - - - - - - - - - - -
#   - - - - - - - - - - - - - - - -

# 11 12
# 13 14
#   - - - - - - - -
#   - - - - - - - -
#   - - - - - - - -
#   - - - - X X X X
#   - - X X X X X X
#   - X X X X X X X
#   X X X X - - X X
#   X X X X - - X X

# 111 112
# 113 114
#   - - - -
#   - - - -
#   - - - -
#   - - - -

# 1111 1112
# 1113 1114
#   - -
#   - -
