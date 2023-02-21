<h1 align="center">Secuencial vs Paralelo</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/Tarea-en-paralelo)

***
<h2>¿De qué trata esta tarea?</h2>
En esta tarea vamos siguiendo una clase de pasos, para ir viendo la diferencia de ejecutar el código en paralelo o en secuencial.

<h2>Explicación paso a paso de código:</h2>

**Pasos:**

**1.** Creamos una lista con distintas urls:

```
urls =["a.com", "b.com", "c.com", "d.com"]
```
**2.** Importamos las librerías:

```
import random  #Importamos la librería random para generar números aleatorios
from time import sleep  #Importamos la librería sleep para esperar un tiempo determinado
```

**3.** Creamos una función que se enargará en simular el proceso de scraping de una página web. Esta simplemente imprime un mensaje y espera un tiempo alatorio entre 0 y 1:

```
def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3) 
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

```

**4.** Ahora haremos lo mismo pero de forma **secuencial**:

```
output = []
for url in urls:
    result = scrape(url)
    output.append(result)

```
En este caso, trabajamos de forma secuencial. Por lo tanto, el tiempo total de ejecución es la suma de los tiempos de ejecución de cada una de las páginas web, lo que hace que sea ineficiente.

**5.** Lo hacemos ahora con **multiprocesamiento**:

Importamos las librerias que necesitamos

```
from multiprocessing import Pool #Importamos la librería Pool para realizar el trabajo en un pool de procesos, es decir, un pool de procesos es una función que se encarga de ejecutar un conjunto de procesos en paralelo.
pool = Pool(processes=4) #Creamos un pool de 4 procesos (podemos crear tantos como queramos)

```



***
