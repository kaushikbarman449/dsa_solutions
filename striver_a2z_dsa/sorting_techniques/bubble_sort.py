# bubble sort

def bubble_sort(sortList):
    for i in range(len(sortList) - 1):
        for j in range(0, len(sortList) - 1 - i):
            if sortList[j] > sortList[j + 1]:
                sortList[j], sortList[j + 1] = sortList[j + 1], sortList[j]

    return sortList


def bubbleSort(sortList):
    swapping = True
    end = len(sortList)
    while swapping:
        swapping = False
        for i in range(1, end):
            if sortList[i - 1] > sortList[i]:
                sortList[i - 1], sortList[i] = sortList[i], sortList[i - 1]
                swapping = True
            end -= 1

    return sortList


if __name__ == "__main__":
    sortList = [1, 4, 3, 11, 3, -13, 3, 0, 99]
    print("Original list", sortList)
    bubble_sort(sortList)
    print("Sorted list", sortList)
    bubbleSort(sortList)
    print("Bubble Sort", sortList)
