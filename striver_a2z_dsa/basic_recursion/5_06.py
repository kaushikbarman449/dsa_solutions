# Reverse an array using loop

def reverseList_using_loop(listValues):
    start = 0
    end = len(listValues) - 1
    while start < end:
        listValues[start], listValues[end] = listValues[end], listValues[start]
        start += 1
        end -= 1

    return listValues


if __name__ == "__main__":
    listValues = [1, 3, 4, 5, 2, 11, 1, 12]
    reversed_List = reverseList_using_loop(listValues)
    print(reversed_List)
