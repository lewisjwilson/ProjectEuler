graph = {0: [3],
         1: [7, 4],
         2: [2, 4, 6],
         3: [8, 5, 9, 3]}

edges = {}


def populateEdges():
    keys = []
    for d in graph:
        for w in graph[d]:
            if d not in keys:
                edges[d] = graph[d][w]
            else:
                edges[d].append(graph[d][w])


populateEdges()
