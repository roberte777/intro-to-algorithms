def algo_4(X: list[int]):
    maxSoFar = 0
    maxEndingHere = 0
    for I in range (0, len(X)):
        maxEndingHere = max(0, maxEndingHere + X[I])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar
