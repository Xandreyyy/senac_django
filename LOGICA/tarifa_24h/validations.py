def date(ipt):
  def isLeapYear(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      return 29
    else: return 28
  def maxDaysInMonth(month):
    if(month == 2): return True
    elif(month == 4 or month == 6 or month == 9 or month == 11):
      return 30
    else: return 31

  validChars = [".", "/"]
  dataList = []
  yearOfCreation = 2023
  for i in range(len(validChars)):
    charIndex = ipt.find(validChars[i])
    if(charIndex >= 0):
      dataList = ipt.split(validChars[i])
  if(len(dataList) == 3):
    for j in range(len(dataList)): dataList[j] = int(dataList[j])
    if((dataList[1] == 2) and (dataList[0] <= isLeapYear(dataList[2])) and (dataList[2] >= yearOfCreation)):
      return dataList
    elif((dataList[0] <= maxDaysInMonth(dataList[1])) and (dataList[1] <= 12) and (dataList[2] >= yearOfCreation)):
      return dataList
    else: return False
  else: return False

def time(ipt):
  timeList = []
  ipt = ipt.strip()
  dotsIndex = ipt.find(":")
  if(dotsIndex == 2 and len(ipt) == 5):
    hourSlice = slice(0, dotsIndex)
    minSlice = slice(dotsIndex + 1, len(ipt))
    hours = ipt[hourSlice]
    mins = ipt[minSlice]
    try:
      hours = int(hours)
      mins = int(mins)
      if((hours <= 23) and (hours >= 0) and (mins >= 0) and (mins <= 59)):
        timeList = [hours, mins]
        return timeList
      else:
        return False
    except Exception as exc:
      print("O horário inserido não é válido!")
      print(exc)
      return False
  elif(len(ipt) <= 2):
    try:
      ipt = int(ipt)
      if(ipt >= 23):
        timeList = [ipt]
        return timeList
    except Exception as exc:
      print("O horário inserido não é válido!")
      print(exc)
      return False
  else: return False