class Stvorce:
    def __init__(self, n):
        self.pole = [[0] * (2**n) for _ in range(2**n)]

    def urob(self, index):
        self.sub_pole = self.pole[:]
        self.slice_start = [0, 0]
        self.slice_end = [len(self.pole), len(self.pole)]
        for i in index:
            if i == "1":
                self.sub_pole = [self.sub_pole[j][:len(self.sub_pole) // 2] for j in range(0, len(self.sub_pole) // 2)]
                self.slice_end[0] -= len(self.sub_pole)
                self.slice_end[1] -= len(self.sub_pole)
            elif i == "2":
                self.sub_pole = [self.sub_pole[j][len(self.sub_pole) // 2:] for j in range(0, len(self.sub_pole) // 2)]
                self.slice_start[1] += len(self.sub_pole)
                self.slice_end[0] -= len(self.sub_pole)
            elif i == "3":
                self.sub_pole = [self.sub_pole[j][:len(self.sub_pole) // 2] for j in range(len(self.sub_pole) // 2, len(self.sub_pole))]
                self.slice_start[0] += len(self.sub_pole)
                self.slice_end[1] -= len(self.sub_pole)
            elif i == "4":
                self.sub_pole = [self.sub_pole[j][len(self.sub_pole) // 2:] for j in range(len(self.sub_pole) // 2, len(self.sub_pole))]
                self.slice_start[0] += len(self.sub_pole)
                self.slice_start[1] += len(self.sub_pole)
        for y in range(self.slice_start[0], self.slice_end[0]):
            for x in range(self.slice_start[1], self.slice_end[1]):
                if self.pole[y][x] == 0:
                    self.pole[y][x] = 1
                elif self.pole[y][x] == 1:
                    self.pole[y][x] = 0

    def pocet(self):
        return (
            sum([i.count(0) for i in self.pole]),
            sum([i.count(1) for i in self.pole]),
        )

    def vypis(self):
        for i in self.pole:
            for j in i:
                if j == 0:
                    print("-", end="")
                elif j == 1:
                    print("X", end="")
            print()


# stv = Stvorce(4)
# vstup = [
#     "1",
#     "11",
#     "131",
#     "1314",
#     "143",
#     "12",
#     "1233",
#     "1234",
#     "1243",
#     "1244",
#     "23",
#     "234",
#     "2133",
#     "2134",
#     "2143",
#     "2144",
#     "24",
#     "242",
#     "2423",
#     "31",
#     "313",
#     "3132",
#     "32",
#     "324",
#     "3232",
#     "3411",
#     "3412",
#     "3421",
#     "3422",
#     "4",
#     "44",
#     "424",
#     "4241",
#     "413",
#     "4141",
#     "43",
#     "4311",
#     "4312",
#     "4321",
#     "4322",
# ]

# for i in vstup:
#     stv.urob(i)
# print(stv.pocet())
# stv.vypis()
