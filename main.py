from funciones import *
limpiar_pantalla()
while True:
    print("""

*** MENU PRINCIPAL ***
1. Stock marca.
2. Búsqueda por precio.
3. Actualizar precio.
4. Salir.""")
    opcion = int(input("Seleccione: "))
    match opcion:
            case 1:
              marca = input("ingrese marca: ").upper()
              stock_marca(marca)
            case 2:
                  p_min = int(input("Ingrese precio mínimo: "))
                  p_max = int(input("Ingrese precio máximo: "))
                  busqueda_precio(p_min, p_max)

            case 3:
              modelo = input("Modelo a actualizar: ")
              p = int(input("Ingrese precio nuevo: "))
              actualizar_precio(modelo, p)
            case 4:
              print("Programa finalizado")
              break

