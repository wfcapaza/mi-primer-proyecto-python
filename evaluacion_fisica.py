nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso en kg: "))
horas_ejercicio = float(input("Ingrese sus horas de ejercicio a la semana: "))

calorias_quemadas = horas_ejercicio * 350

if edad < 18:
    categoria = "Juvenil"
else:
    categoria = "Adulto"

if horas_ejercicio >= 3:
    estado = "Físicamente Activo"
else:
    estado = "Requiere mayor actividad física"

print("\n--- RESUMEN DE EVALUACIÓN FÍSICA ---")
print(f"Nombre: {nombre}")
print(f"Calorías quemadas estimadas por semana: {calorias_quemadas}")
print(f"Categoría: {categoria}")
print(f"Estado: {estado}")