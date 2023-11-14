with open("logo-vstup") as file:
    file = (
        file.read().replace("\n", " ").replace("[", " [ ").replace("]", " ] ").lstrip()
    )
# file = 'lt 90 pu fd 100 rt 30 pd to krok  [ fd 30 rt 120 ]   repeat 4  [    fd 50   lt 10+20   repeat 3 [ krok ] lt 60  ]  rt 30 fd 70 repeat 10 [  ] '

# t = turtle.Turtle()
# t.lt(90)
# t.pu()
# t.fd(100)
# t.rt(30)
# t.pd()
# def krok():
#     t.fd(30)
#     t.rt(120)
# for repc in range(1, 5):
#     t.fd(50)
#     t.lt(10+20)
#     for repc in range(1, 4):
#         krok()
#     t.lt(60)
# t.rt(30)
# t.fd(70)
# for repc in range(1, 11):
#     pass

allowed_key = ["fd", "rt", "lt", "pu", "pd", "setpc", "setpw", "repeat", "to"]
allowed_value = [
    "t.fd(",
    "t.rt(",
    "t.lt(",
    "t.pu()\n",
    "t.pd()\n",
    "t.pencolor(",
    "pensize",
    "for repc in range(1, ",
    "def ",
]


with open(
    "logo-out.py",
    "w",
) as out:
    out.write("import turtle\nt = turtle.Turtle()\n")
    instruction = False
    space = 0
    func = False
    repeat = False
    color = False
    while len(file) > 0:
        last = file.split(" ")[0]
        if not func and not repeat and not color:
            if last in allowed_key:
                instruction = True
                if last == "to":
                    func = True
                elif last == "setpc":
                    color = True
                elif last == "repeat":
                    repeat = True
                    instruction = False
                out.write(f"{' ' * space}{allowed_value[allowed_key.index(last)]}")
            elif last == "[":
                space += 4
                if file[1:].lstrip().split(" ")[0] == "]":
                    out.write(f"{' ' * space}pass\n")
            elif last == "]":
                space -= 4
            elif not instruction:
                out.write(f"{' ' * space}{last}()\n")
            elif str(abs(eval(last))).isnumeric():
                out.write(f"{last})\n")
                instruction = False
        elif repeat:
            out.write(f"{int(last)+1}):\n")
            repeat = False
        elif func:
            out.write(f"{last}():\n")
            func = False
        elif color:
            last = file[: len(file[1:].split("'")[0]) + 2]
            out.write(f"{last})\n")
            color = False
        file = file[len(last) :].lstrip()
    out.write("turtle.done()\n")
