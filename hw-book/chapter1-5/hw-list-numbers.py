# for i in range(1,1000000):
#     print i

list_numbers = list(range(1, 1000001))
print min(list_numbers)
print max(list_numbers)
print sum(list_numbers)

# list_odd = list(range(1, 1000001, 2))
# for i in list_odd:
#     print i


# for i in range(3,30,3):
#     print i


# for i in range(1,10):
#     print i**3

list_3 = [value**3 for value in range(1,11)]
print list_3
