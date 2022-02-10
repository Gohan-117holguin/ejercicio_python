import os
import time

listaNotas = []
listaDesviacion = []
personasDicc = {}
promedio = 0

def menu ():
    while True:
        print('\nPrograma para clasificar listas de datos mediante\ndesviaciones con respecto a la media, ingrese los siguientes datos.')
        print('\n------------------------------------------------------------------------\n')
        menu = '1. Llenado de listas\n2. Salir del programa y limpiar: '

        eleccion = int(input(menu))

        if eleccion == 1:
            llenado()
            
            volver = input('Quiere continuar Si/No: ')

            if volver == 'si':
                pass
            elif volver == 'no':
                print('Gracias por utilizar nuestra aplicacion.')
                limpiar()
                break
        elif eleccion == 2:
            limpiar()

def llenado ():
    cantidadLista = int(input('\nCantidad de listas a procesar: '))
    cantidadDatos = int(input('\nCantidad de datos en la lista: '))

    # llenado de datos, empezando por la cantidad de listas
    for x in range(cantidadLista):
        nombreListas = input('\nIngrese el nombre de la lista ' + str(x + 1) + ': ')
        listaNotas = []

        # llenado de la lista de notas
        for y in range(cantidadDatos):
            notas = float(input('\nIngrese sus notas: '))
            listaNotas.append(notas)
            personasDicc[nombreListas]=listaNotas
    mostrar()
    
    return listaNotas

def mostrar ():
    print(f'\n{personasDicc}\n')

    for x, y in personasDicc.items():
        # aqui se necesita que muestre a todas las personas procesadas
        print(f'Estas son las personas procesadas: \n{x} => {y}')
    calcularPromedio()

def calcularPromedio ():
    suma = 0
    # Suma y promedio de las listas
    for x in range(len(listaNotas)):
        suma = suma + listaNotas[x]

    # Y el promedio se obtiene dividiendo la suma entre la cantidad de elementos
    cantidadNotas = len(listaNotas)
    print(cantidadNotas)
    promedio = suma / cantidadNotas
    print(f'El promedio de la suma de las notas es: {promedio}')
    listaDesviacion.append(promedio)
    comparar()

def comparar ():
    resta = 0
    # Suma y promedio de las listas
    for x in listaNotas:
        for y in listaDesviacion:
            resta = x - y

    print(f"La resta es {resta}")

    # Y el promedio se obtiene dividiendo la suma entre la cantidad de elementos
    # cantidad_elementos = len(listaNotas)
    # promedio = suma / cantidad_elementos
    # print(f"El promedio es {promedio}")
    # print('Lista Carlos presenta una media de 5 y una desviación con respecto a la media de 0 4')

def limpiar ():
    time.sleep(3)

    os.system('cls')