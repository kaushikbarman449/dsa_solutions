# Print N to 1 using backtracking

def printLinearlyBacktracking(curr, stop):
    if curr < stop:
        return
    printLinearlyBacktracking(curr-1, stop)
    print(curr)


if __name__ == "__main__":
    N = int(input())
    printLinearlyBacktracking(N, -3)
