# Reverse an array using recursion

def reverseList_using_recursion(start, listValues, end):
    if start >= end:
        return

    listValues[start], listValues[end] = listValues[end], listValues[start]
    reverseList_using_recursion(start+1, listValues, end-1)


if __name__ == "__main__":
    listValues = [1, 3, 4, 5, 2, 11, 1, 12]
    N = len(listValues) - 1
    reverseList_using_recursion(0, listValues, N)
    print(listValues)
