# modulo para manejar la interfaz de consola y colores ANSI (American National Standards Institud)

# definir codigos ansi para colores
VERDE = "\033[92m"
ROJO = "\033[91m"
RESET = "\033[0m"
AZUL = "\033[94m"

def mostrar_encabezado():
    # titulo principal del juego
    print(AZUL + "\n========================================")
    print("  EL AHORCADO - EL DESAFIO DEL DR LIGHT ")
    print("========================================" + RESET)

def mostrar_menu():
    # mostrar las opciones del menu principal
    print("\n--- MENU PRINCIPAL ---")
    print("1. Registrar palabras")
    print("2. Iniciar partida")
    print("3. Salir del sistema")
    return input("Seleccione una opcion: ").strip()

def seleccionar_personaje():
    # permitir al usuario elegir entre mega man y zero
    print("\n--- SELECCION DE PERSONAJE ---")
    print("1. Mega Man")
    print("2. Zero")
    opcion = input("Elija su personaje (1 o 2): ").strip()
    if opcion == "2":
        return "Zero"
    return "Mega Man"

def mostrar_estado_partida(palabra_oculta, letras_incorrectas, intentos_restantes, personaje):
    # mostrar el estado actual del juego en pantalla
    print(f"\nPersonaje actual: {personaje}")
    print(f"Palabra oculta: {' '.join(palabra_oculta)}")
    
    # formatear letras incorrectas en rojo
    rojo_letras = [ROJO + l + RESET for l in letras_incorrectas]
    print(f"Letras incorrectas: {', '.join(rojo_letras)}")
    print(f"Intentos fallidos restantes: {intentos_restantes}/5")