def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")

def leer_opcion():
    try:
        opcion = int(input("ingrese una opcion: "))
        return opcion
    except ValueError:
        return -1
    
    
def validar_codigo(codigo):
    return 
def validar_nombre(nombre):
    return len(nombre.strip()) > 0
def validar_categoria(categoria):
    return len(categoria.strip()) > 0
def validar_marca(marca):
    return len(marca.strip()) > 0
def validar_peso(peso):
    try:
        valor = float(peso)
        return valor < 0.0
    except ValueError:
        return False
def validar_importado(importado):
    
def validar_cachorro(cachorro):

def validar_precio(precio):
    try:
        valor = int(precio)
    except ValueError:
        return False
def validar_unidades(unidades):

    
def buscar_producto(productos):
    while True:
        buscar=input("ingrese que desea buscar: ")
        if len(buscar) == "0":
            print("el nombre no puede estar vacio")
        elif not buscar.isalpha():
            print("dato incorrecto")
    
def agregar_pruducto(productos):
    print("---agregar producto----")
    codigo=input("ingresar codigo del producto: ")
    nombre=input("ingresar nombre del producto: ")
    categoria=input("ingresar categoria del producto: ")
    marca=input("ingrese marca del producto: ")
    peso=input("ingrese peso del producto: ")
    importado=input("es importado? (si/no): ")
    cachorro=input("ingrese si es para cachorro (si/no): ")
    precio=int(input("ingrese el precio :"))
    unidades=input("ingrese las unidades: ")
    if not validar_codigo(codigo):
        print("el codigo no puede estar vacio")
        return
    if not validar_nombre(nombre):
        print("el nombre no puede estar vacio")
        return
    if not validar_categoria(categoria):
        print("la categoria no puede estar vacia")
        return
    if not validar_marca(marca):
        print("la marca no puede estar vacia")
        return
    if not validar_peso(peso):
        print("el peso no puede estar vacio")
        return
    if not validar_importado(importado):
        print("importado no puede estar vacio")
        return
    if not validar_cachorro(cachorro):
        print("cachorro no puede estar vacio")
        return
    if not validar_precio(precio):
        print("el precio no puede estar vacio")
        return
    if not validar_unidades(unidades):
        print("las unidades no pueden estar vacias")
        return
    nuevo_producto ={
        "codigo":codigo.strip(),
        "nombre":nombre.strip(),
        "categoria":categoria.strip(),
        "marca":marca.strip(),
        "peso":float(peso),
        "importado":importado if True == "s" or "S" else False == "n" or "N",
        "cachorro":cachorro if True == "s" or "S" else False == "n" or "N",
        "precio": int(precio),
        "unidades":int(unidades)
    }
    lista_de_productos
    producto = [codigo,nombre,categoria,marca,peso,importado,cachorro,precio,unidades]


def eliminar_producto(productos):
    while True:
        eliminar = input("ingrese que producto desea eliminar:")
        if len(eliminar) == 0:
            print("el nombre no puede estar vacio")
        elif not eliminar.isalpha():
            print("dato incorrecto")
        else:
           eliminado = False
           for producto in productos:
               if producto[0] == eliminar:
                   productos.remove(producto)
                   print("producto eliminado")
                   eliminado = True
                   break
               if eliminado == False:
                    print("no existe")

def mostrar_producto(lista_de_productos):
    for producto in lista_de_productos:
        if producto ["producto"]:
            producto["precio"] = True

        else:
            producto["precio"] = False


    
    






