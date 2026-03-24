def dfs(adj):
    n = len(adj)
    visited = [False] * n
    result = []

    def dfsUtil(node):
        visited[node] = True
        result.append(node)

        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfsUtil(neighbor)

    dfsUtil(0)   # start from node 0
    return result


# Example
adj = [[1,2], [0,2], [0,1,3,4], [2], [2]]
print(dfs(adj))