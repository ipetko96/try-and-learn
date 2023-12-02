class RobotKarel:
    def __init__(self, meno_suboru):
        with open(meno_suboru) as subor:
            lines = subor.readlines()
            firstLine = lines[0].strip().split()
            self.pole = [
                [["."] for _ in range(int(firstLine[1]))]
                for _ in range(int(firstLine[0]))
            ]
            for line in lines[1:]:
                line = line.strip().split()
                self.pole[int(line[1])][int(line[2])].append(line[0])

    def __str__(self):
        vypis = ""
        for y in range(len(self.pole)):
            for x in range(len(self.pole[y])):
                try:
                    self.karel
                    if y == self.karel["y"] and x == self.karel["x"]:
                        vypis += f"{self.karel['rotate_signs'][self.karel['smer'][0]]}"

                    else:
                        vypis += f"{self.pole[y][x][-1]}"
                except:
                    vypis += f"{self.pole[y][x][-1]}"
            if y < len(self.pole) - 1:
                vypis += "\n"
        return vypis

    def rotate(self, smer):
        smer = smer % 4
        self.karel["smer"] = self.karel["smer"][smer:] + self.karel["smer"][:smer]

    def robot(self, riadok, stlpec, smer):
        try:
            self.karel["y"] = riadok
            self.karel["x"] = stlpec
            self.rotate(smer)
        except:
            self.karel = {
                "y": riadok,
                "x": stlpec,
                "smer": [0, 1, 2, 3],
                "rotate_signs": [">", "v", "<", "^"],
                "batoh": [],
            }
            self.rotate(smer)

    def rob(self, prikaz):
        urobil = 0
        prikazy = prikaz.split()
        while len(prikazy) > 0:
            if prikazy[0].isnumeric():
                pocet = int(prikazy[0])
                prikaz = prikazy[1]
                prikazy = prikazy[2:]
            else:
                pocet = 1
                prikaz = prikazy[0]
                prikazy = prikazy[1:]
            for _ in range(pocet):
                if prikaz == "krok":
                    if self.karel["smer"][0] == 0:
                        if len(self.pole[self.karel["y"]][self.karel["x"]:]) > 1:
                            self.karel["x"] += 1
                            urobil += 1
                    elif self.karel["smer"][0] == 1:
                        if len(self.pole[self.karel["y"]:]) > 1:
                            self.karel["y"] += 1
                            urobil += 1
                    elif self.karel["smer"][0] == 2:
                        if len(self.pole[self.karel["y"]][:self.karel["x"]]) > 0:
                            self.karel["x"] -= 1
                            urobil += 1
                    elif self.karel["smer"][0] == 3:
                        if len(self.pole[:self.karel["y"]]) > 0:
                            self.karel["y"] -= 1
                            urobil += 1
                elif prikaz == "zdvihni":
                    if len(self.pole[self.karel["y"]][self.karel["x"]]) > 1:
                        self.karel["batoh"].append(
                            self.pole[self.karel["y"]][self.karel["x"]][-1]
                        )
                        del self.pole[self.karel["y"]][self.karel["x"]][-1]
                        urobil += 1
                elif prikaz == "vpravo":
                    self.rotate(1)
                    urobil += 1
                elif prikaz == "vlavo":
                    self.rotate(-1)
                    urobil += 1
                elif prikaz == "poloz":
                    try:
                        self.pole[self.karel["y"]][self.karel["x"]].append(
                            self.karel["batoh"][-1]
                        )
                        del self.karel["batoh"][-1]
                        urobil += 1
                    except:
                        pass
        return urobil

    def batoh(self):
        try:
            return self.karel["batoh"]
        except:
            return []
