class Pajton:
    def __init__(self):
        self.tab = {}

    def prem(self, meno):
        try:
            return self.tab[meno]
        except NameError:
            print("premenna neni")

    def vyraz(self, retazec):
        vyraz = ""
        operacie = ["+", "-", "*", "/"]
        retazec = retazec.split()
        for i, v in enumerate(retazec):
            if i % 2 == 0:
                if v.isnumeric():
                    if i != 0 and vyraz[-1] in operacie:
                        vyraz = vyraz.replace("/", "//")
                        vyraz = str(eval(vyraz + v))
                    else:
                        vyraz += v
                else:
                    raise SyntaxError
            elif i % 2 == 1:
                if v in operacie:
                    vyraz += v
                else:
                    raise SyntaxError

        if vyraz[-1] in operacie:
            raise SyntaxError
        return vyraz

    def prirad(self, meno, hodnota):
        ...

    def prikaz(self, retazec):
        if retazec == "globals()":
            return self.globals()
        if retazec == "dir()":
            return self.dir()
        if "vyraz" in retazec:
            return self.vyraz(retazec.split("(")[1][:-1])

    def dir(self):
        return ...

    def globals(self):
        return ...


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
