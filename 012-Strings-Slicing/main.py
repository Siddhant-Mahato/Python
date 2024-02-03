fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5])
# print(fruit[0:-3])
# print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

# Quick Quiz:
# nm = "Harry"
# print(nm[-4:-2])
# @codewithharry


# nm="Harry"
# print(nm[-4:-2])
# *The length of the string is 5, and the order of characters starts from zero, so H(0), a(1), r(2), r(3), y(4). 
# Back to the code;
# (len(nm)-4-->5-4=1
# (len(nm)-4-->5-2=3
# *Hypothetically new statement is print(nm[1:3])
# we know starting point is 1, but to access charater's order we use n-1 principal.
#  So, order of character=n-1
# OC=3-1=2
# Take order of character from 1 to 2 from the actual string; hence, out put is (ar).