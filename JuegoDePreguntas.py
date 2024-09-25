import random
#Definir diccionario con preguntas definidas como tuplas 
cuestionario = {
    "Historia": [
        ("¿En qué año comenzó la Primera Guerra Mundial?", 
         ("A) 1914", "B) 1918", "C) 1920", "D) 1939"), 
         "a"),
        ("¿Quién fue el primer presidente de los Estados Unidos?", 
         ("A) Abraham Lincoln", "B) Thomas Jefferson", "C) George Washington", "D) John Adams"), 
         "c"),
        ("¿Qué civilización construyó las pirámides de Egipto?", 
         ("A) Romanos", "B) Griegos", "C) Egipcios", "D) Persas"), 
         "c"),
        ("¿Qué famosa revolución comenzó en 1789?", 
         ("A) Revolución Americana", "B) Revolución Francesa", "C) Revolución Industrial", "D) Revolución Rusa"), 
         "b"),
        ("¿Quién fue el líder del movimiento independentista de la India?", 
         ("A) Nelson Mandela", "B) Simón Bolívar", "C) Mahatma Gandhi", "D) Winston Churchill"), 
         "c"),
        ("¿En qué país ocurrió la Revolución Industrial?", 
         ("A) Alemania", "B) Francia", "C) Inglaterra", "D) Estados Unidos"), 
         "c"),
        ("¿Qué famoso barco se hundió en 1912 tras chocar con un iceberg?", 
         ("A) Queen Mary", "B) Lusitania", "C) Titanic", "D) Britannic"), 
         "c"),
        ("¿Quién fue el primer hombre en pisar la Luna?", 
         ("A) Yuri Gagarin", "B) Neil Armstrong", "C) Buzz Aldrin", "D) John Glenn"), 
         "b"),
        ("¿En qué año llegó Cristóbal Colón a América?", 
         ("A) 1492", "B) 1500", "C) 1453", "D) 1519"), 
         "a"),
        ("¿Qué país construyó la Gran Muralla?", 
         ("A) Japón", "B) China", "C) India", "D) Corea"), 
         "b"),
    ],
    "Geografía y Ciencias": [
        ("¿Cuál es el océano más grande del mundo?", 
         ("A) Océano Atlántico", "B) Océano Índico", "C) Océano Pacífico", "D) Océano Ártico"), 
         "c"),
        ("¿En qué año llegó el hombre a la Luna por primera vez?", 
         ("A) 1965", "B) 1969", "C) 1972", "D) 1962"), 
         "b"),
        ("¿Cuál es el país con más habitantes del mundo?", 
         ("A) India", "B) Estados Unidos", "C) China", "D) Rusia"), 
         "c"),
        ("¿Quién pintó la famosa obra 'La última cena'?", 
         ("A) Miguel Ángel", "B) Rafael", "C) Leonardo da Vinci", "D) Donatello"), 
         "c"),
        ("¿Cómo se llama el lugar donde vive el Papa?", 
         ("A) Vaticano", "B) Jerusalén", "C) Roma", "D) Constantinopla"), 
         "a"),
        ("¿Qué invento es atribuido a Thomas Edison?", 
         ("A) El teléfono", "B) La bombilla eléctrica", "C) El avión", "D) El automóvil"), 
         "b"),
        ("¿Cuál es el metal más ligero?", 
         ("A) Aluminio", "B) Hierro", "C) Litio", "D) Cobre"), 
         "c"),
        ("¿En qué continente se encuentra el desierto del Sahara?", 
         ("A) Asia", "B) África", "C) América", "D) Oceanía"), 
         "b"),
        ("¿Cuál es el planeta más grande del sistema solar?", 
         ("A) Marte", "B) Júpiter", "C) Saturno", "D) Neptuno"), 
         "b"),
        ("¿Qué ciudad es conocida como 'La Gran Manzana'?", 
         ("A) París", "B) Londres", "C) Nueva York", "D) Los Ángeles"), 
         "c"),
    ]
}
#mostrar pregunta y opciones de respuesta 
def mostrar_pregunta(pregunta, opciones):
    print(f"\n{pregunta}")
    for opcion in opciones:
        print(opcion)
#leer respuesta del usuario 
def obtener_respuesta():
    return input("Ingrese su respuesta (o ingresa '0' para salir): ").lower()
#
def validar_respuesta(respuesta, respuesta_correcta):
    return respuesta == respuesta_correcta

def eliminar_pregunta(categoria, pregunta):
    cuestionario[categoria].remove(pregunta)
    if not cuestionario[categoria]:  # Si la categoría se queda sin preguntas, eliminarla
        del cuestionario[categoria]
#calcular puntuacion del usuario de 0 a 100%
def calcular_puntuacion(correctas, total_preguntas):
    return (correctas / total_preguntas) * 100

# Solicitar el nombre del usuario
nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(f"\nBienvenido/a {nombre_usuario} al juego de preguntas al azar\n")

correctas = 0
incorrectas = 0
total_preguntas = 0

for categoria in cuestionario:
    total_preguntas += len(cuestionario[categoria])
#seleccionar aleatoriamente pregunta y categoria mediante random.choice
while cuestionario:
    categoria = random.choice(list(cuestionario.keys()))  
    pregunta, opciones, respuesta_correcta = random.choice(cuestionario[categoria])  
    
    mostrar_pregunta(pregunta, opciones)  

    while True:  # Bucle para validar la respuesta ingresada por el usuario
        respuesta = obtener_respuesta()  # Obtener respuesta del usuario
        
        if respuesta == "0":  # Salir del juego
            if input("¿Estás seguro(a) que deseas salir? (si/no): ").lower() == "si":
                print("Saliendo del juego")
                exit() # Salir del juego
            else:
                print("¡Continuemos respondiendo las preguntas!")
                continue
        
        # Validar respuesta
        if respuesta in ["a", "b", "c", "d"]:
            break  # Salir del bucle si la respuesta es válida
        else:
            print("Opción no válida. Por favor, elige a, b, c o d.")

    # Validar respuesta correcta o incorrecta
    if validar_respuesta(respuesta, respuesta_correcta):
        print("Respuesta correcta")
        correctas += 1
    else:
        print("Respuesta incorrecta")
        incorrectas += 1

    # Eliminar la pregunta ya realizada de la categoría
    eliminar_pregunta(categoria, (pregunta, opciones, respuesta_correcta))

# Al terminar todas las preguntas calcular puntuacion 
puntuacion = calcular_puntuacion(correctas, total_preguntas)
print(f"\nHa terminado el juego. Respuestas correctas: {correctas}, Respuestas incorrectas: {incorrectas}")
print(f"Tu puntuación de 0 a 100% es: {puntuacion:.2f}%")

if correctas == total_preguntas:
    print("\n¡Felicitaciones! Has contestado todas las preguntas correctamente.")
