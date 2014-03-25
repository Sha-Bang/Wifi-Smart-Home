
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

x = formatData()


for mac in x:
	print mac
	print "heighest:", x[mac][0]

	for sensorReading in x[mac]:
		print sensorReading
