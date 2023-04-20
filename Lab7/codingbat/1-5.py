def parrot_trouble(talking, hour):
  if hour < 7 and talking or hour > 20 and talking:
    return(True)
  else: return(False)