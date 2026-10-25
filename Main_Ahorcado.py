"""
    >Bienvenidos al algoritmo que permite que el usuario jugar el juego Ahorcado utilizando palabra relacionadas a la 
robotica, tegnologia y videojuegos.
    >El jugador tendrá max 5 intentos fallidos para descubrir la palabra secreta 
    >Cada vez que el jugador ingrese una letra correcta, esta deberá aparecer en todas las 
posiciones correspondientes, utilizando un color diferente. Las letras incorrectas deberán 
mostrarse en rojo y, conforme se acumulen errores,. 
    >El juego finalizará cuando el jugador descubra la palabra completa o agote sus cinco 
intentos fallidos.
"""

from ahorcado_app.palabras import registrar_palabras
from ahorcado_app.interfaz import mostrar_encabezado, mostrar_menu, seleccionar_personaje, mostrar_estado_partida
from ahorcado_app.juego import seleccionar_palabra_aleatoria, inicializar_partida, procesar_letra, verificar_victoria

def main():
    # funcion principal que controla el ciclo de ejecucion del juego
    lista_palabras = []
    
    while True:
        mostrar_encabezado()
        opcion = mostrar_menu()
        
        if opcion == "1":
            lista_palabras = registrar_palabras()
        elif opcion == "2":
            if len(lista_palabras) < 10:
                print("\nDebe registrar 10 palabras antes de iniciar una partida")
                continue
                
            personaje = seleccionar_personaje()
            palabra_secreta = seleccionar_palabra_aleatoria(lista_palabras)
            palabra_oculta, letras_correctas, letras_incorrectas, intentos_fallidos = inicializar_partida(palabra_secreta)
            
            # bucle de la partida actual con limite de 5 intentos fallidos
            while intentos_fallidos < 5:
                mostrar_estado_partida(palabra_oculta, letras_incorrectas, 5 - intentos_fallidos, personaje)
                
                if verificar_victoria(palabra_oculta):
                    print(f"\n¡Victoria! Has descubierto la palabra secreta: {palabra_secreta}")
                    break
                    
                letra_ingresada = input("\nIngrese una letra: ").strip()
                intentos_fallidos, valido = procesar_letra(
                    letra_ingresada, palabra_secreta, palabra_oculta, 
                    letras_correctas, letras_incorrectas, intentos_fallidos)
                
                if verificar_victoria(palabra_oculta):
                    mostrar_estado_partida(palabra_oculta, letras_incorrectas, 5 - intentos_fallidos, personaje)
                    print(f"\n¡Victoria! Has descubierto la palabra secreta: {palabra_secreta}")
                    break
            
            if intentos_fallidos >= 5 and not verificar_victoria(palabra_oculta):
                print(f"\nDerrota: Has agotado tus 5 intentos fallidos")
                print(f"La palabra secreta era: {palabra_secreta}")
                
        elif opcion == "3":
            print("\nSaliendo del sistema del Dr Light. ¡Hasta pronto!")
            break
        else:
            print("\nOpcion invalida, seleccione un numero del 1 al 3")

if __name__ == "__main__":
    main()