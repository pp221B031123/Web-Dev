def last2(str):
  c = str[-2:]
  res = 0
  for i in range(len(str)):
    if str[i:i+2] == c:
      res += 1
  return max(res-1,0)