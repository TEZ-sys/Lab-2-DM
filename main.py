import numpy as np

def find_eulerian_cycle(graph):

    num_vertices = len(graph)
    eulerian_cycle = []
    stack = [0]

    while stack:
        u = stack[-1]
        if any(graph[u]):
            v = 0
            while v < num_vertices and graph[u][v] == 0:
                v += 1

            eulerian_cycle.append((u, v))
            graph[u][v] = 0
            graph[v][u] = 0
            stack.append(v)
        else:
            stack.pop()

    return eulerian_cycle

def read_graph_from_txt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_vertices = int(lines[0])
        graph = np.zeros((num_vertices, num_vertices), dtype=int)
        for i in range(1, len(lines)):
            weights = lines[i].strip().split()
            for j in range(len(weights)):
                graph[i-1][j] = int(weights[j])
    return graph


file_path = 'input.txt'
graph = read_graph_from_txt(file_path)
eulerian_cycle = find_eulerian_cycle(graph)
print("Eulerian Cycle:")
for edge in eulerian_cycle:
    print(f"{edge[0]} -> {edge[1]}")
