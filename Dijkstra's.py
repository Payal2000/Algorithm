# Description: Dijkstra's algorithm
import sys
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if distances[current_vertex] < current_distance:
            continue

        for neighbour, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(queue, [distance, neighbour])

    return distances

if __name__ == '__main__':

    graph = {
        'A': {'B': 8, 'C': 1, 'D': 2},
        'B': {},
        'C': {'B': 5, 'D': 2},
        'D': {'E': 3, 'F': 5},
        'E': {'F': 1},
        'F': {'A': 5}
    }

    print(dijkstra(graph, 'A'))

