from funciones import menu

menu()

'''
while True:
    print('\nPrograma para clasificar listas de datos mediante\ndesviaciones con respecto a la media, ingrese los siguientes datos.')
    print('\n------------------------------------------------------------------------\n')

    menu = '1. llenado de listas\n2. salir del programa y limpiar: '

    eleccion = int(input(menu))

    if eleccion == 1:
        cantidadLista = int(input('Cantidad de listas a procesar: '))
        cantidadDatos = int(input('\nCantidad de datos en la lista: '))

        # llenado de datos, empezando por la cantidad de listas
        for x in range(cantidadLista):
            nombreListas = input('\nIngrese el nombre de la lista ' + str(x + 1) + ': ')
            
            listaNotas = []

            # llenado de la lista de notas
            for y in range(cantidadDatos):
                notas = float(input('\nIngrese sus notas: '))
                listaNotas.append(notas)

                # Impresion del diccionario con las personas y notas
                personasDicc = {nombreListas: listaNotas}

            print(f'\n{personasDicc}\n')

            for x, y in personasDicc.items():
                # aqui se necesita que muestre a todas las personas procesadas
                print(f'Estas son las personas procesadas: \n{x} => {y}')

            suma = 0
            # Suma y promedio de las listas
            for x in listaNotas:
                suma = suma + x

            print(f"La suma es {suma}")

            # Y el promedio se obtiene dividiendo la suma entre la cantidad de elementos
            cantidadNotas = len(listaNotas)
            promedio = suma / cantidadNotas
            print(f"El promedio es {promedio}")

        volver = input('Quiere continuar Si/No: ')

        if volver == 'si':
            pass
        elif volver == 'no':
            print('Gracias por utilizar nuestra aplicacion.')
            limpiar()
            break

    elif eleccion == 2:
        limpiar()
        break
'''