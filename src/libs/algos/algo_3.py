#Recursive Function MaxSum
def algo_3(X: list[int], L: int, U: int) -> int:
    if L > U:
        return 0
    if L == U:
        return max(0, X[L])
    M = (L + U) // 2
    sum = 0
    maxToLeft = 0
    for I in range(M,L-1,-1):
        sum += X[I]
        maxToLeft = max(maxToLeft, sum)
    sum = 0
    maxToRight = 0
    for I in range(M+1,U+1):
        sum += X[I]
        maxToRight = max(maxToRight, sum)
    maxCrossing = maxToLeft + maxToRight

    maxInA = algo_3(X,L,M)
    maxInB = algo_3(X,M+1,U)
    return max(maxCrossing, maxInA, maxInB)




