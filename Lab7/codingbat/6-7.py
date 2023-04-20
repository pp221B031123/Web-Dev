def make_chocolate(small, big, goal):
  goal = max(goal%5, goal - big*5)
  if small < goal: return -1
  else: return goal
