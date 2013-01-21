def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d - %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d - %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(30, 2)
iq = divide(70, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

a = divide(iq, 2)
b = multiply(weight, a)
c = subtract(height, b)
what = add(age, c)


print "That becomes: ", what, "Can you do it by hand?"
print "Yes, I can."

calc = add(4, add(4, multiply(3, 3)))

print "Ergebnis %d" % (calc)