# insertion sort implementation using recursion

def insertion_sort(nums, index, n):

    if index == n:
        return

    pointer = index
    while pointer > 0 and nums[pointer - 1] > nums[pointer]:
        nums[pointer - 1], nums[pointer] = nums[pointer], nums[pointer - 1]
        pointer -= 1

    insertion_sort(nums, index + 1, n)

    return nums


if __name__ == "__main__":
    sortList = [13, 46, 24, 52, 20, 9, -1, -10, 32, 32]
    print("Original list", sortList)
    print("Sorted List", insertion_sort(sortList, 0, len(sortList)))
