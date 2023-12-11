def date(ipt):
  # retorna quantidade de dias de fevereiro
  def daysInLeapYear(year):
    # li na wikipedia, mas não entendi 100% este teste
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      return 29
    else: return 28

  def maxDaysInMonth(month):
    if(month == 2): return daysInLeapYear(dataList[2])
    elif(month in [4, 6, 9, 11]): return 30
    else: return 31

  validChars = [".", "/"]
  yearOfCreation = 2023
  dataList = list()

  for char in validChars:
    if(char in ipt):
      dataList = ipt.split(char)

  if(len(dataList) == 3):
    dataList = list(map(int, dataList))

    if(1 <= dataList[0] <= maxDaysInMonth(dataList[1])) and (1 <= dataList[1] <= 12) and (dataList[2] >= yearOfCreation):
      return True
    else: return False

  else: return False

def time(ipt):
  try:
    if(ipt.find(":") in range(1, 3)):
      ipt = ipt.split(":")
      hours, mins = ipt[0], ipt[1]
      hours = int(hours)
      mins = int(mins)
      if(1 <= hours < 24 and 0 <= mins < 60):
        return True
      else:
        print("Hora inválida!")
        return False
    else:
      print("Formato inválido! Insira: HH:MM")
      return False
  except ValueError:
    print("Insira apenas dígitos!")
    return False