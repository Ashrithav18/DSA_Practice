from collections import deque

def bfsOfGraph(V, adj):
    visited = [False] * V
    queue = deque()
    result = []

    # Start from node 0
    queue.append(0)
    visited[0] = True

    while queue:
        node = queue.popleft()
        result.append(node)

        # Traverse neighbors
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result


# ----------- MAIN PROGRAM -----------

adj = [[2,3,1], [0], [0,4], [0], [2]]
V = len(adj)

print(bfsOfGraph(V, adj))