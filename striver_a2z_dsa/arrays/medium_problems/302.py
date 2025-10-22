# Sort an array of 0s, 1s and 2s

def after_sort(nums):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for num in nums:
        if num == 0:
            count_0 += 1
        if num == 1:
            count_1 += 1
        if num == 2:
            count_2 += 1

    for i in range(count_0):
        nums[i] = 0
    for i in range(count_0, count_0 + count_1):
        nums[i] = 1
    for i in range(count_0 + count_1, len(nums)):
        nums[i] = 2

    return nums


def sort_using_dutch_National_flag_algorithm(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


if __name__ == "__main__":
    nums = [0, 2, 1, 2, 0, 0, 2, 1]
    print(f"Original list: {nums}")
    print(f"After sorting: {after_sort(nums)}")
    print(
        f"Sorting using Dutch National flag algorithm: {sort_using_dutch_National_flag_algorithm(nums)}")
