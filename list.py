def get_list(n):
    squares = []
    for i in range(1, n+1):
        squares.append(i**2)
    return squares

def get_tuple(a, b, c):
    return (a, b, c)

def get_dict():
    fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}
    return fruits

squares = get_list(5)
print(squares)  

my_tuple = get_tuple(1, 2, 3)
print(my_tuple) 

fruit_dict = get_dict()
print(fruit_dict)  


