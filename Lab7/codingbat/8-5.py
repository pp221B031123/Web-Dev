def sum67(nums):
  ignore = False
  sum = 0
  for x in nums:
    if x == 6: ignore = True
    if not ignore: sum+=x
    if x == 7: ignore = False
  return sum
