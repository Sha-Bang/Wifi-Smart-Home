
import socket

global sock

def start(q):
	global sock
	sock = socket.socket(socket.AF_INET, # Internet
				                     socket.SOCK_DGRAM) # UDP
	while True:
		#It will sit and wait at the following line for input
		event = q.get()
                updateLighting(event)
                

def send(MESSAGE):
	UDP_PORT = 9750
	addrs = ["192.168.43.91", "192.168.43.61", "192.168.43.102"]
	for UDP_IP in addrs:
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
       
def updateLighting(deviceInstance):
        #ser = serial.Serial('COM14', 57600)
		for mac in deviceInstance:
			for sn in deviceInstance[mac]:
				sensorNum = sn['sensor#']
				avRSSI = sn['avRSSI']
				print sensorNum, avRSSI,
			print
			onArray = [False,False,False,False]
			if deviceInstance[mac][0]['avRSSI']-deviceInstance[mac][1]['avRSSI'] <=2:
				onArray[deviceInstance[mac][0]['sensor#']] = True
				onArray[deviceInstance[mac][1]['sensor#']] = True
			else:
				onArray[deviceInstance[mac][0]['sensor#']] = True

			for sensorNum in range(1, len(onArray)):
				if onArray[sensorNum]:
					send(str(sensorNum) + '1')
					print "Turning on sensor " + str(sensorNum) + "..."                      
				else:
					send(str(sensorNum) + '0')
					print "Turning off sensor " + str(sensorNum) + "..."
		print


 		#sensorNum = deviceInstance.itervalues().next()[0]['sensor#']
        
        
  		#for sensNum in range(1,4):

		#	if sensNum == sensorNum:
		#		send(str(sensorNum) + '1')
		#		print "Turning on sensor " + str(sensorNum) + "..."                      
		#	else:
		#		send(str(sensNum) + '0')
		#		print "Turning off sensor " + str(sensNum) + "..."

