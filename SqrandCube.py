lst = [1,2,3,5,8,5,6,3,44,9]
print("list of integers: ")
print(lst)
print("Square every number in list: ")
square = list(map(lambda x: x ** 2, lst))
print(square)
print("Cube every number in list: ")
cube = list(map(lambda x: x ** 3, lst))
print(cube)