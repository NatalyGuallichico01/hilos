#hilos
from time import sleep, perf_counter
from threading import Thread

def task(id):
    print(f"Iniciando tarea {id}\n")
    sleep(2)
    print(f"Finalizando tarea {id}\n")
    #print(id*id*id)

start_time=perf_counter()

#creacion de 10 threads
threads=[]

for n in range (1, 200):
    t=Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time=perf_counter()
print(f"Tomo {end_time- start_time:}")