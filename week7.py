def number_of_lists(zoznam: list) -> int:
    return int(str(zoznam).count("["))


print(number_of_lists([1, "a", 2]))
print(number_of_lists([[], 1, "a", [3], 2]))
print(number_of_lists(["a", ["dom", [2], 3], [], [[[2]]], "b"]))
print(number_of_lists([1, "[]", 2]))
print(number_of_lists((1, 2)))


def get_elements(zoznam: list) -> tuple:
    asd = (
        str(zoznam)
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
        .replace(" ", "")
        .replace(",,", ",")
    )
    if asd[0] == ",":
        asd = ""
    else:
        asd = asd.split(",")
    return tuple([int(i) if i.isnumeric() else i for i in asd])


print(get_elements([1, 2, 3, [4, 5], 6, [[[7]]], [], 8]))
print(get_elements(["a", ["dom", [2], 3], [], [[[2]]], "b"]))
print(get_elements([[], [[[]]], []]))
zoz = [[[7]], 8]
print(get_elements(zoz))
print(zoz)


def flat_list(zoznam: list) -> None:
    return list(get_elements(zoznam))


zoz = [[[7]], 8]
print(flat_list(zoz))
p = [1, 2, 3, [4, 5], 6, [[[7]]], [], 8]
print(flat_list(p))


def nested_replace(zoznam: list, hodnota1, hodnota2) -> list:
    for i, v in enumerate(zoznam):
        if v == hodnota1:
            zoznam[i] = hodnota2
        elif isinstance(v, list):
            nested_replace(v, hodnota1, hodnota2)

    return zoznam


print(nested_replace([[[7]], 8], 7, "a"))
print(nested_replace([1, 2, 3, [1, 2], 3, [[[1]]], [], 2], 1, "x"))
print(nested_replace([3, [33, [333, [13], 13]], 36], 3, "q"))
print(nested_replace([3, [33, [333, [13], 13]], 36], [13], "m"))


def change_values(zoznam: list, hodnota1, hodnota2) -> list:
    return nested_replace(zoznam, hodnota1, hodnota2)


zoz = [[[7]], 8]
print(change_values(zoz, 7, "a"))
p = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]
print(change_values(p, 1, "x"))
p = [1, 2, 3, [1, 2], 3, [[[1]]], [], 2]
print(change_values(p, 4, "z"))
p = ["a", ["dom", [2], 3], [], [[[2]]], "b"]
print(change_values(p, 2, "abc"))
