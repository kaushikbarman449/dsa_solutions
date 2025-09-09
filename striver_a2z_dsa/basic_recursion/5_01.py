# Understand recursion by print something N times


def printName(i, N):
    if i > N:
        return
    print(f"Kaushik {i}")
    printName(i + 1, N)


if __name__ == "__main__":
    countTimes = int(input("Enter how many times you want to print name: "))
    printName(1, countTimes)
