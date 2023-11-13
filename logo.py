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
while len(file) > 0:
    instruction = file.split(" ")[0]
    if instruction == '[]':
        print(f"{' ' * space}pass")
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
        print(f"{' ' * space}{instruction}()")
        file = file[len(instruction) :].lstrip()
        continue
    file = file[len(instruction) :].lstrip()
    next_instruction = file.split(" ")[0]
    if '[' in next_instruction:
        next_instruction = next_instruction.partition("[")[0]
    elif instruction == 'repeat':
        print(f"{' ' * space}{allowed[instruction.replace('[','')]}(1, {int(next_instruction)+1}):")
        space += 4
    elif next_instruction.isnumeric() or "'" in next_instruction or '+' in next_instruction:
        print(f"{' ' * space}t.{allowed[instruction.replace('[','')]}({next_instruction})")
    elif instruction == "to":
        space = 4
        print(f"{allowed[instruction]} {next_instruction}():")
    elif ']' in next_instruction:
        print(f"{' ' * space}t.{allowed[instruction.replace('[','')]}({next_instruction.replace(']','')})")
        space = 0
    else:
        print(f"{' ' * space}t.{allowed[instruction]}()")
        continue
    file = file[len(next_instruction) :].lstrip()
