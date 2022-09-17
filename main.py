#   Texto de bienvenida para quien juegue la trivia
print ("Hola, bienvenid@ a la trivia sobre astronomía:\n")
nombre = input("Ingresa tu nombre:")

print ("Pondremos a prueba tus conocimientos:\n")

#  Instrucciones sobre cómo jugar:
print ("Acontinuación responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n")

# Pregunta 1
print ("1) ¿Como se llamaba la primera nave tripulada?")
print ("a) Apolo 11")
print ("b) LEXX")
print ("c) PTK-NP")
print ("d) Vostok 1")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")
if respuesta_1 == "d":
  print("Excelente! Es correcto!\n")
else: 
  print("Oh no! Incorrecto!:\n")

# Pregunta 2
print ("2) ¿Como se llamaba el primer astronauta que pisó la luna")
print ("a) Buzz Aldrich")
print ("b) Yuri Gagarin")
print ("c) Neil Armstrong")
print ("d) Buzz Lightyear")

# Almacenamos la respuesta del usuario en la variable "respuesta_2"
respuesta_2 = input("\nTu respuesta: ")
if respuesta_2 == "c":
  print("Excelente! Es Correcto!\n")
else: 
  print("Oh no! Incorrecto \n")

# Pregunta 3
print ("3) ¿Cómo se llama la galaxia a la que pertenecemos?")
print ("a) Andromeda")
print ("b) Vía Lactea")
print ("c) Maffei")
print ("d) Centaurus")

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3 = input("\nTu respuesta: ")
if respuesta_3 == "b":
  print("Excelente! Es correcto!\n")
else: 
  print("Oh no! Incorrecto!:\n")
