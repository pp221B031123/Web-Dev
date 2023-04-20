def squirrel_play(temp, is_summer):
  if temp >= 60 and temp <= 90 + 10*is_summer:
    return True
  else: return False
