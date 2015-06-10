#def start(x):
	#print( x * "*") 

#start(13)
#start(7)
#start(17)	

#def horizontal(y):
#	print(y * "*")
#	print("*" + (y-2) * " " +"*")
#	print(y * "*")

#horizontal(10)  

def box(width, height):
	print (width * "*")
	for i in range (height - 2):
		print ("*" + (width - 2) * " " + "*")
	print (width*  "*")
	
print (13 * "*")
print  (7 * "*")
print (35 * "*")
box(10,3)
box(5,3)		   