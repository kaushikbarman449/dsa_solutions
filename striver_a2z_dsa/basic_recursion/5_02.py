# Print linearly from 1 to N

def printLinearly(i, N):
    if i > N:
        return
    print(i)
    printLinearly(i+1, N)


if __name__ == "__main__":
    N = int(input())
    printLinearly(1, N)
