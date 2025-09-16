# merge sort implementation in Python

def merge_sort(nums):
    # base case: if the list has 0 or 1 element, it's already sorted
    if len(nums) < 2:
        return nums

    # divide: split the list into two halves
    # recursively sort left half
    first = merge_sort(nums[: len(nums) // 2])
    # recursively sort right half
    second = merge_sort(nums[len(nums) // 2:])

    # conquer: merge the two sorted halves
    return merge(first, second)


def merge(first, second):
    final = []
    i = 0  # pointer for first list
    j = 0  # pointer for second list

    # step through both lists until one runs out
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])   # pick smaller element from first
            i += 1
        else:
            final.append(second[j])  # pick smaller element from second
            j += 1

    # if elements remain in first, add them
    while i < len(first):
        final.append(first[i])
        i += 1

    # if elements remain in second, add them
    while j < len(second):
        final.append(second[j])
        j += 1

    return final


if __name__ == "__main__":
    sortList = [1, 4, 3, 11, 3, -13, 3, 0, 99]
    print("Original list", sortList)
    print("Sorted List", merge_sort(sortList))
