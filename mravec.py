class Mravec:
    def __init__(self, meno_suboru):
        with open(meno_suboru) as file:
            file = file.read().split("\n\n")
            self.pole = [[j for j in i] for i in file[0].split()]
            self.kocky = {(int(i[2]), int(i[4])): i[0] for i in file[1].split("\n")}

    def __str__(self):
        vypis = ""
        for y in range(len(self.pole)):
            for x in range(len(self.pole[y])):
                try:
                    vypis += self.kocky[(y, x)]
                except KeyError:
                    vypis += self.pole[y][x]
            vypis += "\n"
        return vypis[:-1]

    def start(self, riadok, stlpec):
        ...

    def rob(self, prikazy):
        ...

    def zisti(self):
        return set()


if __name__ == "__main__":
    m = Mravec("subor1.txt")
    print(m)
    # print("zisti =", m.zisti())
    # m.start(1, 0)
    # m.rob("pp")
    # print(m)
    # print("zisti =", m.zisti())
    # m.rob("dl")
    # print(m)
    # print("zisti =", m.zisti())
