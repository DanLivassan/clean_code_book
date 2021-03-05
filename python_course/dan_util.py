from time import time


def performance(fn):
    def wrapper():
        t1 = time()
        result = fn()
        t2 = time()
        print(f"{t2 - t1}s elapsed")
        return result
    return wrapper
