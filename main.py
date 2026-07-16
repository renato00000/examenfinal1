import petmarket as vld
def main():
    while True:
        vld.mostrar_menu
        opcion = vld.leer_opcion()
        if opcion == "1":
            vld.validar_unidades()
        elif opcion == "2":
            vld.buscar_producto(productos)
        elif opcion == "3":
            vld.actualizar_producto(productos)
        elif opcion == "4":
            vld.agregar_pruducto(productos)
        elif opcion == "5":
            vld.eliminar_producto(productos)
        elif opcion == "6":
            vld.eliminar_producto(producto)
            print("programa finalizado")
            break
                                  

