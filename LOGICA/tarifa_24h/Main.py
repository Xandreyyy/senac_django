from os import system
import pprint as pp
import validations as val
# import datetime as dt

parkingfee = 0
data = {
    "arrived_date": 0,
    "arrived_time": 0,
    "leave_date": 0,
    "leave_time": 0
}

def switch(value):
  global parkingfee
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

def inputFields():
  while True:
    arriveDate = input("Insira a data atual: ")
    if(val.date(arriveDate) == False):
      print("Data inválida!")
      continue
    else:
      data.update({"arrived_date": val.date(arriveDate)})
      pp.pp(data)

    arriveTime = input("Insira a hora atual: ")
    if(val.time(arriveTime) == False):
      print("Hora inválida!")
      continue
    else:
      data.update({"arrived_time": val.time(arriveTime)})
      print("Obrigado! Divirta-se no VIMAPARK!")
      system("cls")

    print("VIMAPARK espera que você tenha se divertido! Para efetuar o pagamento\nda tarifa do estacionamento, por favor, insira as informações com o\nseguinte formato:\n\t\t HH:MM (horário) e DD.MM.AAA (dia)")
    pp.pp(data)
    leaveDate = input("\nInsira a data atual: ")
    if(val.date(leaveDate) == False):
      print("Data inválida!")
      continue
    else:
      data.update({"leave_date": val.date(leaveDate)})
      pp.pp(data)

    leaveTime = input("Insira a hora atual: ")
    if(val.time(leaveTime) == False):
      print("Hora inválida!")
      continue
    else:
      data.update({"leave_time": val.time(leaveTime)})
      pp.pp(data)
      break

# def validarData(ipt):
#   padraoData = '%d.%m.%Y %H:%M'
#   data = '21.02.2005 14:45'
#   return dt.datetime.strptime(data, padraoData)

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
  payment = calcTotalHours() * switch(calcTotalHours())
  return payment

def printResult():
  def numberToString(l, printType):
    string = str()
    match printType:
      case "date":
        for num in range(len(l)):
          l[num] = str(l[num])
          if(num < 2): string += f"{l[num]}/"
          else: string += f"{l[num]}"
        return string
      case "time":
        for num in range(len(l)):
          l[num] = str(l[num])
          if(num == 0):
            string += f"{l[num]}:"
          else: string += f"{l[num]}"
        return string

  system("cls")
  print(f'{("="*33)}')
  print(f'┃    VIMAPARK ESTACIONAMENTO   \t┃')
  print(f'┃\t\t\t     \t┃')
  print(f"┃Data de chegada: {numberToString(data['arrived_date'], 'date')}\t┃")
  print(f"┃Hora de chegada: {numberToString(data['arrived_time'], 'time')}     \t┃")
  print(f"┃Data de saída: {numberToString(data['leave_date'], 'date')}    \t┃")
  print(f"┃Hora de chegada: {numberToString(data['leave_time'], 'time')}     \t┃")
  print(f'┃\t\t\t     \t┃')
  print(f'┃Taxa aplicada: R$5/h     \t┃')
  print(f'┃Total: R$100     \t\t┃')
  print(f'{("="*33)}')

welcomeMsg()
printResult()