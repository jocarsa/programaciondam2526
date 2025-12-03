try:
    numero = int("hola")  # Intentamos convertir texto no numérico a entero
    print("El número es:", numero)

except ValueError:
    print("❌ Error: valor no válido (no se puede convertir a número).")

finally:
    print("🔚 Fin del bloque try-except.")
