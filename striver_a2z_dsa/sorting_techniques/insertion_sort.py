#  insertion sort

def insertion_sort(sortList):
    n = len(sortList)
    for i in range(1, n - 1):
        pointer = i
        while pointer > 0 and sortList[pointer - 1] > sortList[pointer]:
            sortList[pointer - 1], sortList[pointer] = sortList[pointer], sortList[pointer - 1]
            pointer -= 1
    return sortList


if __name__ == "__main__":
    sortList = [1, 4, 3, 11, 3, -13, 3, 0, 99]
    print("Original list", sortList)
    insertion_sort(sortList)
    print("Sorted list", sortList)
