# modulo para la logica principal del juego del ahorcado
import random #(ramdon es una libreria principal que genera datos pseudoaleatorios)
from .interfaz import VERDE, RESET

def seleccionar_palabra_aleatoria(lista_palabras):
    # seleccionar una palabra al azar de la lista usando random
    return random.choice(lista_palabras)

def inicializar_partida(palabra):
    # crear la estructura inicial de la palabra oculta y variables de control
    palabra_oculta = ["_" for _ in palabra]
    letras_correctas = set()
    letras_incorrectas = set()
    intentos_fallidos = 0
    return palabra_oculta, letras_correctas, letras_incorrectas, intentos_fallidos

def procesar_letra(letra, palabra, palabra_oculta, letras_correctas, letras_incorrectas, intentos_fallidos):
    # procesar y validar la letra ingresada por el jugador
    letra = letra.lower()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Debe ingresar una unica letra valida")
        return intentos_fallidos, False
        
    if letra in letras_correctas or letra in letras_incorrectas:
        print("Ya ha utilizado esta letra anteriormente")
        return intentos_fallidos, False
        
    if letra in palabra:
        letras_correctas.add(letra)
        print(VERDE + f"Correcto: la letra '{letra}' esta en la palabra" + RESET)
        # actualizar las posiciones correspondientes en verde
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_oculta[i] = VERDE + letra + RESET
        return intentos_fallidos, True
    else:
        letras_incorrectas.add(letra)
        intentos_fallidos += 1
        print(f"Incorrecto: la letra '{letra}' no esta en la palabra")
        return intentos_fallidos, True

def verificar_victoria(palabra_oculta):
    # comprobar si ya no quedan guiones bajos ocultos
    for item in palabra_oculta:
        if "_" in item:
            return False
    return True