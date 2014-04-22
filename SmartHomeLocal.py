
from multiprocessing import Queue, Process
from subprocess import Popen, PIPE
import shlex
from time import time, sleep
import SocketServer
import sched

w = .25
x = 2.5
myBuffer = {}
q = Queue() #Create multiprocessing.Queue
s = sched.scheduler(time, sleep)
global sysQ

def start(sysQl):
	sysQ = sysQl
	#server.serve_forever()
	HOST, PORT = "localhost", 9750
# Create the server, binding to localhost on port 9999
	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
	system = Process(target=server.serve_forever)
	system.start()
	bufferStuff(q)



def bufferStuff(q):
	while True:
		addr, data = q.get()
		if not myBuffer.get(addr, []):
			s.enter(w*x, 1, sendToSys, addr)
		myBuffer.get(addr, []).append(data)


def sendToSys(addr):
	localData = []
	while myBuffer[addr]:
		localData.append(myBuffer[addr].pop(0))
	sensors = {}
	for data in localData:
		mac, rssi = data.split()
		sensors.setdefault(mac, (0, []))
		sensors[mac][0]+=1
		sensors[mac][1].append(int(rssi))
	retval = []
	for mac in sensors:
		retval.append({'sensor#':mac, 'avRSSI':sum(sensors[mac][1])/sensors[mac][1], 'numRSSIReadings':sensors[mac][1]})
	sensors =  sorted(sensors, key=lambda y:y['avRSSI'])
	print({addr: sensors})
	sysQ.put({addr: sensors})
	
	



class MyTCPHandler(SocketServer.BaseRequestHandler):
	"""
	The RequestHandler class for our server.
	
	It is instantiated once per connection to the server, and must
	override the handle() method to implement communication to the
	client.
	"""
	def handle(self):
    # self.request is the TCP socket connected to the client
		self.data = self.request.recv(1024).strip()
		addr = "{}".format(self.client_address[0])
		data =  self.data
		#myBuffer.get(addr, []).append(data)
		q.put((addr, data))
		
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
	start(2)
