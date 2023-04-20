def close_far(a, b, c):
  if abs(a-b)<2 and abs(c-a)>1 and abs(c-b)>1 or abs(a-c)<2 and abs(b-a)>1 and abs(c-b)>1:
    return True
  else: return False
