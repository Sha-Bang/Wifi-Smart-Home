
import SmartHomeSys
import SmartHomeLocal
#You import the file name, with the .py taken off the end
from multiprocessing import Queue, Process


def start():
	q = Queue() #Create multiprocessing.Queue

	#Prep the new Process creation
	#When you provide a method name with no () at the end it returns a pointer
	#(q,) means create a special type of array(aka tuple) with q in it
	system = Process(target=SmartHomeSys.start, args=(q,))
	local = Process(target=SmartHomeLocal.start, args=(q,))

	#Start the new Processes
	system.start()
	local.start()
	

if __name__ == '__main__':
	start()
