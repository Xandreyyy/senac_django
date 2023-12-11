from os import system
import validations as val
import datetime as dt

data = {
    "arrived_date": 0,
    "arrived_time": 0,
    "leave_date": 0,
    "leave_time": 0
}

def switch(value):
  parkingfee = int()
  if(value >= 5):
    parkingfee = 5
    return parkingfee
  elif(value <= 2):
    parkingfee = 10
    return parkingfee
  else:
    parkingfee = 11
    return parkingfee

def welcomeMsg():
  print(f"\t\t{'︵'*14}\n\t\t{'┃'}BEM-VINDO AO VIMAPARK!{'┃'}\n\t\t{'︶'*14}")
  print("Este é um serviço que calcula a tarifa do nosso estacionamento!\nEntão, por favor, insira as seguintes informações com este padrão:\n\t     HH:MM (horário) e DD.MM.AAA (dia)")
  while True:
    start = input('\nDigite "ok" se você entendeu e deseja continuar, ou "q" para sair: \n').casefold()
    if(start == "q"):
      break
    elif(start == "ok"):
      system("cls")
      inputFields()
      calcFee()
      return
    else:
      system("cls")
      print('Insira apenas "ok" ou "q"!')

def addDate(iptDate):
  validChars = [".", "/"]

  for char in validChars:
    if(char in iptDate):
      dataList = iptDate.split(char)

  dataList = list(map(int, dataList))
  return dataList

def addTime(iptTime):
  timeList = iptTime.split(":")
  timeList = list(map(int, timeList))
  return timeList

def inputFields():
  while True:
    arriveDate = input("Insira a data atual: ")
    if(val.date(arriveDate) == True):
      data.update({"arrived_date": addDate(arriveDate)})

    arriveTime = input("Insira a hora atual: ")
    if(val.time(arriveTime) == True):
      data.update({"arrived_time": addTime(arriveTime)})

    print("VIMAPARK espera que você tenha se divertido! Para efetuar o pagamento\nda tarifa do estacionamento, por favor, insira as informações com o\nseguinte formato:\n\t\t HH:MM (horário) e DD.MM.AAA (dia)")

    leaveDate = input("\nInsira a data atual: ")
    if(val.date(leaveDate) == True):
      data.update({"leave_date": addDate(leaveDate)})

    leaveTime = input("Insira a hora atual: ")
    if(val.time(leaveTime) == True):
      data.update({"leave_time": addTime(leaveTime)})
      break

def convertMinToHours():
  arrivedMinutesValue = data["arrived_time"]
  leaveMinutesValue = data["leave_time"]
  arrivedMinutes = arrivedMinutesValue[1]
  leaveMinutes = leaveMinutesValue[1]
  totalMinutes = leaveMinutes + arrivedMinutes
  minutesInHours = totalMinutes / 60
  return int(minutesInHours)

def convertDaysToHours():
  arrivedDateValues = data["arrived_date"]
  leaveDateValues = data["leave_date"]
  arrivedDay = arrivedDateValues[0]
  leaveDay = leaveDateValues[0]

  if(arrivedDay == leaveDay): return False

  totalDays = leaveDay - arrivedDay
  daysInHours = totalDays * 24
  return daysInHours

def calcTotalHours():
  arrivedHoursValue = data["arrived_time"]
  leaveHoursValue = data["leave_time"]
  arrivedHours = arrivedHoursValue[0]
  leaveHours = leaveHoursValue[0]
  totalHours = 0

  if(convertDaysToHours() == False):
    totalHours = (leaveHours - arrivedHours) + convertMinToHours()
  else:
    totalHours = (leaveHours - arrivedHours) + convertMinToHours() + convertDaysToHours()

  if(totalHours % 1 != 0):
    return int(totalHours) + 1
  return int(totalHours)

def calcFee():
  parkingfee = switch(calcTotalHours())
  payment = calcTotalHours() * parkingfee
  return parkingfee, payment

def printResult():
  def numberToString(l, printType):
    string = str()
    match printType:
      case "date":
        string = '/'.join(map(str, l))
        return string
      case "time":
        string = dt.datetime.strptime(':'.join(map(str, l)), "%H:%M").time()
        return str(string)[:-3]

  #system("cls")
  print(f'{("="*33)}')
  print(f'┃    VIMAPARK ESTACIONAMENTO   \t┃')
  print(f'┃\t\t\t     \t┃')
  print(f"┃Data de chegada: {numberToString(data['arrived_date'], 'date')}\t┃")
  print(f"┃Hora de chegada: {numberToString(data['arrived_time'], 'time')}     \t┃")
  print(f"┃Data de saída: {numberToString(data['leave_date'], 'date')}    \t┃")
  print(f"┃Hora de chegada: {numberToString(data['leave_time'], 'time')}     \t┃")
  print(f'┃\t\t\t     \t┃')
  print(f'┃Taxa aplicada: R${calcFee()[0]}/h     \t┃')
  print(f'┃Total: R${calcFee()[1]}     \t\t┃')
  print(f'{("="*33)}')

welcomeMsg()
printResult()