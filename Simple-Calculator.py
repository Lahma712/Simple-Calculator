def funcAdd():
	num2 = float(input("")) #every float input after the first one
	global result
	result = result + num2
	return
 
def funcSub():
	num2 = float(input(""))
	global result
	result = result - num2
	return

def funcMult():
	num2 = float(input(""))
	global result
	result = result * num2
	return

def funcDiv():
	num2 = float(input(""))
	assert(num2 !=0), "You can not divide by 0!"
	global result
	result = result / num2
	return
 
while True:
	result = float(input("")) #first float input
	while True:
		op = input("")
		if op == "+":
			funcAdd()
		elif op == "-":
			funcSub()
		elif op == "*":
			funcMult()
		elif op == "/":
			funcDiv()
		elif op == "=":
			print(str(result))
			print("")
			break
    
    
		
    
			
    



