qtylist = [5, 7, 3, 11, 2]
unitlist = ['bottles', 'flocks', 'loaves', 'bags', 'cups']
itemlist = ['beer', 'geese', 'bread', 'flax', 'tea']
for i in range(4):
    print "Give me %d %s of %s" % (qtylist[i], unitlist[i], itemlist[i])
