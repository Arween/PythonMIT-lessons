str_first = 'The first three items in the list are: '
str_middle = 'The items from the middle of the list: '
str_last = 'The last three items in the list are: '
list_1 = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream', 'fish', 'cake', 'apple', "orange"]


print str_first + str(list_1[:3])
print str_middle + str(list_1[3:6])
print str_last + str(list_1[6:])