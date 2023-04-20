def lone_sum(a, b, c):
  aa = a
  bb = b
  cc = c
  if a == b or a == c: aa = 0
  if b == a or b == c: bb = 0
  if c == a or c == b: cc = 0
  return aa + bb + cc
