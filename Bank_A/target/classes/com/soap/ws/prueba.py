import multiprocessing
import time
def Child_process():
   print ('Starting function')
   time.sleep(5)
   print ('Finished function')
P = multiprocessing.Process(target = Child_process)
P.start()

print("My Process has terminated, terminating main thread")

print("Terminating Child Process"  + str(P.pid))
P.terminate()
P.join()
P.close()
print("Child Process successfully terminated")
P = multiprocessing.Process(target = Child_process)
P.start()

print("Terminating Child Process"  + str(P.pid))
P.terminate()

print("Child Process successfully terminated")