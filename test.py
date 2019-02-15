# -*- coding: utf-8 -*-  
## __author__ = "Fidcer" ##


import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import threading
import time
import queue

from socket import *
import threading

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    setdefaulttimeout(1)
    for p in range(1,65535):
        t = threading.Thread(target=portScanner,args=('118.184.66.37',p))
        threads.append(t)
        t.start()     

    for t in threads:
        t.join()

    print('[*] The scan is complete!')
    print('[*] A total of %d open port ' % (openNum))

if __name__ == '__main__':
    main()