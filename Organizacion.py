participantes = {}
def ordenar_por_nombre(lista):
    lista_ordenada = lista[:]
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(n - 1):
            if lista_ordenada[j]['nombre'] > lista_ordenada[j + 1]['nombre']:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    return lista_ordenada
def ordenar_por_edad(lista):
    lista_ordenada = lista[:]
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(n - 1):
            if lista_ordenada[j]['edad'] > lista_ordenada[j + 1]['edad']:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    return lista_ordenada
while True:
    print("\n••• MENÚ •••")
    print("1. Agregar participante")
    print("2. Ver participantes por nombre")
    print("3. Ver participantes por edad")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")
    match opcion:
        case '1':
            while True:
                dorsal = input("Dorsal: ")
                nombre = input("Nombre completo: ")
                edad = input("Edad: ")
                categoria = input("Categoría (juvenil, adulto, máster): ")
                participante = {
                    'dorsal': dorsal,
                    'nombre': nombre,
                    'edad': int(edad),
                    'categoria': categoria
                }
                participantes.append(participante)
                otro = input("¿Agregar otro participante? (s/n): ")
                if otro.lower() != 's':
                    break
        case '2':
            print("\nParticipantes por nombre:")
            for p in ordenar_por_nombre(participantes):
                print(f"- {p['nombre']} (Dorsal {p['dorsal']}, Edad {p['edad']}, Categoría: {p['categoria']})")
        case '3':
            print("\nParticipantes por edad:")
            for p in ordenar_por_edad(participantes):
                print(f"- {p['nombre']} (Dorsal {p['dorsal']}, Edad {p['edad']}, Categoría: {p['categoria']})")
        case '4':
            print("Programa finalizado.")
            break
        case _:
            print("Opción no válida. Intenta otra vez.")
