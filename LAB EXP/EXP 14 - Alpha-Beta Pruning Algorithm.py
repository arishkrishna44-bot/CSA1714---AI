
def alphabeta(depth, node, alpha, beta, maximizing, scores):
    if depth == 2:
        return scores[node]

    if maximizing:
        best = float('-inf')

        for child in [node * 2, node * 2 + 1]:
            value = alphabeta(
                depth + 1, child, alpha, beta, False, scores
            )
            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = float('inf')

        for child in [node * 2, node * 2 + 1]:
            value = alphabeta(
                depth + 1, child, alpha, beta, True, scores
            )
            best = min(best, value)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


scores = [3, 5, 2, 9]
result = alphabeta(
    0, 0, float('-inf'), float('inf'), True, scores
)

print("Best score:", result)
