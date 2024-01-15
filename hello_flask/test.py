import time

current_time = time.time()
print(current_time)  


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        stop_time = time.time()
        run_time = stop_time - start_time
        print(f"{function.__name__} run speed: {run_time}")

    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()