# CODE:40
import interfaz

import csv
import random
import interfaz

def leer_palabra_secreta(palabras):
    with open(palabras, 'r') as csvfile:
        lista_palabras = list(csv.DictReader(csvfile)) 

    for palabra in lista_palabras:
        lista_palabras_oculta = palabra['palabras']
        print(lista_palabras_oculta)
    
    palabra_aleatoria = random.choice(lista_palabras)
    palabra_secreta = str(palabra_aleatoria['palabras'])
    return palabra_secreta

def pedir_letra(letras_usadas):
    while True:
        letra = str(input('ingrese una letra: ')).lower()
        if len(letra) != 1:
            print('introduce una letra sola.')
        elif letra in letras_usadas:
            pass
        else:
            letras_usadas.append(letra)
            break
    return letra
        
                 


def verificar_letra(letra, palabra_secreta):
    if letra in palabra_secreta:
        return True
    elif letra not in palabra_secreta:
        return False

def validar_palabra(letras_usadas, palabra_secreta):
    for i in palabra_secreta:
        if i in letras_usadas:
            continue
        elif i not in letras_usadas:
            return False
    return True

if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')

