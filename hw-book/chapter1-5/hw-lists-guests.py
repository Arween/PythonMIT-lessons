guests = ['Harry', 'Ron', 'Hermione']

for guest in guests:
    print ('Welcome, ' + guest + ' 14.01.2017')

cannot = 'Ron'
print cannot + ' can not come.'
guests.remove(cannot)
print 'Remaining guest list: ' + str(guests)

guests.append('Ginny')

for guest in guests:
    print ('Welcome, ' + guest + ' 14.01.2017')

guests.insert(0, 'Percy')
guests.insert(2, 'Luna')

print 'Number of guests: ' + str(guests.__len__()) + '\n' + str(guests)

number = guests.__len__()

for guest in guests[2:]:
    guests.pop()
    print guest + ", I'm sorry"

print str(guests)

for guest in guests:
    print guest + ", all ok!"

del guests[:]

print str(guests) + 'list'