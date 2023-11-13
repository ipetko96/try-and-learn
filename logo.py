with open("logo-vstup") as file:
    file = file.read().replace("\n", " ").lstrip()

allowed = {
    "fd": "fd",
    "rt": "rt",
    "lt": "lt",
    "pu": "pu",
    "pd": "pd",
    "setpc": "pencolor",
    "setpw": "pensize",
    "repeat": "for repc in range",
    "to": "def",
}


space = 0
with open('logo-out.py', 'w',) as out:
    out.write('import turtle\nt = turtle.Turtle()\n')
    while len(file) > 0:
        instruction = file.split(" ")[0]
        if instruction == '[]':
            out.write(f"{' ' * space}pass\n")
        if instruction == '[':
            file = file[len(instruction) :].lstrip()
            continue
        if instruction[0] == '[':
            file = file[1:].lstrip()
            continue
        if instruction[0] == ']':
            space -= 4
            file = file[1:].lstrip()
            continue
        if instruction.split(']')[0] not in allowed:
            instruction = instruction.split(']')[0]
            out.write(f"{' ' * space}{instruction}()\n")
            file = file[len(instruction) :].lstrip()
            continue
        file = file[len(instruction) :].lstrip()
        next_instruction = file.split(" ")[0]
        if '[' in next_instruction:
            next_instruction = next_instruction.partition("[")[0]
        if instruction == 'repeat':
            out.write(f"{' ' * space}{allowed[instruction.replace('[','')]}(1, {int(next_instruction)+1}):\n")
            space += 4
        elif next_instruction.isnumeric() or "'" in next_instruction or '+' in next_instruction:
            out.write(f"{' ' * space}t.{allowed[instruction.replace('[','')]}({next_instruction})\n")
        elif instruction == "to":
            space = 4
            out.write(f"{allowed[instruction]} {next_instruction}():\n")
        elif ']' in next_instruction:
            out.write(f"{' ' * space}t.{allowed[instruction.replace('[','')]}({next_instruction.replace(']','')})\n")
            space = 0
        else:
            out.write(f"{' ' * space}t.{allowed[instruction]}()\n")
            continue
        file = file[len(next_instruction) :].lstrip()
    out.write('turtle.done()\n')