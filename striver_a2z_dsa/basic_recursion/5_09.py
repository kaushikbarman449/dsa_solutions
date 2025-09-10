# Fibonacci Number

import time


def fibNumber(N):
    if N <= 1:
        return N
    return fibNumber(N-1) + fibNumber(N-2)


if __name__ == "__main__":
    start = time.time()
    result = fibNumber(40)
    end = time.time()
    print(f"fibNumber(40) = {result}, time: {end - start:.6f} sec")
