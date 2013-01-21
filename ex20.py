from sys import argv

script, input_file = argv #die zulesende Datei input_file

def print_all(g):	#definition der funktion mit der variablen g
	print g.read()

def rewind(g): #definiton der funktion suche => zuruecksetzen der datei zu beginn
	g.seek(0)

def print_a_line(line_count, g): #denfinition der funktion print_a_line =>Ausgabe von Zeilennummer und Linie
	print line_count, g.readline() #line_count = current_line

current_file = open(input_file) # oeffnet die aktuelle datei argv

print "First let's print the whole file:\n"

print_all(current_file) # druckt alles aus der aktuellen datei aus.

print "Now let's rewind, kind of like a tape."

rewind(current_file) # zuruecksetzen der aktuellen datei durch die funktion rewind

print "Let's print three lines:"


current_line = 1 
print_a_line(current_line, current_file)
# Zuweisung von 1 zu current_line und die Funktion von print_a_line hat 2 variablen

current_line += 1
print_a_line(current_line, current_file)
#+= fuegt der variablen eine Zahl hinzu und aedert sie

current_line += 1
print_a_line(current_line, current_file)


