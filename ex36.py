from sys import exit

def dead(why):
	print why, "continue?"

	exit(0)
def start():
	print "You are in the middle of the jungle. \n There are two pathways: \n"
	print "The leftone is dark and gloomy, while the right one follows to an ancient maya temple"
	print "Which path you want to go?"
 
	branch = raw_input(">")

	if branch == "left":
		forest()
	elif branch == "right":
		temple()
	else:
			dead("A panther jumps out of the dark and eats you.")


def inside_temple():
		print "Inside the temple you find big pile of gold."
		print "A leprachun is sitting on top of it."
		print "How much gold do you seek?"

		gold = raw_input("")

		if gold <= 500:
			print "The leprachun curses you. You greedy bastard.\n You die slowly."
			dead("You die slowly and horrible.")
		elif gold >= 500:
			print "You take the gold with you"
			
		else:
			print "The bottom under you disappears and fall into dark hole."
			dead("Try again.")
			
def temple():
	print "You arrive at the ancient maya temple."
	print "Two panthers guarding the entrance to the temple. You've got torch and a lighter\, two rotten pieces of meat\, a small bag of gold."
	print "What do you do?"

	jaguar = raw_input(">")

	if jaguar == "light torch":
		print ("The panthers are afraid of your fire and let you inside of the temple")
		inside_temple()
	elif jaguar == "give meat":
		print "As you serve the piece of meat both cats jump at the bait."
		print "You try to get inside the temple, but the panthers catch you up."
		dead("They attack you and chew on your bones.")
	#elif jaguar == "throw bag of gold"
	#	print "You provoke the panthers and they attack you instantly."
	#	dead("You end up dead.")
	else:
		print "You hesitate and end up dead"
		dead("Happy playing.")
			
def forest():
	print "You find a group of cannibals."

	cannibals = raw_input(">")

	if cannibals == "run":
		print "You escape the fangs of the brutal cannibals"
		temple()
	elif cannibals == "fight":
		print "You are stabbed by their spears and bleed out."
		dead ("Rot in hell")
		
	else:
		print "They tear you apart"
		dead("Try again")
		
start()