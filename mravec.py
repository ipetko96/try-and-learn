class Mravec:
    def __init__(self, meno_suboru):
        with open(meno_suboru) as file:
            file = file.read().split("\n\n")
            self.pole = [[j for j in i] for i in file[0].split()]
            self.kocky = {(int(i[2]), int(i[4])): i[0] for i in file[1].split("\n")}
            self.hrac = (None, None)

    def __str__(self):
        vypis = ""
        for y in range(len(self.pole)):
            for x in range(len(self.pole[y])):
                if self.hrac == (y, x):
                    vypis += "@"
                    continue
                try:
                    vypis += self.kocky[(y, x)]
                except KeyError:
                    vypis += self.pole[y][x]
            vypis += "\n"
        return vypis[:-1]

    def start(self, riadok, stlpec):
        self.hrac = (riadok, stlpec)

    def potlac(self, y, x, smer):
        if smer == "p":
            if (y, x + 1) in self.kocky:
                self.potlac(y, x + 1, smer)
            self.kocky[(y, x + 1)] = self.kocky.pop((y, x))

    def rob(self, prikazy):
        while len(prikazy) > 0:
            prikaz = prikazy[:1]
            if prikaz == "p":
                y, x = self.hrac
                if (y, x + 1) in self.kocky:
                    self.potlac(y, x + 1, prikaz)
                self.hrac = (y, x + 1)
            prikazy = prikazy[1:]

    def zisti(self):
        naPlusku = set()
        for i in self.kocky:
            if self.pole[i[0]][i[1]] == "+":
                naPlusku.add(self.kocky[i])
        return naPlusku


if __name__ == "__main__":
    m = Mravec("subor1.txt")
    print(m)
    print("zisti =", m.zisti())
    m.start(1, 0)
    print(m)
    m.rob("ppp")
    print(m)
    print("zisti =", m.zisti())
    # m.rob("dl")
    # print(m)
    # print("zisti =", m.zisti())
