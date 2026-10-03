def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])


def solve_puzzle(state, goal):

    print("Initial State:")
    display(state)

    zero = state.index(0)

    # Move blank space to the right
    if zero % 3 < 2:
        new_pos = zero + 1
        state[zero], state[new_pos] = state[new_pos], state[zero]

    print("\nFinal State:")
    display(state)

    if state == goal:
        print("\nPuzzle Solved!")
    else:
        print("\nPuzzle Not Solved")


initial = [1, 2, 3,
           4, 5, 6,
           7, 0, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

solve_puzzle(initial, goal)
