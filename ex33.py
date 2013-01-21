

def loop(b):
		i = 0
		numbers = []
		
		while  i < b:
			print "At the top i is %d" % i
			numbers.append(i)

			i += 1
			print "Numbers now ", numbers
			print "At the bottom i is %d" % i


			print "The numbers: "

			for num in numbers:
				print num

a = float(raw_input(">"))
# Eine Funktion wir immer mit einer variblen aufgerufen
loop(a)
