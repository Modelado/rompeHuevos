import random
n = random.randint(1,100 + 1)
print n
pasos =14
def rompe(numero):
	if numero >= n:
		return True
	return False

	
def rompeHuevos(p,k):
	global pasos 
	pasos -=1
	
	if rompe(k):
		while p <= k:
			if rompe(p):
				return p
				break
			p += 1
			
	else:
		return rompeHuevos(k+1,k+pasos)	

print rompeHuevos(1,14)
print pasos			

# rompeHuevos
