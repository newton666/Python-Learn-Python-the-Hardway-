#from decimal import Decimal
#getcontext().prec = 4

def sticks(a, b):
	return a / b

#raw_input("Fuer wie viele Streichhoelzer soll die Packung ausgelegt sein?"), raw_input("Wie viele Streichhoelzer hast du?"))

ergebnis = sticks(150.0, 35.0)

print "Du brauchst so viele Packungen: %f" % ergebnis