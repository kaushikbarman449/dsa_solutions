# Sum of first N numbers parameterized method

def printSum_parameterized(N, sum):
    if N < 1:
        print(sum)
        return
    printSum_parameterized(N - 1, sum + N)


if __name__ == "__main__":
    N = int(input())
    printSum_parameterized(N, 0)
