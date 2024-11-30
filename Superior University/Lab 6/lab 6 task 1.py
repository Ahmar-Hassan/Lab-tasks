def bfs_without_queue(graph, start):
    visited = []
    to_visit = [start]

    while to_visit:
        current = to_visit[0]
        del to_visit[0] 
        if current not in visited:
            print(current, end=" ")
            visited.append(current)
            to_visit.extend([node for node in graph[current] if node not in visited])

graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

bfs_without_queue(graph, 1)  
