def count_hi(str):
  res = 0
  for i in range(len(str)):
    if str[i:i+2] == 'hi':
      res +=1
  return res
