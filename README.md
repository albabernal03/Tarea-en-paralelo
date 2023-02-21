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

Importamos las libreria que necesitamos

```
from multiprocessing import Pool #Importamos la librería Pool para realizar el trabajo en un pool de procesos, es decir, un pool de procesos es una función que se encarga de ejecutar un conjunto de procesos en paralelo.

```

**6.** Creamos un pool de 4 procesos (podemos crear tantos como queramos) y Ejecutamos la función scrape en paralelo para cada una de las páginas web de la lista urls. El .map es la función que se encarga de ejecutar cada una de las páginas web en paralelo:

```
pool = Pool(processes=4)
data=pool.map(scrape, urls)

```

**7.** A continuación, cerramos el pool e imprimimos data:

```

pool.close() #Cerramos el pool de procesos
print()
for row in data: #Imprimimos los resultados
    print(row)

```

Al trabajar en paralelo, el tiempo total de ejecución es el tiempo de ejecución de la página web más lenta, lo que hace que sea mucho más eficiente.


**8.** Ahora veamos que sucede si aumentamos el número de URls:

```
urls2= ["a.com", "b.com", "c.com", "d.com", "e.com"]
pool = Pool(processes=4) 
data=pool.map(scrape, urls2) 
pool.close() 
print()
for row in data:
    print(row)

```
Como hay 5 urls y solo 4 procesos, el proceso 4 se queda esperando a que se libere un proceso para poder ejecutar la url e.com







***
