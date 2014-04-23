
from multiprocessing import Queue, Process
from subprocess import Popen, PIPE
from threading import Timer
import shlex
from time import time, sleep
import SocketServer
import sched
import socket

w = .25
x = 4.5 #2.5
myBuffer = {"test":"worked"}
q = Queue() #Create multiprocessing.Queue
sch = sched.scheduler(time, sleep)
global sysQ
UDP_IP = "127.0.0.1" #Mike switch order of these two
UDP_IP = "192.168.43.31"
UDP_PORT = 9750

def start(sysQl):
	global sysQ
	sysQ = sysQl

	sock = socket.socket(socket.AF_INET, # Internet
				                     socket.SOCK_DGRAM) # UDP
	sock.bind((UDP_IP, UDP_PORT))
	system = Process(target=startServer, args=(sock,))
	system.start()
	bufferStuff(q)


def startServer(sock): #UDP Server start
	while True:
		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

		#TODO
		addr = "12:3:23:32:ab"
		if data[0]!='#':
			q.put((addr, data))
		#print "sServer", addr, data


def bufferStuff(q):
	while True:
		addr, data = q.get()
		#print "BuffStuff", addr, data
		if not myBuffer.get(addr, []):
			#print "adding", addr
			sch.enter(w*x, 1, sendToSys, addr)
			Timer(w*x, sendToSys, (addr,)).start()

			system = Process(target=sch.run)
		myBuffer.setdefault(addr, [])
		myBuffer[addr].append(data)
		#print "BuffStuff-dict", myBuffer


def sendToSys(addr):
	global sysQ
	#print "s2s", addr
	localData = []
	while myBuffer[addr]:
		localData.append(myBuffer[addr].pop(0))
	sensors = {}
	for data in localData:
		rssi, devN = data.split() 
		rssi = int(rssi)
		if rssi == 0:
			print "#0", devN
			rssi = 100000
		sensors.setdefault(devN, [0, []])
		#print sensors[devN], sensors[devN][0]
		sensors[devN][0] = sensors[devN][0] + 1
		sensors[devN][1].append(rssi)
	retval = []
	for mac in sensors:
		retval.append({'sensor#':int(mac), 'avRSSI':sum(sensors[mac][1])/sensors[mac][0], 'numRSSIReadings':sensors[mac][1]})
	retval =  sorted(retval, key=lambda y:y['avRSSI'], reverse=True)
	

	#print({addr: retval})
	sysQ.put({addr: retval})

		#self.request.sendall(self.data.upper())

def getRSSI():
	x = shlex.split("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I")
	y = Popen(x, stdout=PIPE).stdout.read().split("\n")
	rssi = y[0].split(": ")[1]
	mac = y[11].split(": ")[1]
	me = 1
	return (mac, rssi)


def formatData():
	from random import randint as ri

	deviceInstance={}# MAC adress as key
	for x in range(1,2):# how many mac adresses
		sensors=[]
		for i in range(1,4):
			sensors.append({'sensor#':ri(0,12), 'avRSSI':ri(-90,-10), 'numRSSIReadings':ri(2,14)})
			#append the fake data into a list
		deviceInstance["3c:2d:4g:3%d"%ri(0,9)] = sorted(sensors, key=lambda y:y['avRSSI'])
			#Sort the fake data using the lambda function that used the key 'avRSSI'
			# then assign the fake data to a mac address
	return deviceInstance


def test(q):
	"""
		Every 5 secs create a new set of input
	"""
	while True:
		for k,v in formatData().items():
			#default for x in hash is hash.keys(), calling items allows me to send the whole dict
			q.put({k:v})
		sleep(5)


if __name__ == '__main__':
	print "I don't know what to do, doing the only thing I can"
