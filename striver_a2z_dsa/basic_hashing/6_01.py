# Hashing Theory

if __name__ == "__main__":
    sizeOfList = int(input("Enter size of list: "))
    originalList = [int(input()) for _ in range(sizeOfList)]
    print(f"Original list: {originalList}")

    hashList = [0] * 12
    for num in originalList:
        hashList[num] += 1

    query = int(input("Enter your query: "))
    while query > 0:
        num = int(input("Enter number: "))
        print(hashList[num])
        query -= 1
