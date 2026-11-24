
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def depth_limited_search(node, goal, limit, path):
    path.append(node)

    if node == goal:
        return True

    if limit == 0:
        path.pop()
        return False

    for child in graph[node]:
        if depth_limited_search(child, goal, limit - 1, path):
            return True

    path.pop()
    return False

def iddfs(start, goal, max_depth):
    for depth in range(max_depth + 1):
        path = []

        if depth_limited_search(start, goal, depth, path):
            return path

    return None

start = 'A'
goal = 'G'

path = iddfs(start, goal, 5)

if path:
    print("Path:", " -> ".join(path))
else:
    print("Goal not found")
