def check_if_exist(arr: List[int]) -> bool:
    s = set()
    for x in arr:
        if 2 * x in s or (x % 2 == 0 and x // 2 in s):
            return True
        s.add(x)
    return False
