def centered_average(nums):
    nums.sort()
    sum = 0
    for x in range(1, len(nums) - 1):
        sum += nums[x]

    return sum / (len(nums) - 2)
