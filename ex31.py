print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input(">")

if  door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream the bear."
	print "3. Give him some honey."

	bear = raw_input(">")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	if bear == "3":

		print "The bear takes the honey an runs away."
		print "The cake is in front of you. What do you do?"
		print "1. Eat it."
		print "2. Throw it against the wall."
		cake = raw_input(">")
		if cake == "1":
			print "You die of the poisonus cake"
		elif cake == "2":
			print "You go home and sleep."
		else :
			print "You did the right thing."

	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear


elif door == "2":
	print "You stare into the endless abyss at Cthulu's retina."
	print "What do you do?"
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	print "4. Take out your shotgun."

	insanity = raw_input(">")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello, Good job!"
	elif insanity == "4":
		print "You blow his retina and save the world."
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"


else:
	print "You stumble around and fall on a knife and die. Good job!"

