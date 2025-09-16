# bubble sort implementation using recursion

def bubble_sort(nums, n):
    if n == 1:
        return

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

    bubble_sort(nums, n - 1)

    return nums


if __name__ == "__main__":
    sortList = [13, 46, 24, 52, 20, 9, -1]
    print("Original list", sortList)
    print("Sorted List", bubble_sort(sortList, len(sortList)))
