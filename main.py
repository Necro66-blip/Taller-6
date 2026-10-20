
comentarios = []


def registrar_comentario():
    """Permite agregar un comentario a la lista."""
    texto = input("Escribe tu comentario: ").strip()

    if texto:
        comentarios.append(texto)
        print("¡Comentario guardado con éxito!")
    else:
        print("No puedes guardar un comentario vacío.")


def mostrar_comentarios():
    """Muestra los comentarios que se han guardado."""
    if not comentarios:
        print("Todavía no hay comentarios guardados.")
    else:
        print("\n--- LISTA DE COMENTARIOS ---")

        for i, texto in enumerate(comentarios, start=1):
            print(f"{i}. {texto}")


def buscar_comentarios():
    """Busca una palabra dentro de los comentarios."""
    if not comentarios:
        print("Primero debes registrar algún comentario.")
        return

    palabra = input("¿Qué palabra quieres buscar?: ").strip().lower()

    if not palabra:
        print("Debes escribir una palabra para buscar.")
        return

    encontrados = 0

    print("\n--- RESULTADOS DE LA BÚSQUEDA ---")

    for i, texto in enumerate(comentarios, start=1):
        if palabra in texto.lower():
            print(f"Comentario {i}: {texto}")
            encontrados += 1

    if encontrados == 0:
        print("No encontramos comentarios con esa palabra.")
    else:
        print(f"Encontramos {encontrados} comentario(s).")


def contar_palabras():
    """Cuenta las palabras de cada comentario."""
    if not comentarios:
        print("No hay comentarios para analizar.")
        return

    print("\n--- PALABRAS POR COMENTARIO ---")

    for i, texto in enumerate(comentarios, start=1):
        palabras = texto.split()
        print(f"Comentario {i}: tiene {len(palabras)} palabra(s).")


def contar_palabra():
    """Cuenta cuántas veces aparece una palabra en un comentario."""
    if not comentarios:
        print("Primero debes guardar un comentario.")
        return

    mostrar_comentarios()

    try:
        numero = int(input("Escribe el número del comentario: "))

        if numero < 1 or numero > len(comentarios):
            print("Ese número no corresponde a ningún comentario.")
            return

    except ValueError:
        print("Por favor, escribe un número entero.")
        return

    palabra = input("¿Qué palabra quieres contar?: ").strip().lower()

    if not palabra:
        print("Debes escribir una palabra.")
        return

    texto = comentarios[numero - 1].lower()
    cantidad = texto.count(palabra)

    print(f"La palabra aparece {cantidad} vez/veces.")

    if cantidad == 0:
        print("Esa palabra no aparece en el comentario.")


def mostrar_resumen():
    """Muestra información básica de un comentario."""
    if not comentarios:
        print("No hay comentarios para analizar.")
        return

    mostrar_comentarios()

    try:
        numero = int(input("Elige el número del comentario: "))

        if numero < 1 or numero > len(comentarios):
            print("El número que elegiste no es válido.")
            return

    except ValueError:
        print("Debes ingresar un número entero.")
        return

    texto = comentarios[numero - 1]

    palabra = input("Escribe una palabra para analizar: ").strip().lower()

    if not palabra:
        print("Debes escribir una palabra.")
        return

    caracteres = len(texto)
    palabras = len(texto.split())
    apariciones = texto.lower().count(palabra)

    # Guardamos los resultados en una tupla.
    resumen = (caracteres, palabras, apariciones)

    print("\n--- RESUMEN DEL COMENTARIO ---")
    print("Texto:", texto)
    print("Cantidad de caracteres:", resumen[0])
    print("Cantidad de palabras:", resumen[1])
    print(f"Veces que aparece '{palabra}':", resumen[2])
    print("Resumen completo:", resumen)


def mostrar_menu():
    """Presenta las opciones del programa."""
    print("\n========== ANALIZADOR DE COMENTARIOS ==========")
    print("1. Agregar un comentario")
    print("2. Ver todos los comentarios")
    print("3. Buscar una palabra")
    print("4. Contar las palabras de cada comentario")
    print("5. Contar una palabra en un comentario")
    print("6. Ver el resumen de un comentario")
    print("7. Salir del programa")


def main():
    """Se encarga de ejecutar el menú principal."""
    while True:
        mostrar_menu()
        opcion = input("¿Qué opción deseas elegir?: ").strip()

        if opcion == "1":
            registrar_comentario()
        elif opcion == "2":
            mostrar_comentarios()
        elif opcion == "3":
            buscar_comentarios()
        elif opcion == "4":
            contar_palabras()
        elif opcion == "5":
            contar_palabra()
        elif opcion == "6":
            mostrar_resumen()
        elif opcion == "7":
            print("¡Gracias por usar el analizador de comentarios!")
            break
        else:
            print("Esa opción no existe. Intenta nuevamente.")


if __name__ == "__main__":
    main()
```