def rotate_left3(nums):
  x = nums.pop(0)
  nums.append(x)
  return nums
