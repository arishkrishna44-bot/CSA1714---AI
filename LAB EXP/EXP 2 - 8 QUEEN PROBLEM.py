from itertools import permutations

n = 8

for position in permutations(range(n)):

    valid = True

    for i in range(n):
        for j in range(i + 1, n):

            if abs(position[i] - position[j]) == abs(i - j):
                valid = False
                break

        if not valid:
            break

    if valid:
        for i in range(n):
            for j in range(n):
                if position[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()

        break
