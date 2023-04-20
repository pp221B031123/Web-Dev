def caught_speeding(speed, is_birthday):
  speed = speed - 5*is_birthday
  if speed <= 60: return 0
  elif speed >= 81: return 2
  else: return 1
