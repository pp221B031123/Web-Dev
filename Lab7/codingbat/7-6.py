def xyz_there(str):
  if str[:3] == 'xyz': return True
  for i in range(1, len(str)):
    if str[i:i+3] == 'xyz' and str[i-1:i] != '.': return True
  return False
