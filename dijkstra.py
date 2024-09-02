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
    neighbors = None
    smallest = infinity
    for node in table:
        if node not in unvisited:
            continue
        if table[node][0] < smallest:
            neighbors = node
    for neighbor in graph[neighbors]:
        if neighbors not in unvisited:
            continue
        if table[neighbors][0] + neighbor[1] < table[neighbor[0]][0]:
            table[neighbor[0]][0] = table[neighbors][0] + neighbor[1]
            table[neighbor[0]][1] = neighbors
    visited.append(neighbors)
    unvisited.remove(neighbors)
for neighbors in table:
    print(neighbors, table[neighbors])
