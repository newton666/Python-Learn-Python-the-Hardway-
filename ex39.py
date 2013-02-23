things = ['a', 'b', 'c', 'd']

things [1] = 'z'
print things [1]
print things


stuff = {'name' : 'Zed', 'age' : 36, 'height' : 6*12+2}
print stuff['name']

stuff["city"] = "San Francisco"

print stuff['city']

stuff[1] = "TryIt"
stuff[12] = "HaveIt"

print stuff[12]
print stuff[1]
print stuff

del stuff['city']
del stuff[12]
del stuff[1]
print stuff

#exercise

states = {
	"Oregon" : "OR","Florida" : 'CA', "New York" : "NY", "Michigan" : "MI"
}

print states
# create a basic set of states and some cities in them
cities = { "CA" : "San Francisco", "MI" : "Detroit", "FL" : "Jacksonville"}

# add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
print "_" * 30
print "NY State has:" , cities["NY"]
print "OR State has:" , cities["OR"]

# print some states
print "_" * 30
print "Michigan's abreviation is : " , states['Michigan']
print "Florida's abreviation is : " , states['Florida']
 
# do it by using the state then cities dict
print "_" * 30
print "Michigan has: " , cities[states["Michigan"]]
print "Florida has: " , cities[states["Florida"]]

# print every state abbreviation
print "_" * 30
for state, abbrev in states.items():
	 print "%s is abbreviated %s" % (state, abbrev)

#print every city in state
print "_" * 30
for abbrev, city in cities.items():
	print "%s has the city %s"  % (abbrev, city)

# now do both at the same time
print "_" * 30
for state, abbrev in states.items():
	print "%s state is abbreviated %s and hast city %s" % (state, abbrev, cities[abbrev]) 
print "_" * 30
# safely get a abreviation by state that might not be there
state = states.get("Texas", None)

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist') #get nachschlagen
print "The city for the state 'TX' is: %s" % city



