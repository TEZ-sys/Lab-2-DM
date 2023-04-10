from collections import defaultdict
from heapq import heappop, heappush


def find_eulerian_cycle(graph):
    for vertex in graph:
        in_degrees, out_degrees = graph[vertex]
        if in_degrees != out_degrees:
            return None

    stack = [0]
    path = []
    while stack:
        vertex = stack[-1]
        in_degrees, out_degrees = graph[vertex]
        if out_degrees > 0:
            _, next_vertex, weight = heappop(out_degrees)
            graph[vertex][1] = out_degrees
            stack.append(next_vertex)
            path.append((vertex, next_vertex, weight))
        else:
            stack.pop()

    return path[::-1]


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        num_vertices = int(file.readline())
        graph = defaultdict(lambda: [0, []])
        for i in range(num_vertices):
            weights = list(map(int, file.readline().split()))
            for j, weight in enumerate(weights):
                if weight > 0:
                    graph[i][1].append((weight, j))
                    graph[j][0] += 1

    eulerian_cycle = find_eulerian_cycle(graph)
    if eulerian_cycle:
        total_weight = sum(weight for _, _, weight in eulerian_cycle)
        print(f'Ейлерів цикл: {" -> ".join(str(v) for v, _, _ in eulerian_cycle)}')
        print(f'Загальна вага: {total_weight}')
    else:
        print('Граф не має Ейлерівого циклу')