import csv


class Paciente:

    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def mostrar_perfil_paciente(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")
        print(f"IMC: {self.calcular_imc():.2f}")

lista_pacientes = []

print("Leyendo de CSV")

try:
    with open('pacientes.csv', mode='r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)

        for fila in lector_csv:
            nuevo_paciente = Paciente(
                nombre=fila['nombre'],
                edad=int(fila['edad']),
                peso=float(fila['peso']),
                altura=float(fila['altura'])
            )
            lista_pacientes.append(nuevo_paciente)
      
except FileNotFoundError:
    print("No se encontró el archivo pacientes.csv")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")

if lista_pacientes:
    print("\nPerfiles de pacientes leídos del CSV:")
    for paciente in lista_pacientes:
        paciente.mostrar_perfil_paciente()