# Datos personales

# string: nombre
nombre = input ("¿Cuál es tu nombre?")

# string: apellido paterno
apellido_paterno = input ("¿Cuál es tu apellido paterno?")

# string: apellido materno
apellido_materno = input ("¿Cuál es tu apellido materno?")

# int: edad
edad = int(input("¿Cuál es tu edad?"))

# float: peso
peso = float(input("¿Cuál es tu peso?"))

# float: estatura
estatura = float(input("¿Cuál es tu estatura?"))

imc = peso / estatura ** 2 

print("Bienvenido a la calculadora de IMC")
print(imc)