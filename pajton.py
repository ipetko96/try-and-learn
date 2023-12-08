class Pajton:
    def __init__(self):
        self.tab = {}
        self.allowed = "abcdefghijklmnopqrstuvwxyz0123456789_"
        self.operacie = ["+", "-", "*", "/"]

    def prem(self, meno):
        try:
            return self.tab[meno]
        except KeyError:
            raise NameError

    def vyraz(self, retazec):
        vysledok = ""
        retazec = retazec.split()
        for i, v in enumerate(retazec):
            if i % 2 == 0:
                try:
                    if int(v) < 0:
                        pass
                except ValueError:
                    for j in v:
                        if j in self.operacie:
                            raise SyntaxError
                    if v.isnumeric():
                        pass
                    else:
                        try:
                            v = self.prem(v)
                        except NameError:
                            raise NameError
                if i != 0 and vysledok[-1] in self.operacie:
                    if vysledok[-1] == "+":
                        vysledok = int(vysledok[:-1])
                        vysledok += int(v)
                        vysledok = str(vysledok)
                    elif vysledok[-1] == "-":
                        vysledok = int(vysledok[:-1])
                        vysledok -= int(v)
                        vysledok = str(vysledok)
                    elif vysledok[-1] == "*":
                        vysledok = int(vysledok[:-1])
                        vysledok *= int(v)
                        vysledok = str(vysledok)
                    elif vysledok[-1] == "/":
                        vysledok = int(vysledok[:-1])
                        try:
                            vysledok //= int(v)
                            vysledok = str(vysledok)
                        except ZeroDivisionError:
                            vysledok = str(0)
                else:
                    vysledok += str(v)
            elif i % 2 == 1:
                if v in self.operacie:
                    vysledok += v
                else:
                    raise SyntaxError
        if vysledok[-1] in self.operacie:
            raise SyntaxError
        return int(vysledok)

    def prirad(self, meno, hodnota):
        meno = meno.strip()
        hodnota = str(hodnota)
        if meno == hodnota:
            raise SyntaxError
        for i in meno.strip():
            if i.lower() not in self.allowed:
                raise SyntaxError
        if meno[0].isnumeric():
            raise SyntaxError
        if len(hodnota) == 0:
            raise SyntaxError
        if len(hodnota.split()) > 1:
            hodnota = self.vyraz(hodnota)
        self.tab[meno] = int(hodnota)
        return None

    def prikaz(self, retazec):
        if retazec == "globals()":
            return self.globals()
        if retazec == "dir()":
            return self.dir()
        if "prem(" in retazec:
            return self.prem(retazec[5:-1])
        if " = " in retazec:
            meno, hodnota = retazec.split(" = ")
            meno = meno.strip()
            hodnota = hodnota.strip()
            return self.prirad(meno, hodnota)
        return self.vyraz(retazec)

    def dir(self):
        return self.tab.keys() | set()

    def globals(self):
        if not self.tab:
            return None
        data = ""
        for k, v in self.tab.items():
            data += f"{k}: {v}\n"
        return data[:-1]


if __name__ == "__main__":
    p = Pajton()
    while True:
        try:
            hodn = p.prikaz(input(">>> "))
            if hodn is not None:
                print(hodn)
        except SyntaxError:
            print("+++ syntakticka chyba +++")
        except NameError:
            print("+++ chybne meno premennej +++")
