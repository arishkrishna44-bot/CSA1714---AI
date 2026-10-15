
# Map Coloring using CSP

regions = ['A', 'B', 'C', 'D']

colors = ['Red', 'Green', 'Blue']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

coloring = {}

def is_valid(region, color):
    for neighbor in neighbors[region]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def solve():
    if len(coloring) == len(regions):
        return True

    for region in regions:
        if region not in coloring:
            for color in colors:
                if is_valid(region, color):
                    coloring[region] = color

                    if solve():
                        return True

                    del coloring[region]

            return False

    return True

if solve():
    print("Map Coloring Solution:")
    for region, color in coloring.items():
        print(region, ":", color)
else:
    print("No solution exists")
