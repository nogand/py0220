import threading

def counter(count,name):
  while count > 0:
    print("Cuenta para hilo %s es %d"%(name,count))
    count -= 1
  return

t1 = threading.Thread(target=counter,args=(10,"uno"))
t1.start()
t2 = threading.Thread(target=counter,args=(20,"dos"))
t2.start()
