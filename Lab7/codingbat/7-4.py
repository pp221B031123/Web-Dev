def count_code(str):
  res = 0
  for i in range(len(str)):
    if str[i:i+2] == "co" and str[i+3:i+4] == 'e':
      res += 1
  return res