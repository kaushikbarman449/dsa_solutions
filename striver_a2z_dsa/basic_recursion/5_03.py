# Print N to 1 using recursion

def printLinearlyDesc(N, i):
    if N < i:
        return
    print(N)
    printLinearlyDesc(N-1, i)


if __name__ == "__main__":
    N = int(input())
    printLinearlyDesc(N, -10)
