#!/usr/bin/env python
# coding=utf-8
import time
import subprocess
import psutil
import socket
import os
import datetime

def kill(x):#杀死子进程
    if x.isdigit():#检测字符串是否只由数字组成
        for pid in psutil.pids():
            #print psutil.Process(int(pid)).ppid()
            #print 'xxx'
            
            try: 
                ppid=psutil.Process(int(pid)).ppid()
            except NoSushProcess:
                print 's'
                print "Error:NoSushProcess"
                return 1

            if ppid==int(x):    #ppid父进程ID
                #print 'taskkill /pid '+str(pid)+' /t /f'
                #os.system('taskkill /pid '+str(pid)+' /t /f')
                #print type(pid)
                print pid
                psutil.Process(int(pid)).terminate()
                return 1

def port():#测试端口
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ipv4,tcp
    sk.settimeout(1)
    try:
      sk.connect(('tcp.xiaomiqiu.cn',36488))
      print 'Server port 5555_36488 OK!'
      return True

    except Exception:
      #print 'Server port 5555_36488 not connect!'
      return False
    sk.close()

i=0
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print nowTime
ps = subprocess.Popen('start ngrok.exe -config=ngrok.cfg -proto=tcp 5555', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#print ps.pid
time.sleep(5)
while True:   
    i+=1
    if i%100==0:
        print 'count='+str(i)                       
    if port()==False:
        ps1 = subprocess.Popen('start ngrok.exe -config=ngrok.cfg -proto=tcp 5555', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        time.sleep(5)
        kill(str(ps.pid))
        #print ps.pid
        ps=ps1
    else:
        nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print nowTime
        break
