#Realiza un examen con 3 preguntas que tú desees, el usuario deberá responder "Sí" o "No" y al final otorgarle 
# una calificación (la calificación se logra con una variable que inicia en 0 y por cada respuesta correcta incrementa 1)

# Definir usurio
usuario = {
    "nombre": "",
    "puntaje": 0
 }

# Preguntas
preguntas = [
  {"pregunta": "¿La Antártida es el lugar mas frío en la tierra?", "respuesta": ["sí", "si"]},
  {"pregunta": "¿La capital de Francia es Roma?", "respuesta": ["no"]},
  {"pregunta": "¿El agua es un mineral?", "respuesta": ["no"]}
]

# Función para realizar el examen
def examen(nombre):
  print(f"Bienvenido, {nombre}! Vamos a realizar una prueba de 3 preguntas.")
  print("Responde con 'Sí' o 'No' a las preguntas que salgan.")
  print("¡Buena suerte! \n")
  
# Mostrar preguntas
  for pregunta in preguntas:
    respuesta = input(pregunta["pregunta"] + " Sí/No: ").strip().lower()

    # Validar respuesta
    while respuesta not in ["sí", "si", "no"]:
      print("Respuesta inválida. Por favor, responde con 'Sí' o 'No'.")
      respuesta = input(pregunta["pregunta"] + " Sí/No: ").strip().lower()
    
    # Evaluar respuesta
    if respuesta in pregunta["respuesta"]:
      usuario["puntaje"] += 1

def main():
  usuario["nombre"] = input("Ingresa tu nombre: ")
  usuario_nombre = usuario["nombre"]
  examen(usuario_nombre)
  usuario_puntaje = usuario["puntaje"]
  if usuario_puntaje == 3:
   print(f"¡Felicidades, {usuario_nombre}! Tu puntaje es de {usuario_puntaje}/3 es ¡PERFECTO! :D")
  elif usuario_puntaje == 2:
    print(f"¡Felicidades, {usuario_nombre}! Tu puntaje es de {usuario_puntaje}/3. ¡Casi perfecto! :)")
  else:
    print(f"Necesitas Mejorar! Tu puntaje es de {usuario_puntaje}/3. ¡Sigue intentando! :(")

main()
  
