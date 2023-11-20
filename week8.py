class Stvorce:
    def __init__(self, n):
        self.pole = [[0] * (n**2) for _ in range(n**2)]

    def urob(self, index):
        for i in index:
            if i == "1":
                for i in range(
                    len(
                        [
                            self.pole[i][0 : len(self.pole) // 2]
                            for i in range(0, len(self.pole) // 2)
                        ]
                    )
                ):
                    for j in range(
                        len(
                            [
                                self.pole[i][0 : len(self.pole) // 2]
                                for i in range(0, len(self.pole) // 2)
                            ][i]
                        )
                    ):
                        if self.pole[i][j] == 0:
                            self.pole[i][j] = 1
                        else:
                            self.pole[i][j] = 0
                ...
            elif i == "2":
                ...
            elif i == "3":
                ...

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
stv.urob("1")
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
