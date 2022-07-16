#the one letter capital variable names from the project doc are confusing
# and not pythonic. hence, i am using i, j, k for the indices.
def algo_1(X: list[int]) -> int:
    maxSoFar = 0
    for L in range(len(X)):
        for U in range (L, len(X)):
            sum=0
            for I in range(L,U+1):
                sum+=X[I]
            maxSoFar = max(maxSoFar, sum)
    return maxSoFar
