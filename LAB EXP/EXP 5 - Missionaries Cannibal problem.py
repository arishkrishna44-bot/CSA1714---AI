from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Missionaries should not be outnumbered
    if m > 0 and m < c:
        return False

    # Other side of the river
    m2 = 3 - m
    c2 = 3 - c

    if m2 > 0 and m2 < c2:
        return False

    return True


def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution:")
            for p in path:
                print(p)
            return

        # Possible boat movements
        moves = [(1, 0), (2, 0), (0, 1),
                 (0, 2), (1, 1)]

        for dm, dc in moves:
            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            if is_valid(new_state[0], new_state[1]) \
                    and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))


solve()
