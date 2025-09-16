# Quick sort algorithm implementation

def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high

    while i < j:
        while i <= high and nums[i] <= pivot:
            i += 1
        while j >= low and nums[j] > pivot:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]

    return j


def quick_sort(nums, low, high):
    if low < high:
        j = partition(nums, low, high)
        quick_sort(nums, low, j - 1)
        quick_sort(nums, j + 1, high)

    return nums


if __name__ == "__main__":
    sortList = [13, 46, 24, 52, 20, 9, -1, -10, 32, 32]
    print("Original list", sortList)
    print("Sorted List", quick_sort(sortList, 0, len(sortList) - 1))
