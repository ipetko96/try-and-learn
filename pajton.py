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
                for j in v:
                    if j in self.operacie:
                        raise SyntaxError
                if v.isnumeric():
                    pass
                else:
                    try:
                        v = self.prem(v)
                    except NameError:
                        raise SyntaxError
                if i != 0 and vysledok[-1] in self.operacie:
                    vysledok = vysledok.replace("/", "//")
                    vysledok = str(eval(vysledok + v))
                else:
                    vysledok += v
            elif i % 2 == 1:
                if v in self.operacie:
                    vysledok += v
                else:
                    raise SyntaxError

        if vysledok[-1] in self.operacie:
            raise SyntaxError
        return vysledok

    def prirad(self, retazec):
        meno, hodnota = retazec.split(" = ")
        meno = meno.strip()
        hodnota = hodnota.strip()
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
        self.tab[meno] = hodnota
        return None

    def prikaz(self, retazec):
        if retazec == "globals()":
            return self.globals()
        if retazec == "dir()":
            return self.dir()
        if "prem(" in retazec:
            return eval(f"self.prem('{retazec[5:-1]}')")
        if " = " in retazec:
            return self.prirad(retazec)
        print(self.vyraz(retazec))

    def dir(self):
        return self.tab.keys() | set()

    def globals(self):
        if not self.tab:
            return None
        data = ""
        for k, v in self.tab.items():
            data += f"{k}:{v}\n"
        return data[:-1]


if __name__ == "__main__":
    p = Pajton()
    # p.prikaz("a = 2")
    # p.prikaz("b = a + 1")
    # p.prikaz("c = 7 - b")
    while True:
        try:
            hodn = p.prikaz(input(">>> "))
            if hodn is not None:
                print(hodn)
        except SyntaxError:
            print("+++ syntakticka chyba +++")
        except NameError:
            print("+++ chybne meno premennej +++")
