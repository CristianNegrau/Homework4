# Scrieti un program in care user-ul trebuie sa introduca un numar intre 50 si 100.
# Daca introduce alt numar, printati "Your number is below 50" sau "Your number is above 100".
# Daca introduce litere, printati "You should enter a number"

user = input('Insert a number from 50 to 100:\n')

try:
  if int(user) < 50:
    print('Your number is below 50')
  elif int(user) > 100:
    print('Your number is above 100')
except ValueError:
  print('You should enter a number')
