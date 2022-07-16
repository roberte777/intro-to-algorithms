#the one letter capital variable names from the project doc are confusing
# and not pythonic. hence, i am using i, j, k for the indices.
def algo_2(arr: list[int]):
    maxSoFar = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            maxSoFar = max(maxSoFar, sum)
    return maxSoFar

