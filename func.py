def compose_functions(f, g):
    def h(x):
        return f(g(x))
    return h

def add_one(x):
    return x + 1

def multiply(x):
    return 2 * x

f = input("first function (e.g., add_one): ")
g = input("second function (e.g., multiply): ")

f = globals()[f]
g = globals()[g]

h = compose_functions(f, g)
print(h(5))  