
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(dist)
visited = [False] * n
current = 0
visited[current] = True
path = [current]
cost = 0

while len(path) < n:
    next_city = -1
    min_cost = float('inf')

    for city in range(n):
        if not visited[city] and dist[current][city] < min_cost:
            min_cost = dist[current][city]
            next_city = city

    cost += min_cost
    current = next_city
    visited[current] = True
    path.append(current)

cost += dist[current][0]
path.append(0)

print("Tour:", path)
print("Total Cost:", cost)
