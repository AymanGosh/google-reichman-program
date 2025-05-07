from collections import deque

def mybfs(g,n):
    vis = set()
    q = deque()

    q.append(n)
    vis.add(n)
    print()
    while q:
        n = q.popleft()
        print(n, end=" ")
        for v in g[n]:
            if v not in vis:
                vis.add(v)
                q.append(v)

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)

            # Iterate over neighbors explicitly
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B', 'H'},
    'F': {'C'},
    'G': {'C'},
    'H': {'E'}
}

bfs(graph, 'A')
mybfs(graph, 'A')
