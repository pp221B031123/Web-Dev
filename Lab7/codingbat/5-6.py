def alarm_clock(day, vacation):
  if day==6 or day==0:
    if vacation: return "off"
    else: return "10:00"
  elif vacation: return "10:00"
  else: return "7:00"
