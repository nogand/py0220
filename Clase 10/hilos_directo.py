import threading

def counter(count):
  while count > 0:
    print("Count value", count)
    count -= 1
  return

t1 = threading.Thread(target=counter(10))
t1.start()
t2 = threading.Thread(target=counter,args=(20,))
t2.start()
