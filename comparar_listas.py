import json
import os

def crear_lista(nombre_archivo):
    """Crea una lista de números de 8 dígitos y la guarda en un archivo JSON."""
    lista_numeros = []
    while True:
        numero = input("Ingresa un número de 8 dígitos (o escribe 'fin' para terminar): ")
        if numero.lower() == "fin":
            break
        try:
            numero = int(numero)
            if len(str(numero)) == 8:
                if numero in lista_numeros:
                    print("Error: Este número ya fue introducido.")
                else:  
                    lista_numeros.append(numero)
            else:
                print("Por favor, ingresa un número válido de 8 dígitos.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    with open(nombre_archivo, 'w') as archivo:
        json.dump(lista_numeros, archivo)
    print(f"Lista guardada en el archivo {nombre_archivo}")

def eliminar_lista(nombre_archivo):
    """Elimina un archivo de lista."""
    try:
        os.remove(nombre_archivo)
        print(f"Archivo {nombre_archivo} eliminado.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")

def comparar_listas():
    """Compara dos listas y muestra los números repetidos."""
    archivos_disponibles = [f for f in os.listdir() if f.endswith(".json")]

    if len(archivos_disponibles) < 2:
        print("No hay suficientes listas para comparar. Crea al menos dos listas.")
        return

    print("Archivos de listas disponibles:")
    for i, archivo in enumerate(archivos_disponibles):
        print(f"{i+1}. {archivo}")

    while True:
        try:
            indice_lista1 = int(input("Selecciona el número de la primera lista a comparar: ")) - 1
            indice_lista2 = int(input("Selecciona el número de la segunda lista a comparar: ")) - 1
            nombre_archivo1 = archivos_disponibles[indice_lista1]
            nombre_archivo2 = archivos_disponibles[indice_lista2]
            break
        except (IndexError, ValueError):
            print("Opción inválida. Por favor, selecciona un número de lista válido.")

    with open(nombre_archivo1, 'r') as archivo:
        lista1 = json.load(archivo)

    with open(nombre_archivo2, 'r') as archivo:
        lista2 = json.load(archivo)

    repetidos = set(lista1) & set(lista2)
    if repetidos:
        print("Números repetidos:")
        for numero in repetidos:
            print(numero)
    else:
        print("No se encontraron números repetidos.")

def ver_cantidad_numeros(nombre_archivo):
    """Muestra la cantidad de números en una lista."""
    try:
        with open(nombre_archivo, 'r') as archivo:
            lista = json.load(archivo)
        print(f"La lista {nombre_archivo} tiene {len(lista)} números.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")

def agregar_numero(nombre_archivo):
    """Agrega números a una lista existente."""
    try:
        with open(nombre_archivo, 'r') as archivo:
            lista_numeros = json.load(archivo)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
        return
    
    while True:
        numero = input("Ingresa un número de 8 dígitos (o escribe 'fin' para terminar): ")
        if numero.lower() == "fin":
            break
        try:
            numero = int(numero)
            if len(str(numero)) == 8:
                if numero in lista_numeros:
                    print("Error: Este número ya fue introducido.")
                else:
                    lista_numeros.append(numero)
            else:
                print("Por favor, ingresa un número válido de 8 dígitos.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    with open(nombre_archivo, 'w') as archivo:
        json.dump(lista_numeros, archivo)
    print(f"Lista {nombre_archivo} actualizada.")
    
def eliminar_numero(nombre_archivo):
    """Elimina un número de una lista existente."""
    while True:
        try:
            with open(nombre_archivo, 'r') as archivo:
                lista_numeros = json.load(archivo)
            break
        except FileNotFoundError:
            print(f"\nEl archivo {nombre_archivo} no se encontró.")
            nombre_archivo = input("\nIngrese el nombre del archivo (con extension .json): ")
        except json.JSONDecodeError:
            print(f"\nEl archivo {nombre_archivo} no se contiene un formato JSON válido.")
            nombre_archivo = input("\nIngrese el nombre del archivo (con extension .json): ")

    while True:
        while True:
            try:
                numero_a_eliminar = int(input("Ingresa el número de 8 dígitos que deseas eliminar: "))
                if len(str(numero_a_eliminar)) == 8:
                    break
                else:
                    print("Por favor, ingresa un número válido de 8 dígitos.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        if numero_a_eliminar in lista_numeros:
            lista_numeros.remove(numero_a_eliminar)
            with open(nombre_archivo, 'w') as archivo:
                json.dump(lista_numeros, archivo)
                print(f"Número {numero_a_eliminar} ha sido eliminado de la lista {nombre_archivo}.")
        else:
            print(f"El número {numero_a_eliminar} no se encontró en la lista {nombre_archivo}.")
        
        seguir_eliminando = input(f"Desea seguir eliminando otro número (s/n): ").lower()
        if seguir_eliminando != 's':
            break

def buscar_numero(nombre_archivo):
    """Busca un número en una lista y muestra si está presente."""
    while True:
        try:
            with open(nombre_archivo, 'r') as archivo:
                lista_numeros = json.load(archivo)
            break
        except FileNotFoundError:
            print(f"\nEl archivo {nombre_archivo} no se encontró.")
            nombre_archivo = input("\nIngrese el nombre del archivo (con extension .json): ")
        except json.JSONDecodeError:
            print(f"\nEl archivo {nombre_archivo} no se contiene un formato JSON válido.")
            nombre_archivo = input("\nIngrese el nombre del archivo (con extension .json): ")

    while True:
        while True:
            try:
                numero_a_buscar = int(input("Ingresa el número de 8 dígitos que deseas buscar: "))
                if len(str(numero_a_buscar)) == 8:
                    break
                else: 
                    print("Por favor, ingresa un número válido de 8 dígitos.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        if numero_a_buscar in lista_numeros:
            print(f"\nEl número {numero_a_buscar} está presente en la lista {nombre_archivo}.")
        else:
            print(f"\nEl número {numero_a_buscar} NO está presente en la lista {nombre_archivo}.")
            
        seguir_buscando = input("\n¿Desea seguir buscando otro número? (s/n): ").lower()
        if seguir_buscando != 's':
            break
        
def main():
    """Función principal del programa."""
    while True:
        print("\nOpciones:")
        print("1. Crear lista")
        print("2. Eliminar lista")
        print("3. Comparar listas")
        print("4. Ver cantidad de números")
        print("5. Agregar más números a la lista")
        print("6. Eliminar número")
        print("7. Buscar número")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre_archivo = input("Ingresa el nombre del archivo para la nueva lista (ej: 'lista1.json'): ")
            crear_lista(nombre_archivo)
        elif opcion == '2':
            nombre_archivo = input("Ingresa el nombre del archivo de la lista a eliminar: ")
            eliminar_lista(nombre_archivo)
        elif opcion == '3':
            comparar_listas()
        elif opcion == '4':
            nombre_archivo = input("Ingresa el nombre del archivo de la lista: ")
            ver_cantidad_numeros(nombre_archivo)
        elif opcion == '5':
            nombre_archivo = input("Ingresa el nombre del archivo de la lista a agregar: ")
            agregar_numero(nombre_archivo)
        elif opcion == '6':
            nombre_archivo = input("Ingresa el nombre del archivo de la lista donde eliminar el número: ")
            eliminar_numero(nombre_archivo)
        elif opcion == '7':
            nombre_archivo = input("Ingresa el nombre del archivo de la lista donde buscar el número: ")
            buscar_numero(nombre_archivo)
        elif opcion == '8':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()