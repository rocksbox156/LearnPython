from functools import reduce
# def double(x):
#     return x * 2
#
#
# def add(x, y):
#     return x + y
#
#
# def product(x, y, z):
#     return x * y * z


# double = lambda x: x * 2
# print(double(2))
# add = lambda x, y: x+y
# print(add(2, 3))
# product = lambda x, y, z: x*y*z
# print(product(2, 3, 4))

# filter, reduce, and map
my_list = [2, 3, 4, 5, 1, 3, 5]
my_list2 = [2, 4, 5, 5, 6, 3, 1]
a = map(lambda x: x * 2, my_list)
b = map(lambda x, y: x + y, my_list, my_list2)
for i in b:
    print(i)

c = filter(lambda x: x % 2 == 0, my_list)
print(list(c))

d = filter(lambda x: x > 5, my_list2)
print(list(d))

e = reduce(lambda x,y: x+y, my_list)
print(e)