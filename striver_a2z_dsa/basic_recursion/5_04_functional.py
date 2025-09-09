# Sum of first N numbers functional method

def printSum_functional(N):
    if N == 0:
        return 0
    return N + printSum_functional(N - 1)


if __name__ == "__main__":
    N = int(input())
    sum = printSum_functional(N)
    print(sum)
