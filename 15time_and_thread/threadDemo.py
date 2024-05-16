import threading, time
print('program started')

def take_a_nap():
    time.sleep(5)
    print('wake up!')
    
thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()

print('program end')