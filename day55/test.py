
def decorator_func(function):
    def wrapper(*args):
        result = function(*args)
        print(f"You called {a_function.__name__}({', '.join(map(str, args))})")
        print(f"It returned: {result}")
    return wrapper


@decorator_func
def a_function(a, b, c):
    return a * b * c


inputs = eval(input())
a_function(inputs[0], inputs[1], inputs[2])
