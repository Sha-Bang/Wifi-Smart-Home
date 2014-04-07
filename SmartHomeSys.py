

def start(q):
	while True:
		#It will sit and wait at the following line for input
		event = q.get()
		processInput(event)

def processInput(input): 
	"""
		Example method to show proof of concept
	"""
	print input
			
