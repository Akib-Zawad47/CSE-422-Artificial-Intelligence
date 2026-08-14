def alpha_beta(node, depth, alpha, beta, isMax):

    if(depth == 0 or isinstance(node, int)):
        return node

    if(isMax):
        best = float('-inf')

        for child in node:
            value = alpha_beta(child, depth - 1, alpha, beta, False)
            best = max(best,value)
            alpha = max(best,alpha)

            if beta<= alpha:
                break

        return best

    else:

        best = float('inf')

        for child in node:
            value = alpha_beta(child, depth-1 , alpha, beta, True)
            best = min(best, value)
            beta = min(best,beta)

            if beta <= alpha:
                break

        return best


# Example game tree
tree = [
    [3, 5],
    [6, 9],
    [1, 2],
    [0, -1]
]

result = alpha_beta(
    tree,
    depth=2,
    alpha=float('-inf'),
    beta=float('inf'),
    isMax=True
)

print("Best value:", result)