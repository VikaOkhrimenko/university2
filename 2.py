def find_numbers(nums: List[int]) -> int:
    def digits_count(x: int) -> int:
        c = 0
        while x > 0:
            c += 1
            x //= 10
        return c

    ans = 0
    for x in nums:
        if digits_count(x) % 2 == 0:
            ans += 1
    return ans
