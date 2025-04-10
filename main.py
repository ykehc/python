# Esto es un comentario

print("Hola mundo\n")

# Tarea 1: imprime tu nombre junto a tu edad

print("Mi nombre es Cheky y tengo 19 años\n")

# Tema 2: Operaciones

print(f"{2 < 5} \n")

# Tema 2.1: Variables

nombre, edad = "Alexis", 25
print(f"Hola soy {nombre} y tengo {edad} anio \n")

# Tarea 2: Crea variables que contengan la informacion de nombre, ciudad y genero y imprima por cadena interpolada. (f"{insertar}")

nombre, ciudad, genero = "Cheky", "Las Guaranas", "macho"
print(f"Hola soy {nombre}, soy de {ciudad}, y soy un {genero} \n")

# Tema 2.2: Ingresar valores de usuario

nombre = input("Dame tu nombre: ")

print(f"Hola {nombre}!")

edad = int(input("Cual es tu edad: ")) # 25

edad = edad + 5 # 30

print(f"Tu edad en 5 anios seria {edad}")

# Tarea 3: Pidele al usuario el nombre y el apellido y su edad
nombre = input("Dame tu nombre: ")
apellido = input("Dame tu apellido: ")
print(f"Hola {nombre} {apellido}! \n")

edad = input("Cuantos veranos han pasado despues de tu nacimiento? ")

print(f"Ya veo. Tienes {edad} \n")

print(f"Entonces, tu eres {nombre} {apellido} y tienes {edad}. Wao men. \n")


# Tarea 4: Pidele al usuario 2 numeros y los sumes
print("Klk, somo calculadora basica patron, deme 2 numero ahi.")

# Int es para convertir cadenas de texto a numeros, brother 💀

num1 = int(input("Primer valor: "))
num2 = int(input("Segundo valor: "))

print(f"Entonces tu resultado final es: {num1 + num2}")