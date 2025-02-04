# fib.py
from functools import lru_cache, wraps
import time
from typing import Callable


def timer(func: Callable):
    @wraps(func)
    def wrapper_func(n: int):
        start_time = time.time()  # Record start time
        result = func(n)
        end_time = time.time()  # Record end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Finished in {elapsed_time:.8f}s: f({n}) -> {result}")
        return result

    return wrapper_func


@lru_cache
@timer
def fib(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(100)
