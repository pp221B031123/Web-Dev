def pos_neg(a, b, negative):
  if (a<0)^(b<0) and not negative or negative and a<0 and b<0:
    return True
  else:
    return False
