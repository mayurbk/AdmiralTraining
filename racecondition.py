import threading

x = 0

def incr():
        global x
        x+=1


def t_func():
    for y in range(100000):
        incr()


def main_task():
    global x
    x = 0

    t1 = threading.Thread(target=t_func)

    t2 = threading.Thread(target=t_func)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=='__main__':
    for i in range(16):
        main_task()
        print("iteration {0}: x = {1}".format(i,x))