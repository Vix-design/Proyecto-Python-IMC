# Datos personales

# string: nombre
nombre = input ("¿Cuál es tu nombre?").capitalize()

# string: apellido paterno
apellido_paterno = input ("¿Cuál es tu apellido paterno?").capitalize()

# string: apellido materno
apellido_materno = input ("¿Cuál es tu apellido materno?").capitalize()

# int: edad
edad = int(input("¿Cuál es tu edad?"))

# float: peso
peso = float(input("¿Cuál es tu peso?"))

# float: estatura
estatura = float(input("¿Cuál es tu estatura?"))

imc = peso / estatura ** 2 

print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno} | Edad: {edad} | Peso: {peso} kg | Estatura: {estatura} m | IMC: {imc:.2f}")
