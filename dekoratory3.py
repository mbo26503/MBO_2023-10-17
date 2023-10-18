# pomiar czasu wykonania danej funkcji
# np. obliczanie liczby Pi metodą Monte Carlo trwało 20 sekund
# za pomocą biblioteki numpile - 1 s

import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time} sekundy")
        return result

    return wrapper

@measure_time
def my_function():
    time.sleep(2)

my_function()  # Czas wykonania funkcji my_function: 2.0017809867858887 sekundy