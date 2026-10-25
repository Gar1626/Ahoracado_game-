# Este modulo es para gestionar el registro y validacion de palabras

def validar_palabra(palabra):
    # se verifica que la palabra solo contenga letras y no este vacia
    return palabra.isalpha() and len(palabra) > 0

def registrar_palabras():
    # registrar 10 palabras validas y unicas en una lista
    lista_palabras = []
    print("\n--- REGISTRO DE PALABRAS ---")
    while len(lista_palabras) < 10:
        palabra = input(f"Ingrese la palabra {len(lista_palabras) + 1} (solo letras): ").strip().lower()
        if not validar_palabra(palabra):
            print("Error: la palabra debe contener unicamente letras y no estar vacia")
            continue
        if palabra in lista_palabras:
            print("Error: esta palabra ya fue registrada, ingrese una diferente")
            continue
        lista_palabras.append(palabra)
        print("Palabra registrada exitosamente")
    return lista_palabras