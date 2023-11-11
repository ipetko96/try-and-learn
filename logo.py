with open("vstup") as file:
    file = file.read().replace("\n", " ").split()
print(file)

while len(file) > 0:
    if file[1].isnumeric():
        print(f"t.{file[0]}({file[1]})")
        file.pop(0)
        file.pop(0)
    elif "'" in file[1]:
        print(f"t.pencolor({file[1]})")
        file.pop(0)
        file.pop(0)
    else:
        print(f"t.{file[0]}()")
        file.pop(0)
