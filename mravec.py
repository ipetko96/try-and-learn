class Mravec:
    def __init__(self, meno_suboru):
        with open(meno_suboru) as file:
            file = file.read().split("\n\n")
            self.pole = [[j for j in i] for i in file[0].split()]
            self.kocky = {(int(i[2]), int(i[4])): i[0] for i in file[1].split("\n")}
            self.hrac = (None, None)
            self.mapa = {"p": "y,x+1", "d": "y+1,x", "l": "y,x-1", "h": "y-1,x"}
            self.allowed = "pdlh"

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
        suradnice = self.mapa[smer]
        if eval(suradnice) in self.kocky:
            self.potlac(*eval(suradnice), smer)
        self.kocky[(eval(suradnice))] = self.kocky.pop((y, x))

    def rob(self, prikazy):
        while len(prikazy) > 0:
            prikaz = prikazy[:1]
            if prikaz not in self.allowed:
                prikazy = prikazy[1:]
                continue
            # variables y and x are used later in the eval function
            y, x = self.hrac
            suradnice = self.mapa[prikaz]
            if eval(suradnice) in self.kocky:
                self.potlac(*eval(suradnice), prikaz)
            if len(tuple(filter(lambda x: x < 0, eval(suradnice)))) > 0:
                prikazy = prikazy[1:]
                continue
            if eval(suradnice)[0] > len(self.pole):
                prikazy = prikazy[1:]
                continue
            if eval(suradnice)[1] > len(self.pole[0]):
                prikazy = prikazy[1:]
                continue
            self.hrac = eval(suradnice)
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
    m.rob("ppp")
    print(m)
    print("zisti =", m.zisti())
    # m.rob("dl")
    # print(m)
    # print("zisti =", m.zisti())
