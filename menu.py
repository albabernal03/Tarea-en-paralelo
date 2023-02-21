from url import *
urls=["a.com", "b.com", "c.com", "d.com"]
urls2=["a.com", "b.com", "c.com", "d.com", "e.com"]

def inicio():
    print("Iniciando...")
    print('¿Qué quieres hacer?')
    print('1. Ejecutar el programa de forma secuencial las 4 urls')
    print('2. Ejecutar el programa con multiprocesamiento y 4 procesos las 4 urls')
    print('3. Ejecutar el programa con multiprocesamiento y 4 procesos las 5 urls')

    opcion = int(input('Opcion: '))
    if opcion == 1:
        secuencial(urls)
    elif opcion == 2:
        multiprocess(urls)
    elif opcion == 3:
        multiprocess(urls2)

