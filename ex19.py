def cheese_and_crackers(cheese_count, boxes_of_crackers): #definiton der Funktion/Scripts mit den Variablen cheese_count und boxes_of_crackers 
    print "You have %r cheeses!" % cheese_count # %d als place holder
    print "You have %r boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:" #Eingabe der Zahlen in die Funktion f(x, x)
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"  #Zuweisung von unterschiedlichen Werten zu den Variablen aus dem Script
amount_of_cheese = int(raw_input('Enter cheese: '))
amount_of_crackers = int(raw_input('Enter crackers: '))
#amount_of_cheese = 12
#amount_of_crackers = 43

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # Ausfuehrung des Scripts


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) #Mathematische Operationen


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #Addition der Variablen mit den Zahlen
