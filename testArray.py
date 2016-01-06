mList = [((5, 5), 'start', 0), ((5, 4), 'South', 1), ((5, 5), 'North', 1), ((5, 4), 'South', 1), ((5, 5), 'North', 1), ((5, 4), 'South', 1), ((5, 5), 'North', 1)]

a = ((5, 5), 'North', 1)

b = ((5, 3), 'start', 0)


if a in mList:
    print 'yes a'
else:
    print 'no a'
    
if b in mList:
    print 'yes b'
else:
    print 'no b'
    
i = 0    
while (i<5):    
    if i==3:
        i=i+1
        continue
    for letter in 'Python': 
        if letter == 'h':
            continue
        print 'Current Letter :', letter
    print 'while loop ',i
    i = i +1