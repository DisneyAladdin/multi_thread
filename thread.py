#coding:utf-8
'''
１から１００までカウント．qが入力されたら強制終了．
'''

import threading
import sys
from time import sleep

class Config:
    fg = False

def thread1():
    while True:    
        c = sys.stdin.read(1)
        if c == 'q':
            Config.fg = True

if __name__ == '__main__':
    th = threading.Thread(target=thread1,name="th",args=())
    th.setDaemon(True)
    th.start()

    for i in range(1,101):
        if Config.fg:
            sys.exit()
        print(i)
        sleep(1)
