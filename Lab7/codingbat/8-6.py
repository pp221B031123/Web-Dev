def has22(nums):
  prev = 0
  for x in nums:
    if x == 2 and prev == 2: return True
    prev = x
  return False
