
import random  
from time import sleep  
from multiprocessing import Pool

urls= ["a.com", "b.com", "c.com", "d.com"]
def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3) 
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

def secuencial(url):
    output = []
    for url in urls:
        result = scrape(url)
        output.append(result)

def multiprocess(url):
    pool = Pool(processes=4) 
    data = pool.map(scrape, urls)
    pool.close() 
    print()
    for row in data: 
        print(row)


