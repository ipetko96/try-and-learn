with open("logo_in") as file:
    file = (
        file.read()
        .replace("\n", " ")
        .replace("[", " [ ")
        .replace("]", " ] ")
        .replace('"', "'")
        .lstrip()
    )

allowed_key = ["fd", "rt", "lt", "pu", "pd", "setpc", "setpw", "repeat", "to"]
allowed_value = [
    "t.fd(",
    "t.rt(",
    "t.lt(",
    "t.pu()\n",
    "t.pd()\n",
    "t.pencolor(",
    "t.pensize(",
    "for repc in range(1, ",
    "def ",
]


with open(
    "logo_out.py",
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
                if last == "to":
                    func = True
                elif last == "setpc":
                    color = True
                elif last == "repeat":
                    repeat = True
                    instruction = False
                elif last == "pu" or last == "pd":
                    instruction = False
                else:
                    instruction = True
                out.write(f"{' ' * space}{allowed_value[allowed_key.index(last)]}")
            elif last == "[":
                space += 4
                if file[1:].lstrip().split(" ")[0] == "]":
                    out.write(f"{' ' * space}pass\n")
            elif last == "]":
                space -= 4
            elif not instruction:
                out.write(f"{' ' * space}{last}()\n")
            else:
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
        file = file[len(last):].lstrip()
    out.write("turtle.done()\n")
