#Vamos a seguir paso a paso la tarea

#En primer lugar, creamos una lista:

urls =["a.com", "b.com", "c.com", "d.com"]

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

output = []
for url in urls:
    result = scrape(url)
    output.append(result)

#

