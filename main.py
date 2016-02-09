import consoler
import threading
import time

if __name__ == '__main__':
    con = consoler.Consoler()
    e = threading.Event()
    t = threading.Thread(target=con.console, args=list([e]))
    try:

        t.start()
        while t.is_alive:
            time.sleep(1)

    except KeyboardInterrupt:
        e.set()
        print "except"
    print 'finish'
