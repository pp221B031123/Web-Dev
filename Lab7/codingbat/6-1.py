def make_bricks(small, big, goal):
  goal = max(goal%5, goal - big*5)
  if small < goal: return False
  else: return True
