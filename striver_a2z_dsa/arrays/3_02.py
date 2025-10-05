# Find Second Smallest and Second Largest Element in an array


def getSecLargest(nums):
    largest_num = float('-inf')
    sec_largest_num = float('-inf')

    for num in nums:
        if num > largest_num:
            sec_largest_num = largest_num
            largest_num = num
        elif num > sec_largest_num and num < largest_num:
            sec_largest_num = num

    return sec_largest_num


def getSecSmallest(nums):
    smallest_num = float('inf')
    sec_smallest_num = float('inf')

    for i in range(len(nums)):
        if nums[i] < smallest_num:
            sec_smallest_num = smallest_num
            smallest_num = nums[i]

    return sec_smallest_num


if __name__ == "__main__":
    list_values = [13, 46, 24, 52, 20, 9, -1, -10, 32, 32, 100, 123, 112]
    print("Second Largest Element respectively", getSecLargest(list_values))
    print("Second Smallest Element respectively", getSecSmallest(list_values))
