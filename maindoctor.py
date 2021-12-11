from conexiondoctor import Hospital

base = Hospital()

seleccion = ""

while seleccion != "6":
    print("Seleccione entre las siguientes opciones:")
    print("1. Añadir un nuevo doctor")
    print("2. Modificar el salario de un doctor")
    print("3. Eliminar un doctor")
    print("4. Buscar un doctor")
    print("5. Mostrar todos los doctores")
    print("6. Salir")

    seleccion = input(">")

    if seleccion == "6":
        print("Ha salido.")
        break
    elif seleccion == "1":
        hospitales = base.mostrar_hospitales()

        for hospital in hospitales:
            print(hospital)

        codigo_hospital = input("Introduzca el código del hospital. ")
        apellido = input("Introduzca el apellido. ")
        especialidad = input("Introduzca la especialidad. ")
        salario = input("Introduzca el salario. ")

        resultado = base.nuevo_doctor(codigo_hospital, apellido, especialidad, salario)
        print(f"Ha añadido {resultado} registro(s).")
    elif seleccion == "2":
        numero = input("Introduzca el número identificador. ")
        incremento = input("Introduzca el incremento en el salario. ")

        resultado = base.modificar_salario(incremento, numero)
        print(f"Ha modificado {resultado} registro(s).")
    elif seleccion == "3":
        numero = input("Introduzca el número identificador. ")

        resultado = base.eliminar_doctor(numero)
        print(f"Ha eliminado {resultado} registro(s).")
    elif seleccion == "4":
        numero = input("Introduzca el número identificador. ")

        resultado = base.buscar_doctor(numero)

        if resultado:
            print(resultado)
        else:
            print("No se ha encontrado el identificador.")
    
    elif seleccion == "5":
        doctores = base.mostrar_doctores()

        for doctor in doctores:
            print(doctor)
    else:
        print("Selección incorrecta.")
    print()
