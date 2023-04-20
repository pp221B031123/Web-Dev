def in1to10(n, outside_mode):
  if n > 0 and n < 11 and not outside_mode:
    return True
  elif n < 2 and outside_mode or n > 9 and outside_mode:
    return True
  else: return False
