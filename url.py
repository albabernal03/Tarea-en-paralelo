#Vamos a seguir paso a paso la tarea

import random  #Importamos la librería random para generar números aleatorios
from time import sleep  #Importamos la librería sleep para esperar un tiempo determinado

#Esta función se encarga de simular el proceso de scraping de una página web. Simplemente imprime un mensaje y espera un tiempo aleatorio entre 0 y 1 segundos.
def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3) 
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration


#AHORA VAMOS A VERLO DE FORMA SECUENCIAL
def secuencial(urls):
    output = []
    for url in urls:
        result = scrape(url)
        output.append(result)

#En este caso, trabajamos de forma secuencial. Por lo tanto, el tiempo total de ejecución es la suma de los tiempos de ejecución de cada una de las páginas web, lo que hace que sea ineficiente.


#AHORA HACEMOS EL TRABAJO EN MULTIPROCESAMIENTO

#En primer lugar debemos importar la librería multiprocessing

from multiprocessing import Pool #Importamos la librería Pool para realizar el trabajo en un pool de procesos, es decir, un pool de procesos es una función que se encarga de ejecutar un conjunto de procesos en paralelo.


def multiprocess(urls):
    pool = Pool(processes=4) #Creamos un pool de 4 procesos (podemos crear tantos como queramos)
    data=pool.map(scrape, urls) #Ejecutamos la función scrape en paralelo para cada una de las páginas web de la lista urls. El .map es la función que se encarga de ejecutar cada una de las páginas web en paralelo.
    pool.close() #Cerramos el pool de procesos
    print()
    for row in data: #Imprimimos los resultados
        print(row)


