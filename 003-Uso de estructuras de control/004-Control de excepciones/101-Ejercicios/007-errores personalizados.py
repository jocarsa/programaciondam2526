dividendo = 4
divisor = 0

try:
  division = dividendo/divisor
except ZeroDivisionError:
  print("Tienes un error de division por cero")
except Exception as mierror:
  print("Hay un error")
  print(mierror)
