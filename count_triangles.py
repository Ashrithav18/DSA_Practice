def countTriangles(graph, isDirected):
    V = len(graph)
    count = 0

    # Check all triplets (i, j, k)
    for i in range(V):
        for j in range(V):
            for k in range(V):
                
                # Check triangle condition
                if graph[i][j] and graph[j][k] and graph[k][i]:
                    count += 1

    # Divide based on graph type
    if isDirected:
        return count // 3
    else:
        return count // 6


# Example (Directed Graph)
graph = [
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0]
]

print("Triangles:", countTriangles(graph, True))