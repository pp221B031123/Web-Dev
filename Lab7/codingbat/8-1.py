def count_evens(nums):
    res = 0
    for x in nums:
        if not x % 2: res += 1

    return res

