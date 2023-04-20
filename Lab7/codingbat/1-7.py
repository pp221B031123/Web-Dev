def near_hundred(n):
  if abs(n-100) < 11 or abs(n-200) < 11:
    return True
  else:
    return False
