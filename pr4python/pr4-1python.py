import random
import multiprocessing
from multiprocessing import Process, Queue
import time

def vvod(x):
        vd:str = input('введите число и степень через пробел\n')
        x.put(vd.split())
        

def calc(x):
    while True:
        number_pow : list = x.get()
        itogpow=int(number_pow[0])**int(number_pow[1])
        itogsum=0
        for i in range(0,itogpow+1):
            itogsum+=i
        f=open(str(random.randint(0,10000))+".txt",'w')
        f.write("["+time.strftime("%d.%m.%Y %H:%M:%S") + "]  " + f"{number_pow[0]}^{number_pow[1]} = {itogpow} >> {itogsum}\n")
        f.close()
        

if __name__ == "__main__":
    x = Queue()
    potoc = Process(target=calc, args=(x,))
    potoc.start()
    try:
        while True:
            vvod(x)
    except KeyboardInterrupt:
        exit()

