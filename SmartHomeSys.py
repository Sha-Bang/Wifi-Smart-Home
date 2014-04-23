
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
	addrs = ["192.168.43.91", "192.168.43.61"]
	for UDP_IP in addrs:
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
       
def updateLighting(deviceInstance):
        #ser = serial.Serial('COM14', 57600)
 		sensorNum = deviceInstance.itervalues().next()[0]['sensor#']
        
		print deviceInstance.itervalues().next()[0]['avRSSI'], deviceInstance.itervalues().next()[1]['avRSSI']

        
  		for sensNum in range(1,3):
			if sensNum == sensorNum:
			        #ser.write(str(sensorNum) + '1')
				send(str(sensorNum) + '1')
				print "Turning on sensor " + str(sensorNum) + "..."                      
			else:
			        #ser.write(str(sensNum) + '0')
				send(str(sensNum) + '0')
				print "Turning off sensor " + str(sensNum) + "..."

