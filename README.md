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

***
