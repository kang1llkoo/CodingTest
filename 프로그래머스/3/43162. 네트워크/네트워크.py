def dfs(node, visited, computers):
    visited[node] = 1
    for next_node in range(len(computers)):
        if not visited[next_node] and computers[node][next_node] == 1:
            dfs(next_node, visited, computers)

def solution(n, computers):
    visited = [0] * n
    networks = 0
    for node in range(n):
        if not visited[node]:
            dfs(node, visited, computers)
            networks += 1
    return networks