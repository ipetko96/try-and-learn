"""
A-6-B-3-F
|  /|\  |
1 2 2 5 5
|/  |  \|
D-1-E-5-C
"""

graph = {
    "A": [("B", 6), ("D", 1)],
    "B": [("A", 6), ("C", 5), ("D", 2), ("E", 2), ("F", 3)],
    "C": [("B", 5), ("E", 5), ("F", 5)],
    "D": [("A", 1), ("B", 2), ("E", 1)],
    "E": [("B", 2), ("C", 5), ("D", 1)],
    "F": [("C", 5), ("B", 3)],
}

unvisited = [node for node in graph]
visited = []
infinity = 10**6

table = {node: [infinity, None] for node in graph}
table["A"][0] = 0

while len(unvisited) != 0:
    i = None
    smallest = infinity
    for k in table:
        if k not in unvisited:
            continue
        if table[k][0] < smallest:
            i = k
    for j in graph[i]:
        if i not in unvisited:
            continue
        if table[i][0] + j[1] < table[j[0]][0]:
            table[j[0]][0] = table[i][0] + j[1]
            table[j[0]][1] = i
    visited.append(i)
    unvisited.remove(i)
for i in table:
    print(i, table[i])
