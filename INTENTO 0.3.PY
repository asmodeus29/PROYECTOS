import random
import hashlib
import sys
class CredencialesIncorrectasError(Exception):
  pass
# Parte para hacer el hash de la contraseña del usuario
def hash_password(password):
  # crear un objeto de has SHA-256
  sha256 = hashlib.sha256()
  # Conveetir la contraseña en bytes y agregarla al obejto de hash
  sha256.update(password.encode("utf-8"))
  # obtener la representacion en hexadecimal del has
  hashed_password = sha256.hexdigest()
  # devolver la contraseña encriptada
  return hashed_password

# -----------------INICIO DE SECCION-----------
def login():
  # valores predeterminados de usuario y contraseña
  usuario_predeterminado = "admin"
  contraseña_predeterminada = hash_password("12345")
  while True:
  # al usuario que ingrese el usuario y contraseña
      usuario_ingresado = input("Nombre de Usuario: ")
      contraseña_ingresada = input("Contraseña: ")

  # Encripta la contraseña ingresada para compararla con la almacenada
      contraseña_encriptada = hash_password(contraseña_ingresada)

  # Verificar si los datos ingresados coinciden
      if usuario_ingresado == usuario_predeterminado and contraseña_encriptada == contraseña_predeterminada:
         print("Inicio de sesion exitosa")
         return
    # Si no estan correctas 
  
      print("Crecenciales Incorrectas. Intenta nuevamente") 
    
try:
 login()
except CredencialesIncorrectasError as e:
  print(str(e))
  sys.exit()
print("----------------------------")
print("----------------------------")
print(  " ☞ BIENVENIDO A MI CODIGO"  )
print("----------------------------")
print("  ☞ SIGUE LAS INSTRUCCIONES  ")
print("   ☞ DISFRUTA EL PROGRAMA    ")
print("----------------------------")
print("----------------------------")
print("Este Codigo tiene la funcion de encriptar un mensaje ")
print("que se ingrese y ademas genera una llave de acuerdo la longitud del texto! ")
print("----------------------------")
print("----------------------------")
# Inicia Funcion de cifrado 
def generar_clave(longitud):
    clave = [random.randint(0, 150) for _ in range(longitud)]  # Genera una lista de números aleatorios
    return bytes(clave)  # Convierte la lista de números en un objeto de bytes

def encriptar(mensaje, clave):
    mensaje_bytes = mensaje.encode()  # Convierte el mensaje en una secuencia de bytes
    mensaje_encriptado = bytes(a ^ b for a, b in zip(mensaje_bytes, clave))  # Aplica XOR utilizando comprensión de listas
    return mensaje_encriptado

while True:
 def desencriptar(mensaje_encriptado, clave):
    mensaje_desencriptado = bytes(a ^ b for a, b in zip(mensaje_encriptado, clave))  # Aplica XOR utilizando comprensión de listas
    return mensaje_desencriptado.decode()  # Convierte la secuencia de bytes en una cadena de texto

#Obtener el mensaje y la longitud de la clave
 mensaje = input("Ingrese el mensaje a Encriptar: ")
 longitud_clave = len(mensaje)

#Generar la clave aleatoria del mismo tamaño que el mensaje
 clave = generar_clave(longitud_clave)

#Encriptar el mensaje utilizando la clave generada
 mensaje_encriptado = encriptar(mensaje, clave)

#Desencriptar el mensaje encriptado utilizando la misma clave
 mensaje_desencriptado = desencriptar(mensaje_encriptado, clave)
 
 #Imprimir los resultados
 print("----------------------------")
 print("----------------------------")
 print("----------------------------")
 print("Mensaje original:", mensaje)
 print("Mensaje encriptado:", mensaje_encriptado) 
 print("Mensaje desencriptado:", mensaje_desencriptado)
 print("----------------------------")
 print("----------------------------")
 print("----------------------------")

 continuar = input("¿Desea continuar? (s/n): ")
 if continuar.lower() == 'n':
  print("Ejecución finalizada.")
  break
