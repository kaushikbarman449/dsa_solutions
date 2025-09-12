# selection sort

def selection_sort(sortList):
    for j in range(len(sortList)):
        smallestElement = j
        for i in range(j+1, len(sortList)):
            if sortList[i] < sortList[smallestElement]:
                smallestElement = i

        if smallestElement != j:
            sortList[j], sortList[smallestElement] = sortList[smallestElement], sortList[j]

    return sortList


if __name__ == "__main__":
    sortList = [1, 4, 3, 11, 3, -13, 3, 0, 99]
    print("Original list", sortList)
    selection_sort(sortList)
    print("Sorted list", sortList)
