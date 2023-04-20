def lucky_sum(a, b, c):
  return a * (a != 13) + b * (b != 13 and a !=13) + c * (c != 13 and b != 13 and a != 13)
