# Remove Duplicates in-place from Sorted Array

def remDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == "__main__":
    list_values = [1, 1, 24, 24, 9, 9, -10, 32, 32, 100]
    print(remDuplicates(list_values))
