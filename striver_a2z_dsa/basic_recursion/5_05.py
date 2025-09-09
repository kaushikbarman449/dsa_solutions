# Factorial of N numbers

def print_Factorial(N):
    if not isinstance(N, int):
        raise TypeError("Input must be integer")

    if N < 0:
        raise ValueError("Can't be negative number")

    if N == 0 or N == 1:
        return 1
    return N * print_Factorial(N - 1)


if __name__ == "__main__":
    result = print_Factorial(7)
    print(result)
