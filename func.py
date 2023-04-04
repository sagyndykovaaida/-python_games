def compose_functions(f, g):
    def h(x):
        return f(g(x))
    return h


# print(h(5))  