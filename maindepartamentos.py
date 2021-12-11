from conexiondepartamentos import Hospital

base = Hospital()

eleccion = ""

while eleccion != "0":
    print("Seleccione entre las siguientes opciones:")
    print("1. Ver todos los departamentos")
    print("2. Buscar un departamento")
    print("3. Crear un nuevo departamento")
    print("4. Modificar un departamento existente")
    print("5. Eliminar un departamento existente")
    print("0. Salir")

    eleccion = input("> ")

    if eleccion == "0":
        print("Ha salido.")
    elif eleccion == "1":
        departamentos = base.ver_departamentos()

        for departamento in departamentos:
            print(departamento)
    elif eleccion == "2":
        numero = input("Introduzca el número del departamento. ")

        departamento = base.buscar_departamento(numero)

        if not departamento:
            print("No existe el departamento.")
        else:
            print(departamento)
    elif eleccion == "3":
        numero = input("Introduzca el número del departamento. ")
        nombre = input("Introduzca el nombre del departamento. ")
        localidad = input("Introduzca la localidad del departamento. ")

        registros = base.nuevo_departamento(numero, nombre, localidad)
        print(f"Ha añadido {registros} registro(s).")
    elif eleccion == "4":
        numero = input("Introduzca el número del departamento. ")
        nombre = input("Introduzca el nuevo nombre del departamento. ")
        localidad = input("Introduzca la nueva localidad del departamento. ")

        registros = base.modificar_departamento(numero, nombre, localidad)
        print(f"Ha modificado {registros} registro(s).")
    elif eleccion == "5":
        numero = input("Introduzca el número del departamento. ")

        registros = base.eliminar_departamento(numero)
        print(f"Ha eliminado {registros} registro(s).")
    else:
        print("Selección no válida.")
    print()
