

def start(q):
	test(q)


def formatData():
	from random import randint as ri

	deviceInstance={}# MAC adress as key
	for x in range(1,4):# how many mac adresses
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
	from time import sleep
	while True:
		for k,v in formatData().items():
			#default for x in hash is hash.keys(), calling items allows me to send the whole dict
			q.put({k:v})
		sleep(5)


if __name__ == '__main__':
	print "I don't know what to do, doing the only thing I can"
	print formatData()
