
import random  
from time import sleep  
from multiprocessing import Pool

def scrape(url):
    print("starting", url)
    duration = round(random.random(0,1), 3)  
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

def secuencial(urls):
    output = []
    for url in urls:
        result = scrape(url)
        output.append(result)

def multiprocess(urls):
    pool = Pool(processes=4) 
    data = pool.map(scrape, urls)
    pool.close() 
    print()
    for row in data: 
        print(row)


