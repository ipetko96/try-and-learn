with open("logo-vstup") as file:
    file = file.read().replace("\n", " ")

# allowed = ["fd", "rt", "lt", "pu", "pd", "setpc", "setpw", "repeat", "to"]
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


while len(file) > 0:
    instruction = file.partition(" ")[0]
    file = file[len(instruction) :].lstrip()
    next_instruction = file.partition(" ")[0]
    if next_instruction.isnumeric() or "'" in next_instruction:
        print(f"t.{allowed[instruction]}({next_instruction})")
    else:
        print(f"t.{allowed[instruction]}()")
        continue
    file = file[len(next_instruction) :].lstrip()


# while len(file) > 0:
#     if file[1].isnumeric():
#         print(f"t.{file[0]}({file[1]})")
#         file.pop(0)
#         file.pop(0)
#     elif "'" in file[1]:
#         print(f"t.pencolor({file[1]})")
#         file.pop(0)
#         file.pop(0)
#     else:
#         print(f"t.{file[0]}()")
#         file.pop(0)
