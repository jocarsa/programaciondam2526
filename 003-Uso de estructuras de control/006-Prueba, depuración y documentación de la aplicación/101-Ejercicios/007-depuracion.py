def hazDivision(dividendo,divisor):
  # Comprobamos si son números
  print("Entramos en la funcion")
  if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    print("parece que los parametros son numeros")
    # Comprobamos que el divisor no es cero
    if divisor != 0:
      print("parece que los puedo dividir")
      resultado = dividendo/divisor
      return resultado
    else:
      print("No puedo dividir porque el divisor es cero")
      resultado = 0
  else:
    print("Los parametros no son numeros, pero voy a intentar convertirlos")
    try:
      print("Intento convertir a numeros con exito")
      # Vamos a intentar convertirlo a numeros
      dividendo = float(dividendo)
      divisor = float(divisor)
      resultado = dividendo/divisor
      return resultado
    except:
      print("He intentado convertir a numeros, pero no he podido")
      return 0
  
print(hazDivision(4,"3"))

