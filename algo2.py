def find_median_sorted_arrays(A, B):
    if len(A) > len(B):
        A, B = B, A
    n, m = len(A), len(B)
    low, high = 0, n
    steps = []
    while low <= high:
        partitionA = (low + high) // 2
        partitionB = (n + m + 1) // 2 - partitionA
        maxLeftA = float('-inf') if partitionA == 0 else A[partitionA - 1]
        minRightA = float('inf') if partitionA == n else A[partitionA]
        maxLeftB = float('-inf') if partitionB == 0 else B[partitionB - 1]
        minRightB = float('inf') if partitionB == m else B[partitionB]
        steps.append({
            "partitionA": partitionA,
            "partitionB": partitionB,
            "maxLeftA": maxLeftA,
            "minRightA": minRightA,
            "maxLeftB": maxLeftB,
            "minRightB": minRightB
        })
