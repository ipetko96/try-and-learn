# 3 4
# N 1 3
# O 1 2
# H 1 1
# P 0 1
# Y 0 2
# T 0 3


class RobotKarel:
    def __init__(self, meno_suboru):
        with open(meno_suboru) as subor:
            lines = subor.readlines()
            firstLine = lines[0].strip().split()
            self.pole = [["."] * (int(firstLine[1])) for _ in range(int(firstLine[0]))]
            for line in lines[1:]:
                line = line.strip().split()
                self.pole[int(line[1])][int(line[2])] = line[0]

    def __str__(self):
        return ""

    def robot(self, riadok, stlpec, smer):
        ...

    def rob(self, prikaz):
        return 0

    def batoh(self):
        return []


k = RobotKarel("subor1.txt")
print(k)
