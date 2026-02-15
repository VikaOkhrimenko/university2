def duplicate_zeros(arr: List[int]) -> None:
    n = len(arr)
    zeros = 0
    for x in arr:
        if x == 0:
            zeros += 1
    i = n - 1
    j = n - 1 + zeros
    while i >= 0:
        if j < n:
            arr[j] = arr[i]
        if arr[i] == 0:
            j -= 1
            if j < n:
                arr[j] = 0
        i -= 1
        j -= 1
