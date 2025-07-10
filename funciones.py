from os import system
productos = {"8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
             "2175HD": ["lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
             "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
            "fgdxFHD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i3", "integrada"],
             "GF75HD": ["Asus", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
             "123FHD": ["lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
             "342FHD": ["lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
           "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"]
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1]}

def limpiar_pantalla():
    input("Presione una tecla para continuar")
    ("cls")

   

def stock_marca(marca):
    contador = 0
    for x in stock:
        if marca.upper() == productos[x][0].upper(): 
            contador += 1
            print(f"El stock es {contador}")
        else:
          print(f"El stock es {contador}")

def busqueda_precio(p_min, p_max):
    acum=0
    for x in stock:
            if p_min >= 290890 and p_max <=749990:
                acum+=1
                print(f"Los notebooks entre los precios consultas son: {stock[x][0]}")
            else:
                print("No hay notebooks dentro del rango de precios.")



def actualizar_precio(modelo, p):
    lista = []
    for x in stock:
        modelo = input("Modelo a actualizar: ")
        p = int(input("Ingrese precio nuevo: "))
        if modelo.upper() == productos[x][0].upper():
            if p not in {stock[x][0]}:
                p = {"modelo": modelo, "precioNuevo": p}
                print("Precio actualizado.")
                return True
            else:
                print("Precio existente")
                return False
        else:
            print("Modelo no se encuentra registrado")
