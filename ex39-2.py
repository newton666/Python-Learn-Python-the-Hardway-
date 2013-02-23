#Uebung
laender = { "Nordrhein-Westfalen" : "NRW", "Berlin" : "B", "Bayern" : "BY" , "Niedersachsen" : "NI" }

print laender

laender["Rheinland-Pfalz"] = "RLP"
laender["Hessen"] = "HE"

print laender

staedte = {"HH" : "Hamburg", "K" : "Koeln", "B" : "Berlin", "M" :"Muenchen"}

staedte["Ma"] = "Mainz"

print staedte

print "_"*30
print "In Nordrhein-Westfalen liegt:" , staedte["K"]
print "In Bayern liegt:" , staedte["M"]

print "_"*30
for laender, abbrev in laender.items():
	print "%s ist die Abkuerzung von %s" (laender, abbrev)